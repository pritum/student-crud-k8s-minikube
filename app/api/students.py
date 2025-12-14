from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.student_service import StudentService
from app.models.schemas import StudentCreate, StudentResponse

router = APIRouter()
service = StudentService()

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return service.create_student(db, student)

@router.get("/", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return service.list_students(db)

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = service.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
