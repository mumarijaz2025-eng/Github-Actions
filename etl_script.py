import pandas as pd
import random
from datetime import datetime

print("--- STARTING PANDAS JOB ---")

# 1. Create a fake dataset (Mocking an Extract step)
data = {
    'user_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'login_count': [random.randint(1, 10) for _ in range(5)]
}

# 2. Load into DataFrame (The Core Tool of Data Engineers)
df = pd.DataFrame(data)

# 3. Transform: Filter for active users
print("Raw Data:")
print(df)

print("\nProcessing: Finding top users...")
top_users = df[df['login_count'] > 5]

# 4. Show results
print("\nHigh Activity Users:")
print(top_users)

print("--- JOB FINISHED ---")
