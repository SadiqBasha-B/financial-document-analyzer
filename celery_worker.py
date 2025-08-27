from celery import Celery
# from main import run_crew  # Removed because run_crew is not defined in main.py
from database import SessionLocal, AnalysisResult
import os
import uuid

# Redis broker
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def analyze_document_task(file_path: str, query: str, file_name: str):
    # Run CrewAI
    result = None  # Placeholder since run_crew is not defined

    # Save result in DB
    db = SessionLocal()
    db_result = AnalysisResult(
        file_name=file_name,
        query=query,
        analysis=str(result)
    )
    db.add(db_result)
    db.commit()
    db.close()

    # Clean up uploaded file
    if os.path.exists(file_path):
        os.remove(file_path)

    return str(result)