from pydantic import BaseModel

class FormulaCreate(BaseModel):
    latex: str
    description: str

class FormulaResponse(FormulaCreate):
    id: int
    class Config:
        orm_mode = True

class FormulaUpdate(BaseModel):
    latex: str
    description: str

    class Config:
        from_attributes = True
