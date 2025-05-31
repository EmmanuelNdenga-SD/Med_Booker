from db.connection import engine
from models.base import Base
import models.patient
import models.doctor
import models.appointment
from cli.menu import show_menu

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
    show_menu()