from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from app import db

# from sqlalchemy.orm import DeclarativeBase

Base = declarative_base()


class CommonClinic(db.Model):
    __abstract__ = True  # abstractクラスとして定義
    person_id = Column(Integer, primary_key=True)
    patient_name = Column(String(20), unique=True, nullable=False)
    patient_id_in_clinic = Column(String(20), unique=True, nullable=False)
    password_in_clinic = Column(String(20), unique=True, nullable=False)


class OmoriJibika(CommonClinic):
    __tablename__ = "omori_jibika"


class OmoriHihuka(CommonClinic):
    __tablename__ = "omori_hihuka"
