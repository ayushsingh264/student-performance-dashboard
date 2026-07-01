import pandas as pd
import smtplib
import os
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ==========================
# PATHS
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
PDF_DIR = os.path.join(OUTPUT_DIR, "grade_cards")

# ==========================
# READ REPORT
# ==========================
df = pd.read_excel(
    os.path.join(OUTPUT_DIR, "final_report.xlsx")
)

# Remove duplicate emails
df["Email"] = df["Email"].astype(str).str.strip().str.lower()
df = df.drop_duplicates(subset=["Email"])

# ==========================
# GMAIL DETAILS
# ==========================
sender_email = "7706rs7706@gmail.com"
app_password = "gion rnlk eeds jzzi"

# ==========================
# LOGIN
# ==========================
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

success_count = 0
failed_count = 0
skipped_count = 0

print("=" * 60)
print("EMAIL SENDING STARTED")
print("=" * 60)

for _, row in df.iterrows():

    student_name = str(row["Name"]).strip()
    receiver_email = str(row["Email"]).strip().lower()

    # Skip invalid email
    if (
        receiver_email == ""
        or receiver_email == "0"
        or "@gmail;.com" in receiver_email
        or "@" not in receiver_email
    ):
        skipped_count += 1
        print(f"SKIPPED -> {student_name} : {receiver_email}")
        continue

    print(f"\nSending -> {student_name}")
    print(f"Email    -> {receiver_email}")

    pdf_file = os.path.join(
        PDF_DIR,
        f"{student_name}.pdf"
    )

    msg = MIMEMultipart()

    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Student Performance Report"

    body = f"""
Dear {student_name},

Your Student Performance Report is attached.

----------------------------------------

Total Marks : {row['Total']}
Percentage  : {row['Percentage']} %
Grade       : {row['Grade']}
Rank        : {row['Rank']}

----------------------------------------

Regards,

Ayush Singh
Project Coordinator
Lloyd Institute of Engineering & Technology
"""

    msg.attach(MIMEText(body, "plain"))

    # Attach PDF
    if os.path.exists(pdf_file):

        with open(pdf_file, "rb") as attachment:

            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{os.path.basename(pdf_file)}"'
            )

            msg.attach(part)

    else:
        print("PDF NOT FOUND")
        failed_count += 1
        continue

    try:

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        success_count += 1

        print("SUCCESS")

        # Gmail rate limit se bachne ke liye
        time.sleep(2)

    except Exception as e:

        failed_count += 1

        print("FAILED")
        print(e)

server.quit()

print("\n")
print("=" * 60)
print("EMAIL SUMMARY")
print("=" * 60)

print(f"Total Students : {len(df)}")
print(f"Success        : {success_count}")
print(f"Failed         : {failed_count}")
print(f"Skipped        : {skipped_count}")

print("=" * 60)
print("PROCESS COMPLETED")
print("=" * 60)