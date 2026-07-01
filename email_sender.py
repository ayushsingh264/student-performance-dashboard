import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Read Final Report
df = pd.read_excel(os.path.join(OUTPUT_DIR, "final_report.xlsx"))

# Your Gmail
sender_email = "7706rs7706@gmail.com"

# App Password
password = "gion rnlk eeds jzzi"

# SMTP Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

# Send mail to each student
for index, row in df.iterrows():

    receiver_email = str(row["Email"])
    student_name = str(row["Name"])
    total = row["Total"]
    percentage = row["Percentage"]
    grade = row["Grade"]

    subject = "Quiz Performance Report"
    body = f"""
Dear {student_name},
Your Performance Report-

Total Marks : {total}
Percentage : {percentage}%
Grade : {grade}

Congratulations!

Regards
Ayush Singh
"""

    msg = MIMEMultipart()

    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Mail sent to", student_name)

    except Exception as e:
        print("Failed:", student_name, e)

server.quit()

print("All mails sent successfully")