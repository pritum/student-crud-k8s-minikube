from fastapi import FastAPI
from app.api.students import router
from app.models.db_models import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student CRUD API")

app.include_router(router, prefix="/students")

@app.get("/health")
def health():
    return {"status": "ok"}
