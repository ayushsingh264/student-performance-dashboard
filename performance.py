# import pandas as pd
# import os


# # Base directory
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# # Read merged file
# df = pd.read_excel(os.path.join(OUTPUT_DIR, "master_performance.xlsx"))

# # Total Marks
# df["Total"] = df["Quiz1"] + df["Quiz2"] + df["Quiz3"]

# # Percentage
# max_marks = 10 + 15 + 25  # Total = 50

# df["Percentage"] = round((df["Total"] / max_marks) * 100, 2)

# # Average Marks
# df["Average"] = round(df["Total"] / 3, 2)

# # Save
# df.to_excel(os.path.join(OUTPUT_DIR, "performance.xlsx"), index=False)

# print("✅ performance.xlsx created successfully")
# print(df.head())











import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Read merged file
df = pd.read_excel(
    os.path.join(
        OUTPUT_DIR,
        "master_performance.xlsx"
    )
)

# Detect Quiz Columns Automatically
quiz_columns = [
    col for col in df.columns
    if col.startswith("Quiz")
]

print("Detected Quiz Columns:")
print(quiz_columns)

# Total Marks
df["Total"] = df[quiz_columns].sum(axis=1)

# Average Marks
df["Average"] = round(
    df["Total"] / len(quiz_columns),
    2
)

# Percentage
# IMPORTANT:
# Change this according to your quiz pattern

max_marks_per_quiz = 25

max_marks = (
    len(quiz_columns)
    * max_marks_per_quiz
)

df["Percentage"] = round(
    (df["Total"] / max_marks) * 100,
    2
)

# Save
df.to_excel(
    os.path.join(
        OUTPUT_DIR,
        "performance.xlsx"
    ),
    index=False
)

print("\nperformance.xlsx created successfully")
print("\nTotal Students:", len(df))
print(df.head())


