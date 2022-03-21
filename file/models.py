from enum import unique
from sqlalchemy import Column, String
from mahasiswa.database import Base

class File(Base):
    __tablename__ = 'file'

    name = Column(String, primary_key=True, index=True)
    path = Column(String, nullable=False, unique=True)