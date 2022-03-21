from typing import Optional
from pydantic import BaseModel

class MahasiswaBase(BaseModel):
    name: str
    address: str

class MahasiswaCreate(MahasiswaBase):
    npm: int

class MahasiswaUpdate(MahasiswaBase):
    name: Optional[str]
    address: Optional[str]

class Mahasiswa(MahasiswaCreate):
    class Config:
        orm_mode = True