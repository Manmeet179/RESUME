import streamlit as st


st.set_page_config(
    page_title="MEET MEWADA",
    # page_icon="C:/MY_PYTHON/MY_CODES/PYTHON/I_MANMEET__/IMG/letter-m.png",
    page_icon="IMG/letter-m.png",
    layout="centered",  # You can change layout to wide if needed
    initial_sidebar_state="expanded",  # Sidebar can be either "expanded" or "collapsed"
)

st.markdown(

    """
    <style>
        .container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .info {
            display: flex;
            align-items: center;
            margin: 10px;
            color: white;
        }
        h1, h2 {
            margin: 0 10px;
            text-align: center;
        }
    </style>
    <div class="container">
        <img src="https://img.icons8.com/clouds/100/resume.png" width="70" height="70"/>
        <h1>MY RESUME..</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")

st.markdown(
    """
    <div class="container">
        <h2>Meet Hareshbhai Mevada</h2>
        <img src="https://img.icons8.com/clouds/100/user-male-circle.png" width="70" height="70" alt="user-male-circle" style="margin-right: 10px;"/>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")

st.markdown(
    """
    <div style="display: flex; flex-direction: column; align-items: flex-start; margin: 10px;">
        <div class="info">
            <img src="https://img.icons8.com/fluency/48/new-post.png" width="28" height="28" alt="new-post" />
            <a href="mailto:mevadameet916@gmail.com">mevadameet916@gmail.com</a>
        </div>
        <div class="info">
            <img src="https://img.icons8.com/fluency/48/linkedin.png" width="28" height="28" alt="linkedin" />
            <a href="https://www.linkedin.com/in/meet-mevada-3627b42b1/">Meet Mevada</a>
        </div>
         <div class="info">
            <img src="https://img.icons8.com/color/48/web-design.png" width="28" height="28" alt="Web Design Icon" />
            <a target="_blank" href="https://manmeet179.streamlit.app/">Visit My Blog</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write('---')

# Career Objective
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/fluency/48/goal--v1.png" width="50" height="50" alt="goal--v1" />
        <h2>Career Objective</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
To work hard with full determination and dedication to achieve organizational as well as personal goals. 
I will always try to use my skills like honesty, devotion towards my job, punctuality, etc. 
I will discuss my ideology with my superiors.
""")
st.write("---")

# Project
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/color-glass/50/project-management.png" width="50" height="50" alt="project-management" />
        <h2>Project</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
- **Online News Portal**  
  [GitHub Project Link](https://github.com/Manmeet179/Online-News-Portal/tree/main)  
  Developed an online news portal utilizing HTML, CSS, BOOTSTRAP, PHP, and MySQLi, with the primary focus on informing the public.
""")
st.write("---")

# Experience
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/external-flaticons-flat-flat-icons/64/external-experience-mental-health-flaticons-flat-flat-icons.png" width="50" height="50" alt="experience" />
        <h2>Experience</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
**Company:** Great Ideas Tech, Palanpur  
**Position:** Data Science Intern  
**Duration:** June 2024 – Present  

- Cleaned and manipulated raw data to ensure accuracy and consistency.
- Worked on data preprocessing and pipeline improvements.
- Collaborated with cross-functional teams to deliver data-driven insights.
- Gained 3 months of hands-on experience in data analysis and data science techniques.
""")
st.write("---")

# Skills
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/bubbles/100/admin-settings-male.png" width="50" height="50" alt="skills" />
        <h2>Skills</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
- **Programming Languages:** Python
- **Frameworks & Libraries:** Django
- **Databases:** PostgreSQL, MySQL
- **Version Control:** GitHub
""")

st.markdown(
        """
        <div class="container">
            <img src="https://img.icons8.com/color/48/python--v1.png" width="40" height="40" alt="python" style="margin-right: 15px;" />
            <img src="https://img.icons8.com/color/48/postgreesql.png" width="40" height="40" alt="postgreSQL" style="margin-right: 15px;" />
            <img src="https://img.icons8.com/color/48/html-5--v1.png" width="40" height="40" alt="html5" style="margin-right: 15px;"/>
            <img src="https://img.icons8.com/color/48/css3.png" width="40" height="40" alt="css3"style="margin-right: 15px; "/>
            <img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/24/external-project-jupyter-a-nonprofit-organization-created-to-open-source-software-logo-color-tal-revivo.png" width="40" height="40" alt="jupyter" style="margin-right: 15px;"/>
            <img src="https://img.icons8.com/color/48/selenium-test-automation.png" width="40" height="40" alt="selenium" style="margin-right: 15px;"/>
            <img src="https://img.icons8.com/color/48/pandas.png" width="40" height="40" alt="pandas" style="margin-right: 15px;"/>
            <img src="https://img.icons8.com/color/48/mysql-logo.png" width="40" height="40" alt="mysql"style="margin-right: 15px;" />
            <img src="https://img.icons8.com/color/48/django.png" width="40" height="40" alt="django"style="margin-right: 15px;" />
        </div>
        """,
    unsafe_allow_html=True
)
st.write("---")

# Education
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/doodle/48/teaching.png" width="50" height="50" alt="education" />
        <h2>Education</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
- **Smt. B.K. Mehta I.T. Centre, Palanpur**  
  Bachelor of Computer Applications (BCA), 2024  
- **Smt. C.G. Mevada Higher Secondary School, Palanpur**  
  Higher Secondary Education (HSC), 2021  
- **Smt. C.H. Mevada Secondary School, Palanpur**  
  Secondary Education (SSC), 2019
""")
st.write("---")

# Strength
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/office/40/office.png" width="50" height="50" alt="strength" />
        <h2>Strength</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
- Punctuality
- Meeting deadlines
- Leadership qualities
- Management skills
- Ability to work under pressure
""")
st.write("---")

# Personal Details
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/arcade/64/business-contact.png" width="50" height="50" alt="personal-details" />
        <h2>Personal Details</h2>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("""
- **Name:** Meet Hareshbhai Mevada  
- **Date of Birth:** 17th September 2001  
- **Gender:** Male  
- **Marital Status:** Single/Unmarried  
- **Permanent Address:**  
  A-403 ShivHeights Apartment, Near Gathaman Patiya, Ahmedabad Highway, Palanpur-385001
""")
st.write("---")

# Declaration
st.markdown(
    """
    <div class="container">
        <img src="https://img.icons8.com/external-flat-amoghdesign/50/external-declaration-fourth-of-july-flat-amoghdesign.png" width="50" height="50" alt="declaration" />
        <h2>Declaration</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("""
I hereby declare that the above information is true to the best of my knowledge and belief.
""")

st.write("---")
# Signature
st.markdown(
    """
    <div style="margin-top: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="https://img.icons8.com/color/48/yours.png" width="20" height="20" alt="yours" style="margin-right: 5px;"/>
            <strong>Yours Sincerely,</strong>
        </div>
        <div style="display: flex; align-items: center;">
            <img src="https://img.icons8.com/officel/80/person-male-skin-type-4.png" width="20" height="20" alt="person-male-skin-type-4" style="margin-right: 5px;"/>
            <strong>Meet Mevada</strong>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

