# Business Expense Tracker - Frontend

This is the Next.js frontend for the Business Expense Tracker application with Google authentication.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Copy the environment file:
```bash
cp env.local.example .env.local
```

3. Configure Google OAuth:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google+ API
   - Go to "Credentials" and create an "OAuth 2.0 Client ID"
   - Set the authorized redirect URI to: `http://localhost:3000/api/auth/callback/google`
   - Copy the Client ID and Client Secret

4. Update `.env.local` with your Google OAuth credentials:
```env
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your-random-secret-key-here
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

5. Generate a random secret for NEXTAUTH_SECRET:
```bash
openssl rand -base64 32
```

## Running the Application

### Development Mode
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## Features

- **Google Authentication**: Sign in with Google account
- **Transaction Form**: Add expenses and income (requires authentication)
- **Responsive Design**: Works on desktop and mobile
- **TypeScript**: Full type safety
- **Tailwind CSS**: Modern styling

## Authentication Flow

1. User clicks "Sign in with Google"
2. Redirected to Google OAuth
3. After successful authentication, user is redirected back
4. User can now access the transaction form
5. User can sign out using the "Sign Out" button

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── api/auth/[...nextauth]/  # NextAuth API routes
│   │   ├── page.tsx                 # Main page
│   │   └── layout.tsx               # Root layout
│   └── components/
│       ├── LoginButton.tsx          # Google login/logout button
│       ├── TransactionForm.tsx      # Transaction form
│       └── Providers.tsx            # NextAuth session provider
├── .env.local                       # Environment variables
└── README.md                        # This file
```
