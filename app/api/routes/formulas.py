from fastapi import APIRouter, HTTPException
from app.schemas.formula import FormulaCreate, FormulaResponse
from app.services.formula_service import create_formula, get_formula_by_id

router = APIRouter()

@router.post("/", response_model=FormulaResponse)
async def create_formula_endpoint(formula: FormulaCreate):
    return await create_formula(formula)

@router.get("/{id}", response_model=FormulaResponse)
async def get_formula(id: int):
    formula = await get_formula_by_id(id)
    if not formula:
        raise HTTPException(status_code=404, detail="Formula not found")
    return formula
