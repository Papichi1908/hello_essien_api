#!/bin/bash
#run.sh - starts the Flask development server
echo "Install dependencies..."
pip install -r requirements.txt

echo "Starting server..."
python app.py