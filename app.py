import pandas as pd
import os
from datetime import datetime

# Define the output directory relative to where the script will run
# We'll use a standard path that Docker can easily mount
OUTPUT_DIR = "/app/downloads"
OUTPUT_FILENAME = f"dummy_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
FULL_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

# Create the output directory if it doesn't exist
# This is crucial inside the Docker container
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("--- Starting Data Generation ---")

# 1. Generate Dummy Data
data = {
    'ID': range(1, 11),
    'Name': [f'User_{i}' for i in range(1, 11)],
    'Value': [i * 10.5 for i in range(1, 11)],
    'Date': [datetime.now().date()] * 10
}
df = pd.DataFrame(data)

print(f"Generated {len(df)} rows of data.")

# 2. Export to CSV
try:
    df.to_csv(FULL_PATH, index=False)
    print(f"Data successfully exported to: {FULL_PATH}")
    print("--- Process Complete ---")

except Exception as e:
    print(f"An error occurred during export: {e}")