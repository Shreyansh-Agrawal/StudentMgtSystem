from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.controllers import course_controller
from src.models.schemas import CourseSchema, CourseUpdateSchema
from src.utils.rbac import access_level

router = APIRouter(tags=['Course'])
templates = Jinja2Templates(directory='src/templates')


@router.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@router.get('/courses')
def get_all_courses():
    data = course_controller.get_all_courses()
    if not data:
        raise HTTPException(404, detail=f'No courses present')

    return data


#@access_level(roles=['admin'])
@router.post('/courses')
def create_course(request_data: CourseSchema): # the req data gets passed thru the schema and then to this func after validation
    request_data = dict(request_data)
    course_id = request_data.get('course_id')
    course_name = request_data.get('course_name')
    course_credits = request_data.get('course_credits')
    course_discipline = request_data.get('course_discipline')
    time = datetime.now(timezone.utc)  # current utc time
    date_of_entry = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    data = course_controller.get_course(course_id)
    if data:
        raise HTTPException(400, detail=f'Course with course id {course_id} already exists')

    course_controller.add_course(
            course_id, course_name, course_credits, course_discipline, date_of_entry
        )
    return request_data


@router.get('/courses/{course_id}')
def get_course(course_id: str):
    data = course_controller.get_course(course_id)
    if not data:
        raise HTTPException(404, detail=f'Course with course id {course_id} does not exists')
    return data[0]


#@access_level(roles=['admin'])
@router.patch('/courses/{course_id}')
def update_course(request_data: CourseUpdateSchema, course_id: str):
    
    course = course_controller.get_course(course_id)
    if not course:
        raise HTTPException(400, detail=f'Course with course id {course_id} does not exists')

    request_data = dict(request_data)
    new_course_name = request_data.get('new_course_name')
    course_controller.update_course(course_id, new_course_name)
    course = course_controller.get_course(course_id)
    return course[0]


#@access_level(roles=['admin'])
@router.delete('/courses/{course_id}')
def delete_course(course_id: str):
    course = course_controller.get_course(course_id)
    if not course:
        raise HTTPException(400, detail=f'Course with course id {course_id} does not exists')
    
    course_controller.delete_course(course_id)
    return {'message': f'Course with course id {course_id} deleted'}
