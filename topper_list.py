import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Read final report
df = pd.read_excel(os.path.join(OUTPUT_DIR, "final_report.xlsx"))

# Top 10 students
top10 = df.head(10)

# Save file
top10.to_excel(os.path.join(OUTPUT_DIR, "top10_students.xlsx"), index=False)

print("top10_students.xlsx created successfully")
print(top10[["Name", "Total", "Percentage", "Rank", "Grade"]])