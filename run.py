#!/usr/bin/env python3
"""
EduVision AI - Quick Run Script
This script provides an easy way to run the application with proper setup.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version meets requirements."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import requests
        print("✅ Required dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def run_application():
    """Run the Streamlit application."""
    print("🚀 Starting EduVision AI...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    """Main function to run the application."""
    print("🎯 EduVision AI - Smart Career Guidance")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n🔧 Installing dependencies...")
        if not install_dependencies():
            sys.exit(1)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    print("\n🎉 All checks passed! Starting application...")
    print("📱 The application will open in your default browser")
    print("🔗 URL: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    # Run the application
    run_application()

if __name__ == "__main__":
    main()
