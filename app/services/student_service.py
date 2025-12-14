from sqlalchemy.orm import Session
from app.repositories.student_repository import StudentRepository

repo = StudentRepository()

class StudentService:
    def create_student(self, db: Session, student):
        return repo.create(db, student)

    def list_students(self, db: Session):
        return repo.get_all(db)

    def get_student(self, db: Session, student_id: int):
        return repo.get_by_id(db, student_id)
