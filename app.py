
from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

EMAIL_TEMPLATES_BY_ROLE = {
    "fresher": [
        """Subject: Application Inquiry – Junior {role} Position at {company}

Dear {receiver},

I hope this message finds you well. As a recent graduate with a strong interest in {skills} and a passion for learning, I am writing to express my eager interest in the Junior {role} position at {company}. My academic projects and coursework in [mention relevant course/project] have equipped me with a foundational understanding that I believe would be a valuable asset to your team.

I have been closely following {company}'s innovative work in [mention specific area/project], and I am particularly drawn to [mention company values or specific aspects]. I am confident that my enthusiasm and ability to quickly grasp new concepts would allow me to make a significant contribution as an entry-level professional.

Could we schedule a brief call to discuss how my qualifications could benefit {company}?

Thank you for your time and consideration.

Best regards,
{sender}"""
    ],
    "experienced": [
        """Subject: Inquiry about {role} Position at {company}

Dear {receiver},

I am writing to express my strong interest in the {role} position at {company}. My background includes extensive experience in {skills}, which I believe aligns well with your team's needs. In my previous role at [Previous Company], I successfully [mention a key achievement or responsibility].

I have been closely following {company}'s innovative work in [mention specific area/project], and I am particularly drawn to [mention company values or specific aspects]. I am confident that my skills and enthusiasm would allow me to make a significant contribution.

Could we schedule a brief call to discuss how my qualifications could benefit {company}? I am eager to share how my experience can drive success for your team.

Thank you for your time.

Best regards,
{sender}""",

        """Subject: Potential Collaboration – {sender} from {company_sender}

Greetings {receiver},

My name is {sender}, and I represent {company_sender}, a firm specializing in {skills}. I'm reaching out because I see a great synergy between our work and {company}'s initiatives. We have a proven track record in [mention a relevant success or expertise], and believe our solutions could significantly benefit your team's efforts in [mention a specific area].

I would appreciate the chance to discuss potential collaboration and explore how we might support your goals. Are you available for a quick call next week?

Best regards,
{sender}"""
    ],
    "college_student": [
        """Subject: Internship/Co-op Inquiry – {role} at {company}

Dear {receiver},

I am a current student at [University Name] pursuing a degree in [Your Major], with a strong focus on {skills}. I am writing to express my keen interest in an internship or co-op opportunity for a {role} position at {company}.n
I have been impressed by {company}'s innovative projects in [mention specific area/project] and believe my academic background in [mention relevant coursework] and practical experience with [mention specific tools/technologies] would allow me to contribute meaningfully to your team.

I am eager to learn from industry experts and gain hands-on experience. Would you be open to a brief conversation about potential opportunities?

Thank you for your time and consideration.

Best regards,
{sender}"""
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    email = None
    if request.method == "POST":
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        role_type = request.form["role_type"]
        role = request.form["role"]
        skills = request.form["skills"]
        company = request.form["company"]

        templates = EMAIL_TEMPLATES_BY_ROLE.get(role_type, EMAIL_TEMPLATES_BY_ROLE["fresher"])
        template = random.choice(templates)
        email = template.format(
            sender=sender,
            receiver=receiver,
            role=role,
            skills=skills,
            company=company
        )
        if "company_sender" in template and "company_sender" in request.form:
            email = email.format(company_sender=request.form["company_sender"])

    return render_template("index.html", email=email)

@app.route("/download_email", methods=["POST"])
def download_email():
    email_content = request.form.get("email_content")
    if not email_content:
        return "No email content provided for download.", 400

    html_content = f"<html><body><pre>{email_content}</pre></body></html>"

    response = make_response(html_content)
    response.headers["Content-Disposition"] = "attachment; filename=cold_email.html"
    response.headers["Content-Type"] = "text/html"
    return response

