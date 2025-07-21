# Business Expense Tracker

A full-stack application for tracking business expenses with Google authentication.

## Project Structure

```
├── frontend/           # Next.js frontend application
├── backend/            # Python FastAPI backend service
└── README.md          # This file
```

## Quick Start

### Frontend (Next.js)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

### Backend (Python FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Run the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at http://localhost:8000

## Features

- **Frontend**: Next.js with TypeScript, Tailwind CSS, and ESLint
- **Backend**: FastAPI with Python
- **Authentication**: Google OAuth (to be implemented)
- **Database**: Ready for integration (to be implemented)

## Development

Both frontend and backend are configured for development with hot reloading enabled.

For detailed setup instructions, see the README files in each directory:
- [Frontend README](./frontend/README.md)
- [Backend README](./backend/README.md)
