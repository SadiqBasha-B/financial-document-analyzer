from crewai.agents import Agent
from tools import FinancialDocumentTool
from langchain_openai import ChatOpenAI

# Load LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Financial Analyst Agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze the uploaded financial document at {file_path} and provide clear investment insights.",
    verbose=True,
    memory=True,
    backstory="You are an experienced financial analyst who reads data carefully and reports accurately.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=10,
    allow_delegation=True
)

# Document Verifier Agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Determine if the uploaded file is a financial document and summarize key sections.",
    verbose=True,
    memory=True,
    backstory="You verify documents accurately, noting sections and key financial indicators.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=10,
    allow_delegation=True
)

# Investment Advisor Agent
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide investment recommendations based on the uploaded financial document at {file_path}.",
    verbose=True,
    backstory="You recommend investments grounded in document data.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=10,
    allow_delegation=False
)

# Risk Assessor Agent
risk_assessor = Agent(
    role="Risk Assessor",
    goal="Generate a risk assessment based on the financial document at {file_path}.",
    verbose=True,
    backstory="You identify realistic financial risks and provide mitigation strategies.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=10,
    allow_delegation=False
)
