from datetime import datetime, timezone

from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from src.controllers import course_controller
from src.models.schemas import CourseSchema, CourseUpdateSchema
from src.utils.rbac import access_level

blp = Blueprint('courses', __name__)


@blp.route('/courses')
class CourseList(MethodView):
    
    # @jwt_required()
    @blp.response(200, CourseSchema(many=True))
    def get(self):
        data = course_controller.get_all_courses()
        if not data:
            abort(404, message=f'No courses present')

        return data

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    @blp.arguments(CourseSchema)
    @blp.response(201, CourseSchema)
    def post(self, request_data): # the req data gets passed thru the schema and then to this func after validation
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


@blp.route('/courses/<string:course_id>')
class Course(MethodView):

    @jwt_required()
    @blp.response(200, CourseSchema)
    def get(self, course_id):
        data = course_controller.get_course(course_id)
        if not data:
            abort(404, message=f'Course with course id {course_id} does not exists')
        return data[0]

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    @blp.arguments(CourseUpdateSchema)
    @blp.response(200, CourseSchema)
    def patch(self, request_data, course_id):
        course = course_controller.get_course(course_id)
        if not course:
            abort(400, message=f'Course with course id {course_id} does not exists')

        new_course_name = request_data.get('new_course_name')
        course_controller.update_course(course_id, new_course_name)
        course = course_controller.get_course(course_id)
        return course[0]

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    def delete(self, course_id):
        course = course_controller.get_course(course_id)
        if not course:
            abort(400, message=f'Course with course id {course_id} does not exists')
        
        course_controller.delete_course(course_id)
        return {'message': f'Course with course id {course_id} deleted'}
