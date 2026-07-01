# import pandas as pd
# from reportlab.platypus import Image
# import os

# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     Table,
#     TableStyle
# )

# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.enums import TA_CENTER

# # Paths
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# PDF_DIR = os.path.join(OUTPUT_DIR, "grade_cards")

# os.makedirs(PDF_DIR, exist_ok=True)

# # Read Report
# df = pd.read_excel(
#     os.path.join(OUTPUT_DIR, "final_report.xlsx")
# )

# styles = getSampleStyleSheet()

# title_style = styles["Title"]
# title_style.alignment = TA_CENTER

# for _, row in df.iterrows():

#     student_name = str(row["Name"])

#     pdf_file = os.path.join(
#         PDF_DIR,
#         f"{student_name}.pdf"
#     )

#     doc = SimpleDocTemplate(pdf_file)

#     content = []



# logo_path = os.path.join(
#     BASE_DIR,
#     "assets",
#     "logo.png"
# )

# if os.path.exists(logo_path):

#     logo = Image(
#         logo_path,
#         width=80,
#         height=80
#     )

#     content.append(logo)




#     # College Name
#     content.append(
#         Paragraph(
#             "LLOYD INSTITUTE OF ENGINEERING & TECHNOLOGY",
#             title_style
#         )
#     )

#     content.append(
#         Paragraph(
#             "Student Grade Card",
#             styles["Heading2"]
#         )
#     )

#     content.append(Spacer(1, 20))

#     # Student Info Table
#     student_data = [
#         ["Name", row["Name"]],
#         ["Email", row["Email"]],
#         ["Rank", row["Rank"]],
#         ["Grade", row["Grade"]]
#     ]

#     student_table = Table(student_data, colWidths=[120, 300])

#     student_table.setStyle(
#         TableStyle([
#             ("GRID", (0,0), (-1,-1), 1, colors.black),
#             ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),
#             ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold")
#         ])
#     )

#     content.append(student_table)

#     content.append(Spacer(1, 20))

#     # Marks Table
# marks_data = [
#     ["Quiz", "Marks"],

#     ["Quiz1", row["Quiz1"]],
#     ["Quiz2", row["Quiz2"]],
#     ["Quiz3", row["Quiz3"]],

#     ["Total", row["Total"]],
#     ["Percentage", f"{row['Percentage']} %"],
#     ["Grade", row["Grade"]]
# ]
# marks_table = Table(marks_data, colWidths=[120, 300])
# marks_table.setStyle(
#     TableStyle([
#         ("GRID", (0,0), (-1,-1), 1, colors.black),
#         ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),
#         ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold")
#     ])
# )
# content.append(marks_table)


# content.append(Spacer(1, 40))

#     # Signature Area
# sign_path = os.path.join(
#     BASE_DIR,
#     "assets",
#     "signature.png"
# )

# if os.path.exists(sign_path):

#     sign = Image(
#         sign_path,
#         width=120,
#         height=40
#     )

#     content.append(sign)

# content.append(
#     Paragraph(
#         "Ayush Singh",
#         styles["Normal"]
#     )
# )

# content.append(
#     Paragraph(
#         "Project Coordinator",
#         styles["Normal"]
#     )
# )
# content.append(Spacer(1, 20))

# content.append(
#         Paragraph(
#             "[College Seal / Stamp]",
#             styles["Normal"]
#         )
#     )

# doc.build(content)

# print("Grade Cards Generated Successfully")



























import os
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

# ==========================
# PATHS
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

PDF_DIR = os.path.join(
    OUTPUT_DIR,
    "grade_cards"
)

ASSET_DIR = os.path.join(
    BASE_DIR,
    "assets"
)

os.makedirs(PDF_DIR, exist_ok=True)

# ==========================
# READ FINAL REPORT
# ==========================

df = pd.read_excel(
    os.path.join(
        OUTPUT_DIR,
        "final_report.xlsx"
    )
)

print("Total Students:", len(df))
print(df[["Name", "Email"]].head())
print(df.tail())

# ==========================
# STYLES
# ==========================

styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.darkblue

heading_style = styles["Heading2"]
heading_style.alignment = TA_CENTER
heading_style.textColor = colors.darkred

normal_style = styles["BodyText"]

footer_style = styles["Italic"]
footer_style.alignment = TA_CENTER




# ==========================
# GENERATE PDF
# ==========================

