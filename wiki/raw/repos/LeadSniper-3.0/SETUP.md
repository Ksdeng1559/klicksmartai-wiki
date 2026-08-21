# LeadSniper 3.0 - Setup Guide

## Quick Start with Init Script

The easiest way to set up LeadSniper 3.0 is using the automated initialization script.

### Option 1: Using npm (Recommended)
```bash
npm run init
```

### Option 2: Using Node.js directly
```bash
node init.js
```

### Option 3: Using Bash (Linux/Mac)
```bash
chmod +x init.sh
./init.sh
```

## What the Init Script Does

The initialization script automates the following:

1. ✅ **Checks Node.js version** - Ensures you have Node.js 16+
2. ✅ **Creates `.env.local`** - Sets up environment configuration file
3. ✅ **Installs dependencies** - Runs `npm install` automatically
4. ✅ **Validates setup** - Checks if API key is configured
5. ✅ **Displays project info** - Shows available commands

## Manual Setup (Alternative)

If you prefer to set up manually:

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment
Create a `.env.local` file in the project root:

```env
# Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: DataForSEO API
# DATAFORSEO_LOGIN=your_login_here
# DATAFORSEO_PASSWORD=your_password_here

# Development Settings
VITE_APP_NAME=LeadSniper 3.0
VITE_APP_VERSION=3.0.0
```

### 3. Get Your Gemini API Key
1. Visit: https://aistudio.google.com/app/apikey
2. Create or sign in to your Google account
3. Generate a new API key
4. Copy the key and paste it in `.env.local`

### 4. Start Development Server
```bash
npm run dev
```

## Project Structure

```
LeadSniper-3.0/
├── components/          # React components
│   ├── AuditPanel.tsx   # AI audit interface
│   ├── Dashboard.tsx    # Main dashboard
│   └── LeadCard.tsx     # Lead display card
├── services/            # Business logic & API integrations
│   ├── dataForSeo.ts    # SEO data service
│   ├── geminiService.ts # Gemini AI integration
│   └── leadLogic.ts     # Lead generation logic
├── App.tsx              # Main app component
├── types.ts             # TypeScript definitions
├── init.js              # Initialization script (Node)
├── init.sh              # Initialization script (Bash)
└── .env.local           # Environment variables (create this)
```

## Available Commands

| Command | Description |
|---------|-------------|
| `npm run init` | Initialize project setup |
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |

## Tech Stack

- **Frontend**: React 19 + TypeScript
- **Build Tool**: Vite 6.2
- **AI Integration**: Google Gemini AI
- **Icons**: Lucide React
- **SEO Data**: DataForSEO API (optional)

## Troubleshooting

### "Node.js not found"
Install Node.js 16+ from: https://nodejs.org/

### "Dependencies failed to install"
Try:
```bash
rm -rf node_modules package-lock.json
npm install
```

### "API key not working"
1. Verify your API key is correct in `.env.local`
2. Ensure no spaces before/after the key
3. Restart the dev server after changing `.env.local`

### Port 3000 already in use
The dev server will automatically try the next available port (3001, 3002, etc.)

## Next Steps

1. ✅ Run initialization script
2. ✅ Add your Gemini API key
3. ✅ Start development server
4. 🚀 Begin developing your Lead Generation features!

## Support

For issues or questions:
- View your app in AI Studio: https://ai.studio/apps/drive/1NlwIud13hu8NghL0EUfrLf-j1ULLaVAW
- Check the main README.md for additional information
