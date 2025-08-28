#!/usr/bin/env python3
"""
Helper script for Railway deployment preparation
"""

import os
import shutil
import json

def check_deployment_readiness():
    """Check if all required files are present for Railway deployment."""
    print("🔍 CHECKING RAILWAY DEPLOYMENT READINESS")
    print("="*60)
    
    required_files = [
        "fastapi_chatbot.py",
        "chatbot.py", 
        "definition_chunker.py",
        "requirements.txt",
        "Dockerfile",
        "railway.json",
        "init_database.py"
    ]
    
    data_files = [
        "individual_definition.txt",
        "critical_university_info.txt",
        "comprehensive_fixes.txt",
        "corrections_and_additions.txt",
        "advanced_question_fixes.txt",
        "uniform_and_assistant_fixes.txt",
        "liquor_offense_penalties.txt",
        "private_scholarship_fix.txt",
        "prmsu_location_info.txt",
        "type_of_cross_enrollment.txt",
        "inbound_cross_enrolment.txt"
    ]
    
    print("📋 REQUIRED FILES:")
    missing_required = []
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - MISSING")
            missing_required.append(file)
    
    print(f"\n📄 DATA FILES:")
    missing_data = []
    for file in data_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ⚠️  {file} - Missing (optional)")
            missing_data.append(file)
    
    print(f"\n📁 DIRECTORIES:")
    if os.path.exists("vector_db"):
        print(f"   ✅ vector_db/ directory exists")
    else:
        print(f"   ⚠️  vector_db/ directory missing (will be created)")
    
    print(f"\n📊 SUMMARY:")
    print(f"   Required files: {len(required_files) - len(missing_required)}/{len(required_files)}")
    print(f"   Data files: {len(data_files) - len(missing_data)}/{len(data_files)}")
    
    if missing_required:
        print(f"\n❌ DEPLOYMENT NOT READY:")
        print(f"   Missing required files: {missing_required}")
        return False
    else:
        print(f"\n✅ DEPLOYMENT READY!")
        return True

def show_environment_variables():
    """Show the environment variables needed for Railway."""
    print(f"\n🔧 ENVIRONMENT VARIABLES FOR RAILWAY:")
    print("-"*60)
    print("Set these in your Railway project dashboard:")
    print()
    print("COHERE_API_KEY=your_cohere_api_key_here")
    print("PORT=8000")
    print("RAILWAY_ENVIRONMENT=production") 
    print("DB_PATH=/app/vector_db")
    print()
    print("⚠️  IMPORTANT: Replace 'your_cohere_api_key_here' with your actual Cohere API key!")

def show_deployment_steps():
    """Show the deployment steps."""
    print(f"\n🚀 RAILWAY DEPLOYMENT STEPS:")
    print("-"*60)
    print("1. Push your code to GitHub repository")
    print("2. Go to https://railway.app")
    print("3. Click 'New Project' → 'Deploy from GitHub repo'")
    print("4. Select your repository")
    print("5. Set environment variables (see above)")
    print("6. Wait for deployment to complete")
    print("7. Test your deployment using the provided URL")
    print()
    print("📚 For detailed instructions, see: RAILWAY_DEPLOYMENT.md")

def create_gitignore():
    """Create a .gitignore file for the project."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Test files (don't deploy test files)
test_*.py
*_test.py
demo_*.py
monitor_*.py
quick_*.py

# Local development
.env
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created .gitignore file")

def main():
    """Main function."""
    print("🚀 RAILWAY DEPLOYMENT HELPER")
    print("This script helps prepare your PRMSU chatbot for Railway deployment")
    print()
    
    # Check readiness
    ready = check_deployment_readiness()
    
    # Show environment variables
    show_environment_variables()
    
    # Show deployment steps
    show_deployment_steps()
    
    # Create .gitignore if it doesn't exist
    if not os.path.exists('.gitignore'):
        create_gitignore()
    
    print(f"\n🎉 PREPARATION COMPLETE!")
    
    if ready:
        print("✅ Your project is ready for Railway deployment!")
        print("📚 Follow the steps above or see RAILWAY_DEPLOYMENT.md for details")
    else:
        print("⚠️  Please fix the missing files before deploying")
    
    print(f"\n📱 After deployment, your Android app can connect to:")
    print("   Base URL: https://your-app-name.railway.app")
    print("   Chat Endpoint: POST /chat")

if __name__ == "__main__":
    main()
