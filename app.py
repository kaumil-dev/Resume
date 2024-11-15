import streamlit as st

# Page configuration
st.set_page_config(page_title="Kaumil Mistry - Resume", layout="wide")

# Header section
st.title("Kaumil Mistry")
st.subheader("Aspiring Data Scientist")
st.markdown("""
📧 [Email](mailto:kaumil.mg@gmail.com) | 📞 +91 8758322166 | 📍 Ahmedabad  
[GitHub](https://github.com/kaumil-dev) | [LinkedIn](https://www.linkedin.com/in/kaumil-mistry/) | [Portfolio](https://linktr.ee/Kaumilmg)
""")

# Summary section
st.write("---")
st.header("Professional Summary")
st.write("""
Ambitious and detail-oriented Data Scientist with a robust academic background in Computer Science and Data Science. Proficient in machine learning, data analytics, and cloud data engineering. Adept at crafting data-driven solutions and delivering actionable insights to improve business strategies. Skilled in Python, SQL, Power BI, and Snowflake, with a proven track record of developing impactful machine learning projects.
""")

# Key skills section
st.write("---")
st.header("Key Skills")
skills = [
    "Programming & Tools: Python (pandas, scikit-learn, matplotlib, plotly), SQL, Power BI",
    "Cloud Platforms: AWS (EC2, S3, Glue), Snowflake",
    "Machine Learning: EDA, feature engineering, classification algorithms",
    "Data Visualization: Dashboards, interactive reports, trend analysis",
]
for skill in skills:
    st.markdown(f"- {skill}")

# Professional experience
st.write("---")
st.header("Professional Experience")
st.subheader("Data Scientist Intern")
st.write("**Let's Enkindle** (Ahmedabad) | 05/2024 – Present")
st.markdown("""
- Analyzed and visualized complex datasets using SQL, Python, and Power BI.
- Developed interactive dashboards to present key performance metrics to stakeholders.
- Streamlined data pipelines and enhanced data accessibility through Snowflake cloud solutions.
""")

# Education section
st.write("---")
st.header("Education")
st.subheader("MSc Data Science")
st.write("**Symbiosis Skills and Professional University** (Pune) | 09/2022 – 05/2024")
st.write("Achieved a CGPA of 7.9, mastering data science concepts and tools to tackle real-world challenges.")

st.subheader("BTech in Computer Science and Engineering (CSE)")
st.write("**Indus University** (Ahmedabad) | 09/2018 – 05/2022")
st.write("Graduated with a CGPA of 7.5, building a strong foundation in programming and software development.")

# Projects section
st.write("---")
st.header("Projects")
st.subheader("Forest Fire Detection Using Machine Learning")
st.markdown("""
- Designed an ML pipeline for forest fire classification using Python and scikit-learn.  
- Deployed the solution using Flask and AWS services (EC2, S3).  
- **Key skills**: EDA, feature engineering, classification models, and cloud deployment.
""")

st.subheader("Data Visualization and Analysis")
st.markdown("""
- Conducted in-depth data analysis using Power BI, SQL, and Python.  
- Worked with diverse datasets (CSV, JSON, Excel) and applied visualization libraries like matplotlib and seaborn.  
- Delivered actionable insights through interactive dashboards and detailed reports.
""")

# Certifications section
st.write("---")
st.header("Certifications")
certifications = {
    "Data Science Master": "https://pwskills.com/learn/certificate/d334f700-6492-43ae-8a61-7c255e8fb3d4",
    "Build a Data Science Web App with Streamlit and Python": "https://lnkd.in/dZue93N4",
    "Data Analytics Part 2: Extending and Applying Core Knowledge": "https://www.coursera.org/account/accomplishments/certificate/PAS6RXGC4FDD",
}
for cert, link in certifications.items():
    st.markdown(f"- [{cert}]({link})")

# Additional Information
st.write("---")
st.header("Additional Information")
st.markdown("""
- **Portfolio**: [linktr.ee/Kaumilmg](https://linktr.ee/Kaumilmg)  
- **Languages**: English, Hindi, Gujarati
""")
