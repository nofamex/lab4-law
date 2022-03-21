from http.client import HTTPException
from fastapi import Depends, FastAPI, UploadFile
from mahasiswa import service, models, schema
from file import schema as FileSchema
from file import service as FileService
from sqlalchemy.orm import Session
from mahasiswa.database import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/mahasiswa", response_model=schema.Mahasiswa)
def create_mahasiswa(mahasiswa: schema.MahasiswaCreate, db:Session = Depends(get_db)):
    mahasiswa = service.create_mahasiswa(db=db, mahasiswa=mahasiswa)
    return mahasiswa

@app.put("/mahasiswa/{npm}", response_model=schema.Mahasiswa)
def update_mahasiswa(npm:int, mahasiswa: schema.MahasiswaUpdate, db:Session = Depends(get_db)):
    updated_mahasiswa = service.update_mahasiswa(db=db, mahasiswa=mahasiswa, npm=npm)

    if updated_mahasiswa is None:
        raise HTTPException(status_code=400, detail="No mahasiswa with given npm")

    return updated_mahasiswa

@app.get("/mahasiswa/{npm}", response_model=schema.Mahasiswa)
def get_mahasiswa_by_npm(npm: int, db:Session = Depends(get_db)):
    mahasiswa = service.get_mahasiswa(db=db, npm=npm)

    if mahasiswa is None:
        raise HTTPException(status_code=400, detail="No mahasiswa with given npm")
    
    return mahasiswa

@app.delete("/mahasiswa/{npm}", response_model=schema.Mahasiswa)
def delete_mahasiswa(npm: int, db:Session = Depends(get_db)):
    deleted_mahasiswa = service.delete_mahasiswa(db=db, npm=npm)

    if deleted_mahasiswa is None:
        raise HTTPException(status_code=400, detail="No mahasiswa with given npm")
    
    return deleted_mahasiswa

@app.post("/file", response_model=FileSchema.File)
def upload_file(file: UploadFile, db:Session = Depends(get_db)):
    uploaded_file = FileService.upload_file(db=db, file=file)

    if uploaded_file is None:
        raise HTTPException(status_code=400, detail="Already exist file with given name")

    return uploaded_file

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)