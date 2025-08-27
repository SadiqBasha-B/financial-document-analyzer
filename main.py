from fastapi import FastAPI, File, UploadFile, Form
import os
import uuid
from celery_worker import analyze_document_task

app = FastAPI(title="Financial Document Analyzer with Queue & DB")

@app.post("/analyze")
async def analyze_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    os.makedirs("data", exist_ok=True)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    if not query:
        query = "Analyze this financial document for investment insights"

    # Queue the task
    task = analyze_document_task.delay(file_path=file_path, query=query, file_name=file.filename)

    return {
        "status": "queued",
        "task_id": task.id,
        "message": "Your document analysis has been queued and will be processed shortly."
    }

@app.get("/result/{task_id}")
def get_result(task_id: str):
    from celery_worker import celery_app
    res = celery_app.AsyncResult(task_id)
    if res.ready():
        return {"status": "completed", "result": res.result}
    else:
        return {"status": "pending", "result": None}
