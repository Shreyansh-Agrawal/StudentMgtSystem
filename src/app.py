import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI

from src.blocklist import BLOCKLIST
from src.views.auth_views import router as AuthRouter
from src.views.course_views import router as CourseRouter
from src.views.registration_views import router as RegistrationRouter
from src.views.student_views import router as StudentRouter

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


def create_app():
    app = FastAPI()
    app.include_router(AuthRouter, prefix='/v1')
    app.include_router(CourseRouter, prefix='/v1')
    app.include_router(RegistrationRouter, prefix='/v1')
    app.include_router(StudentRouter, prefix='/v1')

    return app