for _, row in df.iterrows():

    student_name = str(row["Name"])

    pdf_file = os.path.join(
        PDF_DIR,
        f"{student_name}.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=25,
        leftMargin=25,
        topMargin=20,
        bottomMargin=20
    )

    content = []

    # ==========================
    # LOGO
    # ==========================

    logo_path = os.path.join(
        ASSET_DIR,
        "logo.png"
    )

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=70,
            height=70
        )

        logo.hAlign = "CENTER"

        content.append(logo)

    # ==========================
    # COLLEGE NAME
    # ==========================

    content.append(
        Paragraph(
            "LLOYD INSTITUTE OF ENGINEERING & TECHNOLOGY",
            title_style
        )
    )

    content.append(
        Paragraph(
            "STUDENT GRADE CARD",
            heading_style
        )
    )

    content.append(Spacer(1, 20))

    # ==========================
    # STUDENT INFORMATION
    # ==========================

    student_info = [

        ["Name", row["Name"]],

        ["Email", row["Email"]],

        ["Rank", row["Rank"]],

        ["Grade", row["Grade"]]

    ]

    student_table = Table(
        student_info,
        colWidths=[120, 320]
    )

    student_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#D9EAF7")),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("ALIGN",(0,0),(-1,-1),"LEFT")

        ])

    )

    content.append(student_table)

    content.append(Spacer(1,20))



        # ==========================
    # QUIZ MARKS TABLE
    # ==========================

    marks_data = [
        ["Quiz", "Marks"]
    ]

    # Automatically detect all quiz columns
    quiz_columns = [
        col for col in df.columns
        if col.endswith("_Obtained")
    ]

    # If old version (Quiz1, Quiz2...)
    if len(quiz_columns) == 0:

        quiz_columns = [
            col for col in df.columns
            if col.startswith("Quiz")
            and col not in [
                "Total",
                "Percentage",
                "Average",
                "Rank",
                "Percentile",
                "Grade"
            ]
        ]

    for col in quiz_columns:

        marks_data.append([
            col.replace("_Obtained",""),
            row[col]
        ])

    marks_data.append(["",""])
    marks_data.append(["Total", row["Total"]])
    marks_data.append(["Percentage", f"{row['Percentage']} %"])
    marks_data.append(["Grade", row["Grade"]])

    marks_table = Table(
        marks_data,
        colWidths=[170,170]
    )

    marks_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#4F81BD")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(0,-1),colors.HexColor("#D9EAF7")),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    content.append(marks_table)

    content.append(Spacer(1,25))

    # ==========================
    # PERFORMANCE MESSAGE
    # ==========================

    percentage = row["Percentage"]

    if percentage >= 90:
        performance = "Outstanding Performance"
    elif percentage >= 75:
        performance = "Excellent Performance"
    elif percentage >= 60:
        performance = "Very Good Performance"
    elif percentage >= 40:
        performance = "Good Performance"
    else:
        performance = "Needs Improvement"

    content.append(
        Paragraph(
            f"<b>Performance :</b> {performance}",
            normal_style
        )
    )

    content.append(Spacer(1,30))



        # ==========================
    # SIGNATURE
    # ==========================

    sign_path = os.path.join(
        ASSET_DIR,
        "signature.png"
    )

    if os.path.exists(sign_path):

        sign = Image(
            sign_path,
            width=120,
            height=45
        )

        sign.hAlign = "RIGHT"

        content.append(sign)

    content.append(
        Paragraph(
            "<b>Ayush Singh</b>",
            footer_style
        )
    )

    content.append(
        Paragraph(
            "Project Coordinator",
            footer_style
        )
    )

    content.append(
        Paragraph(
            "Lloyd Institute of Engineering & Technology",
            footer_style
        )
    )

    content.append(Spacer(1, 20))

    # ==========================
    # FOOTER
    # ==========================

    content.append(
        Paragraph(
            "<font color='grey'><i>"
            "This is a computer generated grade card. "
            "No signature is required if digitally verified."
            "</i></font>",
            footer_style
        )
    )

# ==========================
# BUILD PDF
# ==========================

print(f"Generating PDF : {student_name}")

doc.build(content)

print(f"Saved : {pdf_file}")


# ==========================
# FINISHED
# ==========================

print("=" * 50)
print("Grade Cards Generated Successfully")
print(f"Location : {PDF_DIR}")
print("=" * 50)

