from fastapi import APIRouter
from app.schemas.analysis import FormulaAnalysisRequest, FormulaAnalysisResponse
from app.services.analysis_service import analyze_formula

router = APIRouter()

@router.post("/", response_model=FormulaAnalysisResponse)
async def analyze_formula_endpoint(request: FormulaAnalysisRequest):
    return await analyze_formula(request)
