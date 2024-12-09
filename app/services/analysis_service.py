from app.models.formula import Formula
from app.db.database import SessionLocal
from sqlalchemy.future import select
from sympy.parsing.latex import parse_latex
from sympy import simplify
from typing import List

async def analyze_formulas(input_formulas: List[str]):
    async with SessionLocal() as session:
        async with session.begin():
            # Получаем все формулы из базы данных
            result = await session.execute(select(Formula))
            formulas_in_db = result.scalars().all()

            analysis_results = []

            for input_formula in input_formulas:
                best_match = None
                highest_similarity = 0.0
                try:
                    input_sympy = simplify(parse_latex(input_formula))
                except Exception:
                    analysis_results.append({
                        "input_formula": input_formula,
                        "formula_in_db": None,
                        "similarity_percentage": 0.0,
                        "error": "Invalid LaTeX format"
                    })
                    continue

                for formula in formulas_in_db:
                    try:
                        db_sympy = simplify(parse_latex(formula.latex))
                        if input_sympy.equals(db_sympy):
                            similarity = 100.0  # Формулы идентичны
                        else:
                            similarity = 0.0  # Формулы разные, можно доработать частичное совпадение

                        if similarity > highest_similarity:
                            highest_similarity = similarity
                            best_match = formula
                    except Exception:
                        continue

                analysis_results.append({
                    "input_formula": input_formula,
                    "formula_in_db": best_match.latex if best_match else None,
                    "similarity_percentage": highest_similarity
                })

            return analysis_results