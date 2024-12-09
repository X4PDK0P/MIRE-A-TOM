from typing import List

from pydantic import BaseModel

class FormulaAnalysisRequest(BaseModel):
    formula: List[str]  # Список формул в формате LaTeX

class FormulaAnalysisResponse(BaseModel):
    results: List[dict]  # Список результатов для каждой формулы
