from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app import db


class ReserveInfo(db.Model):
    reserve_id = Column(Integer, primary_key=True)
    patient_name = Column(String(50), nullable=False)
    reserve_clinic = Column(String(20), nullable=False)
    reserve_time = Column(DateTime, nullable=False)
