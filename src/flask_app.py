from flask import Flask
from flask_smorest import Api

from views.course_views import blp as CourseBlueprint
from views.registration_views import blp as RegistrationBlueprint
from views.student_views import blp as StudentBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True # propagate any exception of flask extension, propagate it to main app
app.config["API_TITLE"] = "Student Management System REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3" # a standard for api documentation
app.config["OPENAPI_URL_PREFIX"] = "/" # root of our endpoint
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app) # Connects flask smorest extension to flask app
api.register_blueprint(CourseBlueprint, url_prefix='/v1')
api.register_blueprint(RegistrationBlueprint, url_prefix='/v1')
api.register_blueprint(StudentBlueprint, url_prefix='/v1')


if __name__ == '__main__':
    app.run(debug=True)
