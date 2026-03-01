from pydantic import BaseModel, Field

class Expense(BaseModel): 
    amount: float = Field(gt=0)
    category: str
    description: str