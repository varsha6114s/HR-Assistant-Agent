#!/bin/bash

# HR Assistant Agent - Run Script
# This script activates the virtual environment and runs the Streamlit app

echo "Starting HR Assistant Agent..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Warning: .env file not found!"
    echo "Please create a .env file with your OPENAI_API_KEY"
    echo "You can copy .env.example and add your API key"
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Activate virtual environment
source venv/bin/activate

# Run Streamlit app
echo "Launching Streamlit app..."
echo "The app will open in your browser at http://localhost:8501"
echo ""
streamlit run app.py
