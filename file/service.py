import shutil
from fastapi import UploadFile
from sqlalchemy.orm import Session
from . import models

def upload_file(db: Session, file: UploadFile):
    duplicate = db.query(models.File).filter(models.File.name == file.filename).first()

    if duplicate is not None:
        return None

    DEFAULT_PATH = './uploads/' + file.filename

    with open(DEFAULT_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    uploaded_file = models.File(name=file.filename, path=DEFAULT_PATH)

    db.add(uploaded_file)
    db.commit()

    return uploaded_file