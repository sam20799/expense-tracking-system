from fastapi import FastAPI,HTTPException

import db_helper
from datetime import date
from typing import  List
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

class MonthRange(BaseModel):
    month_name: str
    total: float




@app.get('/expenses/{expense_date}',response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expense_for_date(expense_date)
    return expenses

@app.post('/expenses/{expense_date}')
def insert_expenses(expense_date: date, expenses:List[Expense]):
    db_helper.delete_record(expense_date)
    for expense in expenses:
        db_helper.insert_record(expense_date,expense.amount,expense.category,expense.notes)

    return {"message": 'Record inserted successfully'}

@app.post('/analytics')
def get_analytics(date_range: DateRange):
    data = db_helper.get_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail='failed to retrieve expense summary')

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        pct = round(row['total']*100/total,2)
        breakdown[row['category']] =  {
            'total': row['total'],
            'percentage': pct
        }

    return breakdown

@app.get('/monthlyAnalytics',response_model=List[MonthRange])
def get_monthly_analytics():
    data = db_helper.get_monthly_summary()
    return data



