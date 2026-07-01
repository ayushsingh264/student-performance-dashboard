import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Read performance file
df = pd.read_excel(
    os.path.join(
        OUTPUT_DIR,
        "performance.xlsx"
    )
)

# Rank
df["Rank"] = (
    df["Total"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)

# Percentile
df["Percentile"] = round(
    df["Total"].rank(pct=True) * 100,
    2
)

# Grade Function
def grade(p):

    if p >= 90:
        return "A+"

    elif p >= 80:
        return "A"

    elif p >= 70:
        return "B"

    elif p >= 60:
        return "C"

    elif p >= 50:
        return "D"

    else:
        return "F"


# Apply Grades
df["Grade"] = df["Percentage"].apply(grade)

# Sort by Rank
df = df.sort_values(
    by=["Rank", "Name"]
)

# Save Final Report
df.to_excel(
    os.path.join(
        OUTPUT_DIR,
        "final_report.xlsx"
    ),
    index=False
)

print("final_report.xlsx created successfully")
print("\nTop 5 Students:")
print(
    df[
        [
            "Name",
            "Total",
            "Percentage",
            "Rank",
            "Grade"
        ]
    ].head()
)






# import pandas as pd

# # Read file
# df = pd.read_excel("output/performance.xlsx")

# # Rank
# df["Rank"] = df["Total"].rank(ascending=False, method="dense")

# # Percentile
# df["Percentile"] = round(df["Total"].rank(pct=True)*100,2)

# # Grade Function
# def grade(p):

#     if p >= 90:
#         return "A+"

#     elif p >= 80:
#         return "A"

#     elif p >= 70:
#         return "B"

#     elif p >= 60:
#         return "C"

#     elif p >= 50:
#         return "D"

#     else:
#         return "F"


# df["Grade"] = df["Percentage"].apply(grade)

# # Sort according to rank
# df = df.sort_values("Rank")

# # Save
# df.to_excel("output/final_report.xlsx", index=False)

# print("Final Report Generated Successfully!")