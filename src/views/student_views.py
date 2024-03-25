from datetime import datetime, timezone

from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from src.controllers import student_controller
from src.models.schemas import StudentSchema, StudentUpdateSchema
from src.utils.rbac import access_level

blp = Blueprint('students', __name__)


@blp.route('/students')
class StudentList(MethodView):

    # @access_level(roles=['admin'])
    # @jwt_required()
    @blp.response(200, StudentSchema(many=True))
    def get(self):
        data = student_controller.get_all_students()
        if not data:
            abort(404, message='No students present')
        return data

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    @blp.arguments(StudentSchema)
    @blp.response(201, StudentSchema)
    def post(self, request_data):
        roll_no = request_data.get('roll_no')
        name = request_data.get('name')
        age = request_data.get('age')
        gender = request_data.get('gender')
        phone = request_data.get('phone')
        date_of_joining = request_data.get('date_of_joining')
        time = datetime.now(timezone.utc)  # current utc time
        date_of_entry = time.strftime("%Y-%m-%d")  # yyyy-mm-dd
        
        data = student_controller.get_student(roll_no)
        if data:
            abort(400, f'Roll no {roll_no} already exists')

        student_controller.add_student(
                roll_no, name, age, gender, phone, date_of_joining, date_of_entry
            )
        data = student_controller.get_student(roll_no)
        return data[0]


@blp.route('/students/<string:roll_no>')
class StudentDetails(MethodView):

    @jwt_required()
    @blp.response(200, StudentSchema)
    def get(self, roll_no):
        data = student_controller.get_student(roll_no)
        if not data:
            abort(404, message=f'Roll no {roll_no} does not exists')

        return data[0]

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    @blp.arguments(StudentUpdateSchema)
    @blp.response(200, StudentSchema)
    def patch(self, request_data, roll_no):
        student = student_controller.get_student(roll_no)
        if not student:
            abort(400, message=f'Roll no {roll_no} does not exists')

        new_name = request_data.get('new_name')

        student_controller.update_student(roll_no, new_name)
        data = student_controller.get_student(roll_no)
        return data[0]

    @access_level(roles=['admin'])
    @jwt_required(fresh=True)
    def delete(self, roll_no):
        student = student_controller.get_student(roll_no)
        if not student:
            abort(400, message=f'Roll no {roll_no} does not exists')
        
        student_controller.delete_student(roll_no)
        return {'message': f'Roll no {roll_no} deleted'}
