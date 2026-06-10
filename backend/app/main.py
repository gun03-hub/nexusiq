from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.db.database import create_tables

# IMPORTANT
from app.models.user import User

app = FastAPI()

create_tables()

@app.get("/")
def root():
    return {"message": "NexusIQ API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}



app.include_router(auth_router)