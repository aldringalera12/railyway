# 🚀 Railway Deployment Guide for PRMSU Chatbot

This guide will help you deploy the PRMSU FastAPI chatbot and vector database to Railway.

## 📋 Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **GitHub Repository**: Your code should be in a GitHub repository
3. **Cohere API Key**: Get one from [cohere.ai](https://cohere.ai)

## 🛠️ Deployment Steps

### Step 1: Prepare Your Repository

Ensure your repository contains these files:
- ✅ `fastapi_chatbot.py` - Main FastAPI application
- ✅ `chatbot.py` - Core chatbot functionality
- ✅ `definition_chunker.py` - Vector database management
- ✅ `requirements.txt` - Python dependencies
- ✅ `Dockerfile` - Container configuration
- ✅ `railway.json` - Railway deployment configuration
- ✅ `init_database.py` - Database initialization script
- ✅ All `.txt` files with PRMSU data
- ✅ `vector_db/` directory (will be created if missing)

### Step 2: Deploy to Railway

1. **Connect Repository**:
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Configure Environment Variables**:
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add these environment variables:
     ```
     COHERE_API_KEY=your_cohere_api_key_here
     PORT=8000
     RAILWAY_ENVIRONMENT=production
     DB_PATH=/app/vector_db
     ```

3. **Deploy**:
   - Railway will automatically detect the `Dockerfile`
   - The build process will start automatically
   - Wait for deployment to complete (usually 2-5 minutes)

### Step 3: Initialize Database

The database will be automatically initialized during startup with all PRMSU data from the `.txt` files.

### Step 4: Test Your Deployment

1. **Get Your Railway URL**:
   - In Railway dashboard, find your app's URL
   - It will look like: `https://your-app-name.railway.app`

2. **Test Endpoints**:
   ```bash
   # Health check
   curl https://your-app-name.railway.app/health
   
   # Test chat
   curl -X POST https://your-app-name.railway.app/chat \
     -H "Content-Type: application/json" \
     -d '{"question": "What does PRMSU stand for?"}'
   ```

3. **API Documentation**:
   - Visit: `https://your-app-name.railway.app/docs`
   - Interactive API explorer: `https://your-app-name.railway.app/redoc`

## 🔧 Configuration Details

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `COHERE_API_KEY` | Your Cohere API key | Required |
| `PORT` | Server port | 8000 |
| `RAILWAY_ENVIRONMENT` | Environment type | production |
| `DB_PATH` | Vector database path | /app/vector_db |

### Docker Configuration

The `Dockerfile` includes:
- Python 3.11 slim base image
- System dependencies (gcc, g++)
- Python package installation
- Vector database directory creation
- Port exposure (8000)
- Startup command

### Railway Configuration

The `railway.json` includes:
- Dockerfile-based build
- Health check endpoint (`/health`)
- Restart policy configuration
- Port configuration from environment

## 📊 Database Initialization

The vector database is automatically populated with:
- ✅ University information and policies
- ✅ Academic requirements and procedures
- ✅ Student services and programs
- ✅ Disciplinary policies and penalties
- ✅ Scholarship and financial aid information
- ✅ Uniform and dress code policies
- ✅ Cross-enrollment procedures
- ✅ Graduation requirements and honors

## 🔍 Monitoring and Logs

1. **View Logs**:
   - In Railway dashboard, go to "Deployments"
   - Click on latest deployment
   - View build and runtime logs

2. **Health Monitoring**:
   - Railway automatically monitors the `/health` endpoint
   - App will restart if health checks fail

## 🚨 Troubleshooting

### Common Issues:

1. **Build Fails**:
   - Check that all required files are in repository
   - Verify `requirements.txt` is correct
   - Check Dockerfile syntax

2. **Database Empty**:
   - Ensure all `.txt` files are included in repository
   - Check initialization logs
   - Verify file paths are correct

3. **API Key Issues**:
   - Verify `COHERE_API_KEY` environment variable is set
   - Check API key is valid and has sufficient credits

4. **Memory Issues**:
   - Railway provides 512MB RAM by default
   - Vector database initialization may need more memory
   - Consider upgrading Railway plan if needed

### Debug Commands:

```bash
# Check database health
curl https://your-app-name.railway.app/database/health

# List definitions
curl https://your-app-name.railway.app/database/definitions

# Test specific question
curl -X POST https://your-app-name.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the admission requirements?"}'
```

## 🎉 Success!

Once deployed, your PRMSU chatbot will be available at:
- **API Base URL**: `https://your-app-name.railway.app`
- **Documentation**: `https://your-app-name.railway.app/docs`
- **Health Check**: `https://your-app-name.railway.app/health`

The chatbot will:
- ✅ Only answer PRMSU student handbook questions
- ✅ Provide user-friendly formatted responses
- ✅ Include complete information (like campus location)
- ✅ Reject non-PRMSU topics and bypass attempts
- ✅ Handle all the advanced question types you've tested

## 📱 Android Integration

Your Android app can now connect to:
```
Base URL: https://your-app-name.railway.app
Chat Endpoint: POST /chat
Content-Type: application/json
Body: {"question": "your question here"}
```

The API is ready for production use! 🚀
