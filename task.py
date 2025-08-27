from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

# Task: Analyze Financial Document
analyze_financial_document = Task(
    description="""
    Analyze the uploaded financial document at {file_path}.
    Summarize key financial metrics, trends, and investment insights.
    Provide actionable recommendations supported by data in the document.
    Avoid hallucinations or fictional URLs.
    Output results in bullet points.
    """,
    expected_output="""
    - Key financial metrics
    - Observed trends
    - Document-based risks
    - Investment recommendations
    """,
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=True,
)

# Optional Verification Task
verification_task = Task(
    description="""
    Check if the uploaded file at {file_path} is a financial document.
    Summarize key sections and important financial indicators.
    Avoid inventing data; rely on actual content.
    """,
    expected_output="""
    - Document type
    - Sections summary
    - Key financial indicators
    """,
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=True,
)
