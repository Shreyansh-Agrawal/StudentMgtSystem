from flask import Flask, jsonify, Blueprint
# from flask_restplus import Api
from views import course_views, registration_views, student_views

app = Flask(__name__)

app.register_blueprint(course_views.app, url_prefix='/v1')
app.register_blueprint(registration_views.app, url_prefix='/v1')
app.register_blueprint(student_views.app, url_prefix='/v1')

@app.route("/")
def home():
    data = {
        "endpoints": {
            "course": ["/courses", "/courses/{course_id}"],
            "registration": ['/registrations', '/registrations/{roll_no}'],
            "student": ['/students', 'students/{roll_no}'],
        }
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
