@echo off
echo 🚀 DEPLOYING PRMSU CHATBOT TO RAILWAY
echo =====================================

echo 📝 Adding all changes to git...
git add .

echo 💾 Committing changes...
set /p commit_message="Enter commit message (or press Enter for default): "
if "%commit_message%"=="" set commit_message=Update PRMSU chatbot for Railway deployment

git commit -m "%commit_message%"

echo 🌐 Pushing to GitHub...
git push origin main

echo ✅ Code pushed to GitHub successfully!
echo 🚂 Now go to Railway.app to deploy:
echo    1. Go to https://railway.app
echo    2. Click 'New Project' → 'Deploy from GitHub repo'
echo    3. Select your 'chatbot' repository
echo    4. Set environment variables:
echo       COHERE_API_KEY=your_actual_cohere_api_key
echo       PORT=8000
echo       RAILWAY_ENVIRONMENT=production
echo       DB_PATH=/app/vector_db
echo    5. Deploy!

pause
