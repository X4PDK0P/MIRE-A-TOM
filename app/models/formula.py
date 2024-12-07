from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Formula(Base):
    __tablename__ = "formulas"
    id = Column(Integer, primary_key=True, index=True)
    latex = Column(String, nullable=False)
    description = Column(String, nullable=True)
