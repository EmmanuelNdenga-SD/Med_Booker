from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    status = Column(String, default='Scheduled')

    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))

    patient = relationship("Patient", backref="appointments")
    doctor = relationship("Doctor", backref="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, datetime={self.datetime}, status='{self.status}')>"