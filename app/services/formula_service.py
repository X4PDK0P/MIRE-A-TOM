from app.models.formula import Formula
from app.db.database import SessionLocal
from app.schemas.formula import FormulaCreate

async def create_formula(data: FormulaCreate):
    async with SessionLocal() as session:
        formula = Formula(**data.dict())
        session.add(formula)
        await session.commit()
        await session.refresh(formula)
        return formula

async def get_formula_by_id(id: int):
    async with SessionLocal() as session:
        return await session.get(Formula, id)
