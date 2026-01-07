import json
import random
from datetime import datetime

# Simulate fetching data
print("--- STARTING ETL JOB ---")

data = {
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "users_processed": random.randint(100, 500),
    "status": "SUCCESS"
}

# Simulate processing
print(f"Processing data for {data['date']}...")
print(f"Total users found: {data['users_processed']}")

# Output result as JSON
print(json.dumps(data, indent=2))

print("--- JOB FINISHED ---")
