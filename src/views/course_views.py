from datetime import datetime, timezone

from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from controllers import course_controller
from views.schemas import CourseSchema, CourseUpdateSchema

blp = Blueprint('courses', __name__)


@blp.get('/courses/<string:course_id>')
@jwt_required()
@blp.response(200, CourseSchema)
def get_course(course_id):
    data = course_controller.get_course(course_id)
    if not data:
        abort(404, message=f'Course with course id {course_id} does not exists')

    return data[0]


@blp.get('/courses')
@jwt_required()
@blp.response(200, CourseSchema(many=True))
def get_all_courses():
    data = course_controller.get_all_courses()
    if not data:
        abort(404, message=f'No courses present')

    return data


@blp.post('/courses')
@jwt_required()
@blp.arguments(CourseSchema)
@blp.response(201, CourseSchema)
def create_course(request_data): # the req data gets passed thru the schema and then to this func after validation
    course_id = request_data.get('course_id')
    course_name = request_data.get('course_name')
    course_credits = request_data.get('course_credits')
    course_discipline = request_data.get('course_discipline')
    time = datetime.now(timezone.utc)  # current utc time
    date_of_entry = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    data = course_controller.get_course(course_id)
    if data:
        abort(400, message=f'Course with course id {course_id} already exists')

    course_controller.add_course(
            course_id, course_name, course_credits, course_discipline, date_of_entry
        )
    return request_data


@blp.patch('/courses/<string:course_id>')
@jwt_required()
@blp.arguments(CourseUpdateSchema)
@blp.response(200, CourseSchema)
def update_course(request_data, course_id):
    course = course_controller.get_course(course_id)
    if not course:
        abort(400, message=f'Course with course id {course_id} does not exists')

    new_course_name = request_data.get('new_course_name')
    course_controller.update_course(course_id, new_course_name)
    course = course_controller.get_course(course_id)
    return course[0]


@blp.delete('/courses/<string:course_id>')
@jwt_required()
def delete_course(course_id):
    course = course_controller.get_course(course_id)
    if not course:
        abort(400, message=f'Course with course id {course_id} does not exists')
    
    course_controller.delete_course(course_id)
    return {'message': f'Course with course id {course_id} deleted'}
