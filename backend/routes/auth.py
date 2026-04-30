from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


# Define the blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# In-memory storage for users (for demo purposes)
users = {}


@auth_bp.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate data
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    
    # Hash the password and create the user record
    hashed_password = generate_password_hash(password)
    users[username] = {'password': hashed_password, 'role': 'patient'}
    return jsonify({'message': 'Patient registered successfully!'}), 201


@auth_bp.route('/register/doctor', methods=['POST'])
def register_doctor():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate data
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    
    # Hash the password and create the user record
    hashed_password = generate_password_hash(password)
    users[username] = {'password': hashed_password, 'role': 'doctor'}
    return jsonify({'message': 'Doctor registered successfully!'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401


