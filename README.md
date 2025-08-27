📊 Financial Document Analyzer (CrewAI + Celery + DB)

A Financial Document Analyzer built with CrewAI, FastAPI, Celery, Redis, and SQLite.
This system allows users to upload financial documents (PDFs), process them asynchronously using a queue worker, and retrieve results later.
It also stores all analysis results in a database for future reference.

✨ Features

📂 Upload financial documents (PDF) for analysis

⚡ Asynchronous processing with Celery + Redis (queue worker model)

🗄️ Database integration (SQLite) to store analysis results

🔍 Investment Analysis Tool (placeholder for financial logic)

⚠️ Risk Assessment Tool (placeholder for risk models)

🚀 Built with FastAPI for easy API access

🛠️ Setup Instructions
1. Clone Repository
git clone https://github.com/yourusername/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt


If requirements.txt is missing, install manually:

pip install fastapi uvicorn python-dotenv crewai crewai_tools langchain sqlalchemy celery redis aiosqlite

4. Start Redis Server

Ensure Redis is running locally:

redis-server

5. Start Celery Worker
celery -A celery_worker.celery_app worker --loglevel=info

6. Start FastAPI Server
uvicorn main:app --reload

📌 API Endpoints
1. Upload & Queue Analysis

POST /analyze
Upload a PDF document and queue for analysis.

Request:

file: Financial PDF file

query: Custom query for analysis (optional)

Example:
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@data/sample.pdf" \
  -F "query=Analyze this report for investment insights"

Response:
{
  "status": "queued",
  "task_id": "d9f84d29-4b5e-4a10-a1fb-2a2b41f8bda9",
  "message": "Your document analysis has been queued and will be processed shortly."
}

2. Check Analysis Result

GET /result/{task_id}

Example:
curl http://127.0.0.1:8000/result/d9f84d29-4b5e-4a10-a1fb-2a2b41f8bda9

Response (if pending):
{
  "status": "pending",
  "result": null
}

Response (when completed):
{
  "status": "completed",
  "result": "Investment analysis functionality to be implemented"
}

🗄️ Database

Database: SQLite (financial_analysis.db)

Table: analysis_results

Schema:
Column	Type	Description
id	Integer	Primary key
file_name	String	Uploaded file name
query	String	User query
analysis	Text	Analysis result
timestamp	DateTime	When the analysis was created
🐛 Bugs Fixed

Missing Imports

Added missing imports like Pdf loader, uuid, etc.

Async Misuse

Some tools used async unnecessarily → converted to standard sync functions.

Whitespace Cleanup

Fixed infinite loop risk in string cleanup (while loop for spaces).

Error Handling

Added file existence check before PDF parsing.

Inefficient Prompts

Simplified prompts and removed redundant formatting.

🚀 Future Improvements


✅ Add user authentication (JWT/OAuth2)

✅ Enhance investment and risk analysis logic

✅ Deploy with Docker + Kubernetes for scalability

✅ Switch DB to PostgreSQL / Firebase for production
