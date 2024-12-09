from fastapi import APIRouter, HTTPException
from app.schemas.formula import FormulaCreate, FormulaResponse, FormulaUpdate
from app.services.formula_service import create_formula, get_formula_by_id, update_formula, delete_formula

router = APIRouter()

@router.post("/", response_model=FormulaResponse)
async def create_formula_endpoint(formula: FormulaCreate):
    return await create_formula(formula)

@router.get("/")
async def get_formulas():
    return {"message": "List of formulas"}

@router.put("/{id}", response_model=FormulaResponse)
async def update_formula_endpoint(id: int, formula_update: FormulaUpdate):
    formula = await update_formula(id, formula_update)
    if not formula:
        raise HTTPException(status_code=404, detail="Formula not found")
    return formula

@router.delete("/{id}", status_code=204)
async def delete_formula_endpoint(id: int):
    success = await delete_formula(id)
    if not success:
        raise HTTPException(status_code=404, detail="Formula not found")
