from flask_sqlalchemy import SQLAlchemy


# ============================================================
# DATABASE OBJECT
# ============================================================

db = SQLAlchemy()


# ============================================================
# PROJECT MODEL
# ============================================================

class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    technologies = db.Column(
        db.String(300)
    )

    github_url = db.Column(
        db.String(300)
    )

    live_url = db.Column(
        db.String(300)
    )

    image_url = db.Column(
        db.String(300)
    )


# ============================================================
# SKILL MODEL
# ============================================================

class Skill(db.Model):

    __tablename__ = "skills"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(100)
    )


# ============================================================
# MESSAGE MODEL
# ============================================================

class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )