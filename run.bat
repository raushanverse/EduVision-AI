@echo off
echo 🎯 EduVision AI - Smart Career Guidance
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if requirements are installed
echo 📦 Checking dependencies...
python -c "import streamlit, requests" >nul 2>&1
if errorlevel 1 (
    echo 🔧 Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed
) else (
    echo ✅ Dependencies are already installed
)

echo.
echo 🚀 Starting EduVision AI...
echo 📱 The application will open in your default browser
echo 🔗 URL: http://localhost:8501
echo ⏹️  Press Ctrl+C to stop the application
echo ================================================
echo.

REM Run the application
python -m streamlit run main.py

pause
