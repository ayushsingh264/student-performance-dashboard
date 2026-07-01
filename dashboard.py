# llm and confusion  matrix



import streamlit as st
import pandas as pd
import os
import subprocess
import plotly.express as px
import matplotlib.pyplot as plt
# from PIL import Image

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

ASSET_DIR = os.path.join(BASE_DIR, "assets")

REPORT_FILE = os.path.join(
    OUTPUT_DIR,
    "final_report.xlsx"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main{
    background:#F4F8FB;
}

.title{
    font-size:40px;
    color:#003366;
    text-align:center;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.metric-box{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,.15);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD DATA
# ==========================================

# if not os.path.exists(REPORT_FILE):

#     st.error("final_report.xlsx not found.")
#     st.stop()

if not os.path.exists(REPORT_FILE):

    st.error("""
final_report.xlsx not found.

Please upload the generated report into

output/final_report.xlsx
""")

    st.stop()

df = pd.read_excel(REPORT_FILE)

# ==========================================
# HEADER
# ==========================================

col1, col2 = st.columns([1,5])

logo_path = os.path.join(
    ASSET_DIR,
    "logo.png"
)

with col1:

    if os.path.exists(logo_path):

        st.image(
            logo_path,
            width=120
        )

with col2:

    st.markdown(
        "<div class='title'>LLOYD INSTITUTE OF ENGINEERING & TECHNOLOGY</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Student Performance Dashboard</div>",
        unsafe_allow_html=True
    )

st.divider()



# ==========================================
# SIDEBAR
# ==========================================

# st.sidebar.image(logo_path, width=120)

if os.path.exists(logo_path):
    st.sidebar.image(logo_path)

st.sidebar.title("🎓 Student Dashboard")

st.sidebar.markdown("---")

st.sidebar.header("⚙️ Project Controls")

# if st.sidebar.button("📂 Merge Quiz Files"):
#     subprocess.run(["python", "merge_files.py"])
#     st.sidebar.success("Merge Completed")

# if st.sidebar.button("📊 Generate Performance"):
#     subprocess.run(["python", "performance.py"])
#     st.sidebar.success("Performance Generated")

# if st.sidebar.button("🏆 Rank & Grade"):
#     subprocess.run(["python", "rank_grade.py"])
#     st.sidebar.success("Ranking Completed")

# if st.sidebar.button("📄 Generate Grade Cards"):
#     subprocess.run(["python", "pdf_generator.py"])
#     st.sidebar.success("PDF Generated")

# if st.sidebar.button("📧 Send Emails"):
#     subprocess.run(["python", "email_sender_pdf.py"])
#     st.sidebar.success("Emails Sent")

st.sidebar.header("⚙️ Project")

st.sidebar.success("Dashboard Running Successfully")

st.sidebar.info("""
This is the deployed version.

Data is loaded from
output/final_report.xlsx
""")

st.sidebar.markdown("---")

# ==========================================
# DASHBOARD METRICS
# ==========================================

total_students = len(df)

highest_marks = int(df["Total"].max())

lowest_marks = int(df["Total"].min())

average_marks = round(df["Total"].mean(),2)

highest_percentage = round(df["Percentage"].max(),2)

average_percentage = round(df["Percentage"].mean(),2)

pass_students = len(df[df["Percentage"] >= 40])

fail_students = len(df[df["Percentage"] < 40])

# ==========================================
# KPI CARDS
# ==========================================

st.subheader("📊 Dashboard Overview")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "👨‍🎓 Total Students",
    total_students
)

c2.metric(
    "🏆 Highest Marks",
    highest_marks
)

c3.metric(
    "📉 Lowest Marks",
    lowest_marks
)

c4.metric(
    "📈 Avg Percentage",
    f"{average_percentage}%"
)

st.write("")

c5,c6,c7,c8 = st.columns(4)

c5.metric(
    "✅ Pass",
    pass_students
)

c6.metric(
    "❌ Fail",
    fail_students
)

c7.metric(
    "🥇 Highest %",
    f"{highest_percentage}%"
)

c8.metric(
    "📚 Average Marks",
    average_marks
)

st.divider()

# ==========================================
# TOPPER CARD
# ==========================================

topper = df.sort_values(
    "Rank"
).iloc[0]

st.subheader("🏆 Class Topper")

left,right = st.columns([1,3])

with left:

    st.image(
        logo_path,
        width=120
    )

with right:

    st.success(f"""
### 👨‍🎓 {topper['Name']}

**Email :** {topper['Email']}

**Total Marks :** {topper['Total']}

**Percentage :** {topper['Percentage']} %

**Rank :** {topper['Rank']}

**Grade :** {topper['Grade']}
""")

st.divider()



# ==========================================
# STUDENT SEARCH & FILTER
# ==========================================

st.subheader("🔍 Student Search")

col1, col2 = st.columns(2)

with col1:
    search_name = st.text_input(
        "Search by Student Name"
    )

with col2:
    grade_filter = st.selectbox(
        "Filter By Grade",
        ["All"] + sorted(df["Grade"].astype(str).unique().tolist())
    )

filtered_df = df.copy()

if search_name:

    filtered_df = filtered_df[
        filtered_df["Name"]
        .astype(str)
        .str.contains(
            search_name,
            case=False,
            na=False
        )
    ]

if grade_filter != "All":

    filtered_df = filtered_df[
        filtered_df["Grade"] == grade_filter
    ]

st.success(f"Students Found : {len(filtered_df)}")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)

