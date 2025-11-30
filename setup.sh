#!/bin/bash

# HR Assistant Agent - Setup Script
# This script sets up the environment and installs all dependencies

echo "Setting up HR Assistant Agent..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a .env file with your OpenAI API key:"
echo "   cp .env.example .env"
echo "   # Then edit .env and add your API key"
echo ""
echo "2. Run the application:"
echo "   ./run.sh"
echo ""
