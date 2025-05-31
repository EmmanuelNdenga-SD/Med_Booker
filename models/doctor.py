from sqlalchemy import Column, Integer, String
from models.base import Base

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)

    def __repr__(self):
        return f"<Doctor(id={self.id}, name='{self.name}', specialty='{self.specialty}')>"