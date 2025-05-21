import streamlit as st
from datetime import date

st.set_page_config(page_title="CV Generator", layout="centered")

st.title("CV Generator")

st.sidebar.header("Personal Info")
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email")
phone = st.sidebar.text_input("Phone Number")
linkedin = st.sidebar.text_input("LinkedIn")
github = st.sidebar.text_input("GitHub")
dob = st.sidebar.date_input("Date of Birth", date(2000, 1, 1))

st.sidebar.header("Education")
edu_school = st.sidebar.text_input("School/University")
edu_degree = st.sidebar.text_input("Degree")
edu_year = st.sidebar.text_input("Year of Graduation")

st.sidebar.header("Experience")
job_title = st.sidebar.text_input("Job Title")
company
