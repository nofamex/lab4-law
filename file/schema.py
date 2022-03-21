from pydantic import BaseModel

class FileBase(BaseModel):
    name: str
    path: str

class File(FileBase):
    class Config:
        orm_mode = True