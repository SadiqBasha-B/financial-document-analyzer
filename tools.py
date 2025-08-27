import os
import re
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PyPDFLoader as Pdf

# Search Tool
search_tool = SerperDevTool()

# Custom PDF Reader Tool
class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        """Read data from a PDF file and clean it"""
        docs = Pdf(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content
            # Remove multiple newlines
            content = re.sub(r'\n+', '\n', content).strip()
            full_report += content + "\n"

        return full_report


# Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        """Analyze financial document data"""
        processed_data = re.sub(r'\s+', ' ', financial_document_data)
        # TODO: Implement real investment analysis
        return "Investment analysis functionality to be implemented"


# Risk Assessment Tool
class RiskTool:
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        # TODO: Implement real risk assessment
        return "Risk assessment functionality to be implemented"
