from fastapi import APIRouter
from app.schemas.expense import Expense
from app.services.expense_service import create_expense

router = APIRouter()

@router.post("/expenses")
def add_expense(expense: Expense):
    return create_expense(expense)