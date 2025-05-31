from sqlalchemy import Column, Integer, String, Date
from models.base import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    phone = Column(String)

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.name}')>"
    