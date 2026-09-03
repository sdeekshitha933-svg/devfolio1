from app import app
from database.models import db, Project, Skill


with app.app_context():

    # ==============================
    # SKILLS
    # ==============================

    skills = []

    skill1 = Skill()
    skill1.name = "Python"
    skill1.category = "Programming"
    skills.append(skill1)

    skill2 = Skill()
    skill2.name = "JavaScript"
    skill2.category = "Programming"
    skills.append(skill2)

    skill3 = Skill()
    skill3.name = "HTML"
    skill3.category = "Frontend"
    skills.append(skill3)

    skill4 = Skill()
    skill4.name = "CSS"
    skill4.category = "Frontend"
    skills.append(skill4)

    skill5 = Skill()
    skill5.name = "Flask"
    skill5.category = "Backend"
    skills.append(skill5)

    skill6 = Skill()
    skill6.name = "PostgreSQL"
    skill6.category = "Database"
    skills.append(skill6)

    skill7 = Skill()
    skill7.name = "Machine Learning"
    skill7.category = "AI / ML"
    skills.append(skill7)

    skill8 = Skill()
    skill8.name = "Git & GitHub"
    skill8.category = "Tools"
    skills.append(skill8)

    db.session.add_all(skills)


    # ==============================
    # PROJECTS
    # ==============================

    projects = []

    project1 = Project()
    project1.title = "Smart Learner AI"
    project1.description = (
        "An AI-powered learning platform that helps students "
        "learn through personalized content, quizzes, assignments "
        "and performance tracking."
    )
    project1.technologies = "Python, Flask, PostgreSQL, AI/ML"
    project1.github_url = "https://github.com/"
    project1.live_url = ""
    project1.image_url = ""
    projects.append(project1)

    project2 = Project()
    project2.title = "Devfolio"
    project2.description = (
        "A full-stack personal portfolio website built to showcase "
        "projects, technical skills and development experience."
    )
    project2.technologies = "HTML, CSS, JavaScript, Flask, PostgreSQL"
    project2.github_url = "https://github.com/"
    project2.live_url = ""
    project2.image_url = ""
    projects.append(project2)

    project3 = Project()
    project3.title = "Student Performance Analyzer"
    project3.description = (
        "A machine learning based application that analyzes "
        "student performance and provides useful insights."
    )
    project3.technologies = "Python, Pandas, Scikit-learn, Machine Learning"
    project3.github_url = "https://github.com/"
    project3.live_url = ""
    project3.image_url = ""
    projects.append(project3)

    db.session.add_all(projects)

    # ==============================
    # SAVE TO DATABASE
    # ==============================

    db.session.commit()

    print("===================================")
    print("Sample data inserted successfully!")
    print("Skills:", len(skills))
    print("Projects:", len(projects))
    print("===================================")