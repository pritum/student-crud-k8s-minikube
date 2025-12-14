import json
from app.repositories.student_repository import StudentRepository
from app.cache.redis_client import redis_client

repo = StudentRepository()

class StudentService:

    def get_student(self, db, student_id: int):
        cache_key = f"student:{student_id}"

        # Try cache
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)

        # Fallback to DB
        student = repo.get_by_id(db, student_id)
        if not student:
            return None

        # Store in cache
        redis_client.setex(
            cache_key,
            300,  # 5 minutes
            json.dumps({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "email": student.email
            })
        )

        return student

    def create_student(self, db, student):
        new_student = repo.create(db, student)
        # Invalidate cache if needed (safe)
        redis_client.flushdb()
        return new_student