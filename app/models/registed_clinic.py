from sqlalchemy import Column, Integer, String

from app import db


class RegistedClinic(db.Model):
    clinic_id = Column(Integer, primary_key=True)
    clinic_name = Column(String(50), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"RegistedClinic('{self.clinic_name}')"
