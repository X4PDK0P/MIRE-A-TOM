from fastapi import FastAPI
from app.api.routes import formulas, analysis
from app.db.database import init_db

app = FastAPI(title="Math Formula API")

# Подключение маршрутов
app.include_router(formulas, prefix="/api/v1/formulas", tags=["Formulas"])
app.include_router(analysis, prefix="/api/v1/analysis", tags=["Analysis"])

@app.on_event("startup")
async def startup_event():
    await init_db()
