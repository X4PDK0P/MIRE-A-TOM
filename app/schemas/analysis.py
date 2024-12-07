from pydantic import BaseModel

class FormulaAnalysisRequest(BaseModel):
    formula: str

class FormulaAnalysisResponse(BaseModel):
    similarity_percentage: float
