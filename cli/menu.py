from db.connection import session
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from datetime import datetime

def show_menu():
    while True:
        print("\n--- Medical Appointment Manager ---")
        print("1. Add patient")
        print("2. Add doctor")
        print("3. Schedule appointment")
        print("4. View all appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            add_doctor()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_appointments()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def add_patient():
    name = input("Patient name: ")
    birth_date_str = input("Date of birth (YYYY-MM-DD): ")
    phone = input("Phone number: ")

    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    except ValueError:
        print(" Invalid date format. Use YYYY-MM-DD.")
        return

    patient = Patient(name=name, birth_date=birth_date, phone=phone)
    session.add(patient)
    session.commit()
    print(f" Patient '{name}' added.")

def add_doctor():
    name = input("Doctor name: ")
    specialty = input("Specialty: ")

    doctor = Doctor(name=name, specialty=specialty)
    session.add(doctor)
    session.commit()
    print(f" Doctor '{name}' added.")

def schedule_appointment():
    try:
        patient_id = int(input("Patient ID: "))
        doctor_id = int(input("Doctor ID: "))
        datetime_str = input("Appointment date & time (YYYY-MM-DD HH:MM): ")
        appointment_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print(" Invalid input format.")
        return

    appointment = Appointment(
        datetime=appointment_datetime,
        patient_id=patient_id,
        doctor_id=doctor_id
    )
    session.add(appointment)
    session.commit()
    print(" Appointment scheduled.")

def view_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
        return

    for a in appointments:
        print(f"ID: {a.id} | Date: {a.datetime.strftime('%Y-%m-%d %H:%M')} | "
              f"Patient: {a.patient.name} | Doctor: {a.doctor.name} | Status: {a.status}")

def view_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
        return

    print("\n--- List of Appointments ---")
    for a in appointments:
        print(
            f"ID: {a.id} | Date: {a.datetime.strftime('%Y-%m-%d %H:%M')} | "
            f"Patient: {a.patient.name} | Doctor: {a.doctor.name} "
            f"({a.doctor.specialty}) | Status: {a.status}"
        )