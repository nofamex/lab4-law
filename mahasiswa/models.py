from sqlalchemy import Column, String, Integer
from .database import Base

class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'

    npm = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
