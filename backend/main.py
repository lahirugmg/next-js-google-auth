from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Business Expense Tracker API",
    description="Backend API for the business expense tracker application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for transaction data
class TransactionCreate(BaseModel):
    amount: float
    description: str
    category: str
    date: str
    type: str

class Transaction(TransactionCreate):
    id: int

# In-memory storage for transactions (replace with database in production)
transactions: List[Transaction] = []
transaction_id_counter = 1

@app.get("/")
async def root():
    return {"message": "Business Expense Tracker API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

@app.post("/transactions", response_model=Transaction)
async def create_transaction(transaction: TransactionCreate):
    global transaction_id_counter
    
    # Validate transaction type
    if transaction.type not in ["expense", "income"]:
        raise HTTPException(status_code=400, detail="Transaction type must be 'expense' or 'income'")
    
    # Validate amount
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    
    # Create new transaction with ID
    new_transaction = Transaction(
        id=transaction_id_counter,
        **transaction.dict()
    )
    
    transactions.append(new_transaction)
    transaction_id_counter += 1
    
    return new_transaction

@app.get("/transactions", response_model=List[Transaction])
async def get_transactions():
    return transactions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 