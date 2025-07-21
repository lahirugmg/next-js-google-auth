# Business Expense Tracker - Backend

This is the Python FastAPI backend for the Business Expense Tracker application.

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the environment file:
```bash
cp env.example .env
```

5. Update the `.env` file with your configuration.

## Running the Application

### Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
python main.py
```

## API Documentation

Once the server is running, you can access:
- API documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc
- Health check: http://localhost:8000/health

## Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── env.example         # Environment variables template
├── venv/               # Virtual environment (created)
└── README.md           # This file
``` 