st.divider()

# ==========================================
# TOP 10 STUDENTS
# ==========================================

st.subheader("🏆 Top 10 Students")

top10 = (
    df.sort_values("Rank")
      .head(10)
)

st.dataframe(
    top10[
        [
            "Rank",
            "Name",
            "Total",
            "Percentage",
            "Grade"
        ]
    ],
    width="stretch",
    hide_index=True
)

st.divider()

# ==========================================
# WEAK STUDENTS
# ==========================================

st.subheader("⚠️ Students Needing Attention")

weak_students = df[
    df["Percentage"] < 40
]

if weak_students.empty:

    st.success(
        "🎉 No weak students found."
    )

else:

    st.dataframe(
        weak_students[
            [
                "Name",
                "Total",
                "Percentage",
                "Grade"
            ]
        ],
        width="stretch",
        hide_index=True
    )

st.divider()

# ==========================================
# CLASS STATISTICS
# ==========================================

st.subheader("📊 Class Statistics")

left, right = st.columns(2)

with left:

    st.info(f"""
### 📚 Overall Statistics

👨‍🎓 Total Students : {len(df)}

🏆 Highest Marks : {df['Total'].max()}

📉 Lowest Marks : {df['Total'].min()}

📈 Average Marks : {round(df['Total'].mean(),2)}

""")

with right:

    st.info(f"""
### 📈 Performance

Highest Percentage : {df['Percentage'].max()} %

Average Percentage : {round(df['Percentage'].mean(),2)} %

Pass Students : {pass_students}

Fail Students : {fail_students}

""")

st.divider()

# ==========================================
# STUDENT RANK LIST
# ==========================================

st.subheader("🥇 Complete Rank List")

rank_df = df.sort_values("Rank")

st.dataframe(

    rank_df[
        [
            "Rank",
            "Name",
            "Total",
            "Percentage",
            "Grade"
        ]
    ],

    width="stretch",

    hide_index=True

)

st.divider()

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.subheader("📥 Download Final Report")

