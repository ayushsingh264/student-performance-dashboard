import pandas as pd
import matplotlib.pyplot as plt
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Read final report
df = pd.read_excel(os.path.join(OUTPUT_DIR, "final_report.xlsx"))

# -------------------------
# Grade Distribution Chart
# -------------------------
plt.figure(figsize=(8,5))

df["Grade"].value_counts().plot(kind="bar")

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "grade_distribution.png"))

plt.show()


# -------------------------
# Top 10 Students Chart
# -------------------------
top10 = df.sort_values("Rank").head(10)

plt.figure(figsize=(10,5))

plt.bar(top10["Name"], top10["Total"])

plt.xticks(rotation=45)

plt.title("Top 10 Students")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR, "top10_students.png"))

plt.show()

print("Charts created successfully")