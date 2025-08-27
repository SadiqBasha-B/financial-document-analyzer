from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///financial_analysis.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    query = Column(String, nullable=False)
    analysis = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)
def save_analysis_result(file_name: str, query: str, analysis: str):
    """Save analysis result to the database"""
    db = SessionLocal()
    try:
        result = AnalysisResult(
            file_name=file_name,
            query=query,
            analysis=analysis
        )
        db.add(result)
        db.commit()
        db.refresh(result)
        return result
    finally:
        db.close()