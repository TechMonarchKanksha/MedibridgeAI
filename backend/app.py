from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "medibridge.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            symptoms TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            doctor_name TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()

@app.route("/patients", methods=["GET", "POST"])
def patients():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if request.method == "POST":
        data = request.json
        cursor.execute(
            "INSERT INTO patients (name, age, symptoms) VALUES (?, ?, ?)",
            (data["name"], data["age"], data["symptoms"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Patient registered successfully"})

    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()

    patients_list = []
    for row in rows:
        patients_list.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "symptoms": row[3]
        })

    return jsonify(patients_list)

@app.route("/doctors", methods=["GET"])
def doctors():
    return jsonify([
        {"id": 1, "name": "Dr. Sharma", "specialization": "General Physician"},
        {"id": 2, "name": "Dr. Patel", "specialization": "Cardiologist"},
        {"id": 3, "name": "Dr. Mehta", "specialization": "Dermatologist"}
    ])

@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if request.method == "POST":
        data = request.json
        cursor.execute(
            "INSERT INTO appointments (patient_name, doctor_name, date) VALUES (?, ?, ?)",
            (data["patient_name"], data["doctor_name"], data["date"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Appointment booked successfully"})

    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    conn.close()

    appointments_list = []
    for row in rows:
        appointments_list.append({
            "id": row[0],
            "patient_name": row[1],
            "doctor_name": row[2],
            "date": row[3]
        })

    return jsonify(appointments_list)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
