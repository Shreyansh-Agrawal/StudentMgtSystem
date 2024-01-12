import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from blocklist import BLOCKLIST
from views.auth_views import blp as AuthBlueprint
from views.course_views import blp as CourseBlueprint
from views.registration_views import blp as RegistrationBlueprint
from views.student_views import blp as StudentBlueprint

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True # propagate any exception of flask extension, propagate it to main app
    app.config["API_TITLE"] = "Student Management System REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3" # a standard for api documentation
    app.config["OPENAPI_URL_PREFIX"] = "/" # root of our endpoint
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app) # Connects flask smorest extension to flask app

    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    jwt = JWTManager(app) # create an instance of jwt manager

    # whenever we receive jwt, this func runs and checks if the token is in blocklist

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    # if the above func returns true, this func runs
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    # for adding additional claims to jwt token

    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
    #     if identity == 'admin':
    #         return {"is_admin": True}
    #     return {"is_admin": False}

    # for jwt token error messages
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    api.register_blueprint(CourseBlueprint, url_prefix='/v1')
    api.register_blueprint(RegistrationBlueprint, url_prefix='/v1')
    api.register_blueprint(StudentBlueprint, url_prefix='/v1')
    api.register_blueprint(AuthBlueprint, url_prefix='/v1')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
