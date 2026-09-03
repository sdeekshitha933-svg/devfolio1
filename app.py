from flask import Flask, render_template, request, jsonify
from threading import Timer
import webbrowser

from config import Config
from database.models import db, Project, Skill, Message


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config.from_object(Config)

db.init_app(app)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    skills = Skill.query.order_by(
        Skill.id.asc()
    ).all()

    projects = Project.query.order_by(
        Project.id.asc()
    ).all()

    return render_template(
        "home.html",
        skills=skills,
        projects=projects
    )


# ============================================================
# PROJECT DETAILS PAGE
# ============================================================

@app.route("/project/<int:project_id>")
def project_details(project_id):

    project = Project.query.get_or_404(
        project_id
    )

    return render_template(
        "project_details.html",
        project=project
    )


# ============================================================
# CONTACT API
# ============================================================

@app.route("/api/contact", methods=["POST"])
def contact():

    data = request.get_json(silent=True)

    # --------------------------------------------------------
    # CHECK REQUEST
    # --------------------------------------------------------

    if not data:

        return jsonify({
            "success": False,
            "message": "Invalid request."
        }), 400


    # --------------------------------------------------------
    # GET FORM DATA
    # --------------------------------------------------------

    name = data.get("name", "").strip()

    email = data.get("email", "").strip()

    message_text = data.get(
        "message",
        ""
    ).strip()


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not name:

        return jsonify({
            "success": False,
            "message": "Please enter your name."
        }), 400


    if not email:

        return jsonify({
            "success": False,
            "message": "Please enter your email."
        }), 400


    if not message_text:

        return jsonify({
            "success": False,
            "message": "Please enter your message."
        }), 400


    # ========================================================
    # CREATE MESSAGE OBJECT
    # ========================================================
    #
    # IMPORTANT:
    # We are NOT doing:
    #
    # Message(
    #     name=name,
    #     email=email,
    #     message=message_text
    # )
    #
    # because Pylance may show:
    # No parameter named "message"
    #
    # Instead, create the object first and assign values.
    # ========================================================

    new_message = Message()


    new_message.name = name

    new_message.email = email

    new_message.message = message_text


    # --------------------------------------------------------
    # SAVE MESSAGE TO POSTGRESQL
    # --------------------------------------------------------

    try:

        db.session.add(
            new_message
        )

        db.session.commit()

    except Exception as error:

        db.session.rollback()

        print(
            "Contact database error:",
            error
        )

        return jsonify({
            "success": False,
            "message": "Unable to save your message."
        }), 500


    # --------------------------------------------------------
    # SUCCESS RESPONSE
    # --------------------------------------------------------

    return jsonify({
        "success": True,
        "message": "Your message has been sent successfully!"
    }), 201


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

with app.app_context():

    db.create_all()


# ============================================================
# AUTOMATICALLY OPEN BROWSER
# ============================================================

def open_browser():

    webbrowser.open(
        "http://127.0.0.1:5000/",
        new=2
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    # Open the portfolio automatically
    Timer(
        1,
        open_browser
    ).start()


    # Start Flask server
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )