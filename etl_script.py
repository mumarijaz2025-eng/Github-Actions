import json
import random
from datetime import datetime

print("--- STARTING ETL JOB ---")
data = {
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "users_processed": random.randint(100, 500),
    "status": "SUCCESS"
}
print(json.dumps(data, indent=2))
print("--- JOB FINISHED ---")
