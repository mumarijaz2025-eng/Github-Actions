name: Python Data Pipeline

on: workflow_dispatch

jobs:
  run-etl:
    runs-on: ubuntu-latest
    
    steps:
      # CRITICAL STEP 1: Check out the code
      # Without this, the robot has an empty folder!
      - name: Check out code
        uses: actions/checkout@v3
      
      # CRITICAL STEP 2: Install Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      # Step 3: Run your script
      - name: Run ETL Script
        run: python etl_script.py
