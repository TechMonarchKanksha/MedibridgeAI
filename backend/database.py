from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(DateTime)
    medical_records = relationship('MedicalRecord', back_populates='patient')

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    appointments = relationship('Appointment', back_populates='doctor')

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date = Column(DateTime, nullable=False)
    patient = relationship('Patient', back_populates='medical_records')
    doctor = relationship('Doctor', back_populates='appointments')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    record_details = Column(String)
    patient = relationship('Patient', back_populates='medical_records')

class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    reminder_time = Column(DateTime, nullable=False)
    appointment = relationship('Appointment')

# Database Initialization
engine = create_engine('sqlite:///medibridgeai.db') # Replace with your database URI
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
