from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

class StudentResponse(StudentCreate):
    id: int
    class Config:
        orm_mode = True
