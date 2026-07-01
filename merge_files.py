# import pandas as pd
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Read files
# quiz1 = pd.read_csv(os.path.join(DATA_DIR, "Quiz1_15_6_26.csv"))
# quiz2 = pd.read_csv(os.path.join(DATA_DIR, "Quiz 2_16_6_26.csv"))
# quiz3 = pd.read_csv(os.path.join(DATA_DIR, "Quiz 3_17_6_26.csv"))

# # Keep required columns
# quiz1 = quiz1[["Email", "Name", "Total score"]]
# quiz2 = quiz2[["Email", "Name", "Total score"]]
# quiz3 = quiz3[["Email", "Name", "Total score"]]

# # Rename columns
# quiz1.rename(columns={"Total score": "Quiz1"}, inplace=True)
# quiz2.rename(columns={"Total score": "Quiz2"}, inplace=True)
# quiz3.rename(columns={"Total score": "Quiz3"}, inplace=True)

# # Extract only obtained marks
# quiz1["Quiz1"] = quiz1["Quiz1"].astype(str).str.split("/").str[0].astype(float)
# quiz2["Quiz2"] = quiz2["Quiz2"].astype(str).str.split("/").str[0].astype(float)
# quiz3["Quiz3"] = quiz3["Quiz3"].astype(str).str.split("/").str[0].astype(float)

# # Merge
# df = quiz1.merge(quiz2, on="Email", how="outer")
# df = df.merge(quiz3, on="Email", how="outer")

# # Fill missing values
# df.fillna(0, inplace=True)

# # Save file
# df.to_excel(os.path.join(OUTPUT_DIR, "master_performance.xlsx"), index=False)

# print("✅ master_performance.xlsx created successfully")
# print(df.head())












import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

df = pd.read_excel(
    os.path.join(
        OUTPUT_DIR,
        "master_performance.xlsx"
    )
)

obtained_cols = [
    col for col in df.columns
    if col.endswith("_Obtained")
]

max_cols = [
    col for col in df.columns
    if col.endswith("_Max")
]

print("Obtained Columns:", obtained_cols)
print("Max Columns:", max_cols)

# Total Obtained Marks
df["Total"] = df[obtained_cols].sum(axis=1)

# Total Maximum Marks
df["Max_Total"] = df[max_cols].sum(axis=1)

# Percentage
df["Percentage"] = round(
    (df["Total"] / df["Max_Total"]) * 100,
    2
)

# Average
df["Average"] = round(
    df[obtained_cols].mean(axis=1),
    2
)

df.to_excel(
    os.path.join(
        OUTPUT_DIR,
        "performance.xlsx"
    ),
    index=False
)

print("performance.xlsx created successfully")
print(df.head())