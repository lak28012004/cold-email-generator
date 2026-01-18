from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_email(template, name, company, role, skills):
    templates = {

        "student": f"""
Subject: Internship / Entry-Level Opportunity – {role}

Dear Hiring Manager at {company},

My name is {name}, and I am a student interested in the {role} role.

I have gained practical experience in {skills} through projects and coursework.
I am eager to learn and contribute to your team.

Thank you for your time and consideration.

Best regards,
{name}
""",

        "fresher": f"""
Subject: Application for {role}

Dear Hiring Manager at {company},

My name is {name}, a recent graduate applying for the {role} position.

I have hands-on experience in {skills} and a strong willingness to learn and grow.

I would be excited to begin my professional journey with your organization.

Sincerely,
{name}
""",

        "experienced": f"""
Subject: Experienced Professional – {role}

Dear Hiring Manager at {company},

I am {name}, a professional with experience in {skills}, applying for the {role} role.

I have contributed to real-world projects and delivered meaningful results.
I would love to discuss how I can add value to your team.

Best regards,
{name}
""",

        "networking": f"""
Subject: Exploring Opportunities at {company}

Hello,

My name is {name}, and I am reaching out to connect regarding opportunities related to {role}.

With experience in {skills}, I am eager to learn more about your team and work.

Looking forward to connecting.

Warm regards,
{name}
"""
    }

    return templates.get(template, templates["fresher"])


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json or {}

    email = generate_email(
        data.get("template_type", "fresher"),
        data.get("name", "Candidate"),
        data.get("company", "Company"),
        data.get("role", "Role"),
        data.get("skills", "Skills")
    )

    return jsonify({"email": email})


@app.route("/")
def home():
    return jsonify({"status": "Cold Mail Generator API running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
