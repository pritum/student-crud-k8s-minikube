from sqlalchemy.orm import Session
from app.models.db_models import Student

class StudentRepository:
    def create(self, db: Session, student):
        db_student = Student(**student.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    def get_all(self, db: Session):
        return db.query(Student).all()

    def get_by_id(self, db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()
