from app.models.formula import Formula
from app.db.database import SessionLocal
from app.schemas.formula import FormulaCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas.formula import FormulaUpdate

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

async def update_formula(id: int, formula_update: FormulaUpdate):
    async with SessionLocal() as session:
        async with session.begin():
            result = await session.execute(select(Formula).where(Formula.id == id))
            formula = result.scalars().first()
            if not formula:
                return None

            formula.latex = formula_update.latex
            formula.description = formula_update.description
            session.add(formula)
            await session.commit()
            await session.refresh(formula)
            return formula

async def delete_formula(id: int):
    async with SessionLocal() as session:
        async with session.begin():
            result = await session.execute(select(Formula).where(Formula.id == id))
            formula = result.scalars().first()
            if not formula:
                return False

            await session.delete(formula)
            await session.commit()
            return True

