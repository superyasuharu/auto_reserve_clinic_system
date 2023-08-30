from sqlalchemy import Column, Integer, String

from app import db


class User(db.Model):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    line_token = Column(String(512), unique=True, nullable=False)
