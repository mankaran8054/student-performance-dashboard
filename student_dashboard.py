import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Student Dashboard",
    page_icon="Student",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("students.csv")

# -----------------------------
# Title
# -----------------------------

st.title("Student Dashboard")

st.write("Student performance analysis using Pandas and Streamlit")

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")

# Branch filter

branches = st.sidebar.multiselect(
    "Select Branch",
    options=df["branch"].unique(),
    default=df["branch"].unique()
)

# City filter

cities = st.sidebar.multiselect(
    "Select City",
    options=df["city"].unique(),
    default=df["city"].unique()
)

# -----------------------------
# Apply Filters
# -----------------------------

filtered_df = df[
    (df["branch"].isin(branches)) &
    (df["city"].isin(cities))
]

# -----------------------------
# Dashboard Metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Students",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Marks",
        round(filtered_df["marks"].mean(), 2)
    )

with col3:
    st.metric(
        "Highest Marks",
        filtered_df["marks"].max()
    )

with col4:
    st.metric(
        "BCA Students",
        len(filtered_df[filtered_df["branch"] == "BCA"])
    )

# -----------------------------
# Student Data
# -----------------------------

st.subheader("Student Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# -----------------------------
# Charts
# -----------------------------

col1, col2 = st.columns(2)

# -----------------------------
# Marks by Student
# -----------------------------

with col1:

    st.subheader("Student Marks")

    chart_data = filtered_df.set_index("name")["marks"]

    st.bar_chart(chart_data)

# -----------------------------
# Students by Branch
# -----------------------------

with col2:

    st.subheader("Students by Branch")

    branch_count = filtered_df["branch"].value_counts()

    st.bar_chart(branch_count)

# -----------------------------
# Average Marks by Branch
# -----------------------------

st.subheader("Average Marks by Branch")

branch_average = (
    filtered_df
    .groupby("branch")["marks"]
    .mean()
)

st.bar_chart(branch_average)

# -----------------------------
# Average Marks by City
# -----------------------------

st.subheader("Average Marks by City")

city_average = (
    filtered_df
    .groupby("city")["marks"]
    .mean()
)

st.bar_chart(city_average)