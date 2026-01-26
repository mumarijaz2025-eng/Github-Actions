# Automated Data Pipeline with GitHub Actions

This repository demonstrates a fully automated ETL (Extract, Transform, Load) pipeline using **GitHub Actions**. It showcases how to schedule and monitor data processing tasks in a cloud-native environment.

## Features
- **Automated Scheduling:** Uses GitHub Actions cron schedules to run data jobs daily.
- **Python-Based ETL:** A modular Python script that simulates data extraction, transformation, and reporting.
- **Dependency Management:** Automated environment setup using `requirements.txt`.
- **Workflow Monitoring:** Real-time logging and status tracking via the GitHub Actions dashboard.

## Tech Stack
- **Language:** Python 3.9
- **Libraries:** Pandas
- **Automation:** GitHub Actions

## Workflow Configuration
The pipeline is defined in `.github/workflows/demo1.yml` and includes:
1. **Trigger:** Scheduled to run daily at 08:00 UTC and supports manual triggers (`workflow_dispatch`).
2. **Environment:** Runs on `ubuntu-latest`.
3. **Steps:**
   - Repository checkout.
   - Python environment setup.
   - Dependency installation.
   - Execution of the ETL script.

## Getting Started
To replicate this setup:
1. Fork the repository.
2. Navigate to the **Actions** tab to enable workflows.
3. Manually trigger the "Python Data Pipeline" to verify the setup.
