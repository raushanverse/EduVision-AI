#!/bin/bash

echo "🎯 EduVision AI - Smart Career Guidance"
echo "================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import streamlit, requests" &> /dev/null; then
    echo "🔧 Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
    echo "✅ Dependencies installed"
else
    echo "✅ Dependencies are already installed"
fi

echo
echo "🚀 Starting EduVision AI..."
echo "📱 The application will open in your default browser"
echo "🔗 URL: http://localhost:8501"
echo "⏹️  Press Ctrl+C to stop the application"
echo "================================================"
echo

# Run the application
python3 -m streamlit run main.py
