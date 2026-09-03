from app import app
from database.models import db, Project


with app.app_context():

    project1 = Project.query.filter_by(
        title="Smart Learner AI"
    ).first()

    project2 = Project.query.filter_by(
        title="Devfolio"
    ).first()

    project3 = Project.query.filter_by(
        title="Student Performance Analyzer"
    ).first()


    if project1:
        project1.image_url = (
            "/static/images/projects/project-01.jpg"
        )


    if project2:
        project2.image_url = (
            "/static/images/projects/project-02.jpg"
        )


    if project3:
        project3.image_url = (
            "/static/images/projects/project-03.jpg"
        )


    db.session.commit()


    print("===================================")
    print("Project images connected successfully!")
    print("===================================")