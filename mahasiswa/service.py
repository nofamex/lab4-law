from sqlalchemy.orm import Session
from . import models, schema

def get_mahasiswa(db: Session, npm: int):
    return db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()

def create_mahasiswa(db: Session, mahasiswa: schema.MahasiswaCreate):
    db_item = models.Mahasiswa(npm=mahasiswa.npm, name=mahasiswa.name, address=mahasiswa.address)
    db.add(db_item)
    db.commit()
    return db_item

def update_mahasiswa(db: Session, npm:int, mahasiswa: schema.MahasiswaUpdate):
    updated_mahasiswa = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()

    if updated_mahasiswa is None:
        return None
    
    if mahasiswa.name:
        updated_mahasiswa.name = mahasiswa.name
    
    if mahasiswa.address:
        updated_mahasiswa.address = mahasiswa.address
    
    db.commit()

    return updated_mahasiswa

def delete_mahasiswa(db: Session, npm: int):
    deleted_mahasiswa = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()

    if deleted_mahasiswa is None:
        return None

    db.delete(deleted_mahasiswa)
    db.commit()

    return deleted_mahasiswa