import pandas as pd

# Read files
quiz1 = pd.read_csv("data/quiz1.csv")
quiz2 = pd.read_csv("data/quiz2.csv")

# Rename marks column
quiz1.rename(columns={'Marks':'Quiz1'}, inplace=True)
quiz2.rename(columns={'Marks':'Quiz2'}, inplace=True)

# Merge records
df = pd.merge(quiz1, quiz2, on="Email")

# Total marks
df['Total'] = df['Quiz1'] + df['Quiz2']

# Percentage
df['Percentage'] = (df['Total']/40)*100

# Rank
df['Rank'] = df['Total'].rank(ascending=False)

# Grade
def grade(p):
    if p >= 90:
        return 'A'
    elif p >= 75:
        return 'B'
    elif p >= 60:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Percentage'].apply(grade)

# Save file
df.to_excel("output/final_result.xlsx", index=False)

print(df)