from fastapi import APIRouter, HTTPException
from app.schemas.analysis import FormulaAnalysisRequest, FormulaAnalysisResponse
from app.services.analysis_service import analyze_formulas

router = APIRouter()

@router.post("/bulk", response_model=FormulaAnalysisResponse)
async def analyze_formulas_endpoint(request: FormulaAnalysisRequest):
    if not request.formulas:
        raise HTTPException(status_code=400, detail="No formulas provided in the request")

    results = await analyze_formulas(request.formulas)

    if not results:
        raise HTTPException(status_code=404, detail="No results found for the given formulas")

    return {"results": results}
