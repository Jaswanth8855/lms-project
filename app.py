
from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {"id": 1, "name": "Python Programming", "instructor": "Ravi"},
    {"id": 2, "name": "Database Management", "instructor": "Priya"},
    {"id": 3, "name": "Web Development", "instructor": "Arun"}
]

@app.route("/")
def home():
    return """
    <h1>Learning Management System</h1>
    <a href="/courses">View Available Courses</a>
    """

@app.route("/courses")
def get_courses():
    html = "<h1>Available Courses</h1><ul>"
    for course in courses:
        html += f"<li>{course['name']} - {course['instructor']}</li>"
    html += "</ul>"
    return html

@app.route("/api/courses")
def courses_api():
    return jsonify(courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
