from db.connection import session
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from models.base import Base
from db.connection import engine
from datetime import datetime, date


Base.metadata.create_all(engine)


session.query(Appointment).delete()
session.query(Patient).delete()
session.query(Doctor).delete()


p1 = Patient(name="Khabib", birth_date=date(1990, 4, 12), phone="0700001111")
p2 = Patient(name="Israel Adesanya", birth_date=date(2012, 7, 23), phone="0700002222")


d1 = Doctor(name="Dr. James Bond", specialty="Cardiology")
d2 = Doctor(name="Dr. Beyonce", specialty="General Practice")

a1 = Appointment(datetime=datetime(2025, 6, 1, 10, 30), patient=p1, doctor=d1)
a2 = Appointment(datetime=datetime(2025, 6, 2, 14, 0), patient=p2, doctor=d2)


session.add_all([p1, p2, d1, d2, a1, a2])
session.commit()

print(" Database seeded with initial test data.")