with open(REPORT_FILE, "rb") as file:

    st.download_button(

        label="📄 Download Excel Report",

        data=file,

        file_name="final_report.xlsx",

        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

st.divider()



# ==========================================
# CHARTS & ANALYTICS
# ==========================================

st.header("📊 Visual Analytics Dashboard")

# ==========================================
# PASS VS FAIL PIE CHART
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥧 Pass vs Fail")

    pass_fail_df = pd.DataFrame({
        "Category": ["Pass", "Fail"],
        "Students": [pass_students, fail_students]
    })

    fig = px.pie(
        pass_fail_df,
        names="Category",
        values="Students",
        hole=0.45,
        title="Pass vs Fail Analysis"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(fig, width="stretch")

# ==========================================
# GRADE DISTRIBUTION
# ==========================================

with col2:

    st.subheader("🎓 Grade Distribution")

    grade_df = (
        df["Grade"]
        .value_counts()
        .reset_index()
    )

    grade_df.columns = ["Grade", "Students"]

    fig = px.bar(
        grade_df,
        x="Grade",
        y="Students",
        text="Students",
        color="Grade",
        title="Grade Distribution"
    )

    st.plotly_chart(fig, width="stretch")

st.divider()

# ==========================================
# TOP 10 STUDENTS
# ==========================================

st.subheader("🏆 Top 10 Students")

top10 = (
    df.sort_values("Rank")
    .head(10)
)

fig = px.bar(
    top10,
    x="Name",
    y="Total",
    color="Grade",
    text="Total",
    title="Top 10 Students"
)

fig.update_layout(
    xaxis_title="Students",
    yaxis_title="Marks"
)

st.plotly_chart(fig, width="stretch")

st.divider()

# ==========================================
# QUIZ ANALYSIS
# ==========================================

st.subheader("📈 Quiz Wise Performance")

quiz_columns = [
    col for col in df.columns
    if col.startswith("Quiz")
]

quiz_data = []

for col in quiz_columns:

    quiz_data.append({

        "Quiz": col,

        "Average Marks": round(
            df[col].mean(),
            2
        )

    })

quiz_df = pd.DataFrame(quiz_data)

if len(quiz_df) > 0:

    fig = px.line(

        quiz_df,

        x="Quiz",

        y="Average Marks",

        markers=True,

        title="Average Marks in Every Quiz"

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

else:

    st.warning(
        "Quiz columns not found."
    )

st.divider()

# ==========================================
# MARKS DISTRIBUTION
# ==========================================

st.subheader("📉 Total Marks Distribution")

fig = px.histogram(

    df,

    x="Total",

    nbins=20,

    title="Marks Distribution"

)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# ==========================================
# PERCENTAGE DISTRIBUTION
# ==========================================

st.subheader("📊 Percentage Distribution")

fig = px.histogram(

    df,

    x="Percentage",

    nbins=20,

    title="Percentage Distribution"

)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# ==========================================
# RANK DISTRIBUTION
# ==========================================

st.subheader("🥇 Rank Distribution")

fig = px.scatter(

    df,

    x="Rank",

    y="Percentage",

    color="Grade",

    hover_name="Name",

    title="Rank vs Percentage"

)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# ==========================================
# TOPPER COMPARISON
# ==========================================

st.subheader("🏅 Top 5 Students Comparison")

top5 = (
    df.sort_values("Rank")
    .head(5)
)

fig = px.bar(

    top5,

    x="Name",

    y="Percentage",

    color="Grade",

    text="Percentage",

    title="Top 5 Percentage"

)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# ==========================================
# GRADE PIE CHART
# ==========================================

st.subheader("🥧 Grade Percentage")

grade_pie = (
    df["Grade"]
    .value_counts()
    .reset_index()
)

grade_pie.columns = [
    "Grade",
    "Students"
]

fig = px.pie(

    grade_pie,

    names="Grade",

    values="Students",

    hole=.45,

    title="Grade Share"

)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# ==========================================
# PERFORMANCE SUMMARY
# ==========================================

st.subheader("📌 Dashboard Summary")

st.success(f"""
🎓 Total Students : {len(df)}

🏆 Topper : {topper['Name']}

🥇 Highest Percentage : {highest_percentage} %

📈 Average Percentage : {average_percentage} %

✅ Pass Students : {pass_students}

❌ Fail Students : {fail_students}
""")




# =====================================================
# PART 5 : DOWNLOAD CENTER + SIGNATURES + FOOTER
# =====================================================

st.header("📄 Grade Card Download Center")

pdf_dir = os.path.join(OUTPUT_DIR, "grade_cards")

# if os.path.exists(pdf_dir):

    # pdf_files = sorted(
    #     [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    # )

if os.path.exists(pdf_dir):

    pdf_files = sorted(
        [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
    )


    if len(pdf_files) > 0:

        selected_pdf = st.selectbox(
            "Select Student Grade Card",
            pdf_files
        )

        pdf_path = os.path.join(
            pdf_dir,
            selected_pdf
        )

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="📥 Download Selected Grade Card",
                data=pdf,
                file_name=selected_pdf,
                mime="application/pdf",
                width="stretch"
            )

        st.success(f"Total Grade Cards : {len(pdf_files)}")

    else:

        st.warning("No Grade Cards Found.")

else:

    pdf_files = []



# else:

#     st.error("grade_cards folder not found.")

# st.divider()

# =====================================================
# RUN COMPLETE PROJECT
# =====================================================

# st.header("🚀 Project Automation")

# if st.button(
#     "▶ Run Complete Project",
#     width="stretch"
# ):

#     progress = st.progress(0)

#     tasks = [

#         ("Merge Quiz Files", "merge_files.py"),

#         ("Generate Performance", "performance.py"),

#         ("Generate Rank", "rank_grade.py"),

#         ("Generate Grade Cards", "pdf_generator.py"),

#         ("Generate Charts", "charts.py")

#     ]

#     total = len(tasks)

#     for i, (name, script) in enumerate(tasks):

#         st.write(f"Running : {name}")

#         subprocess.run(
#             ["python", script]
#         )

#         progress.progress(
#             int(((i + 1) / total) * 100)
#         )

#     st.success("🎉 Project Completed Successfully!")

# st.divider()



st.header("🚀 Project Status")

st.success("All reports are already generated.")

st.info("This cloud version is only for viewing reports.")




# =====================================================
# EMAIL CENTER
# =====================================================

# st.header("📧 Email Center")

# if st.button(
#     "📤 Send Grade Cards to Students",
#     width="stretch"
# ):

#     subprocess.run(
#         ["python", "email_sender_pdf.py"]
#     )

#     st.success(
#         "Emails Sent Successfully."
#     )

# st.divider()


st.header("📧 Email Center")

st.warning("""
Email sending is available only in the Local Desktop Version.

Streamlit Cloud does not support automated SMTP execution.
""")


# =====================================================
# PROJECT INFORMATION
# =====================================================

st.header("ℹ Project Information")

info1, info2 = st.columns(2)

with info1:

    st.info(f"""

### 🎓 Dashboard Information

**College**

Lloyd Institute of Engineering & Technology

**Department**

Data Science

**Language**

Python

**Framework**

Streamlit

**Charts**

Plotly

""")

with info2:

    st.info(f"""

### 📊 Database

Students : {len(df)}

Grade Cards : {len(os.listdir(pdf_dir)) if os.path.exists(pdf_dir) else 0}

Topper :

{topper['Name']}

Average %

{average_percentage}

""")

st.divider()

# =====================================================
# FACULTY & HOD SIGNATURE
# =====================================================

st.header("🖋 Approval")

faculty_col, hod_col = st.columns(2)

faculty_sign = os.path.join(
    ASSET_DIR,
    "faculty_sign.png"
)

hod_sign = os.path.join(
    ASSET_DIR,
    "hod_sign.png"
)

with faculty_col:

    if os.path.exists(faculty_sign):

        st.image(
            faculty_sign,
            width=180
        )

    st.markdown("### Faculty Signature")

    st.write("Mr. Ayush Singh")

    st.write("Project Coordinator")

with hod_col:

    if os.path.exists(hod_sign):

        st.image(
            hod_sign,
            width=180
        )

    st.markdown("### HOD Signature")

    st.write("Head of Department")

    st.write("Data Science Department")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
---
<center>

### 🎓 Lloyd Institute of Engineering & Technology

Student Performance Management System

Developed Using

🐍 Python | 📊 Streamlit | 📈 Plotly | 📄 ReportLab | 🐼 Pandas

© 2026 All Rights Reserved

</center>
""",
unsafe_allow_html=True
)

# =====================================================
# END
# =====================================================




# run krane ke liye terminal me ye command use karein

# streamlit run dashboard.py


#Local URL: http://localhost:8501
#Network URL: http://10.39.57.136:8501