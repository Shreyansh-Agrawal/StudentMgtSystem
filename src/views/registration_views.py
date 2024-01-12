from datetime import datetime, timezone

from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from src.controllers import registration_controller
from src.models.schemas import RegistrationSchema, RegistrationUpdateSchema, RegistrationDeleteSchema
from src.utils.rbac import access_level

blp = Blueprint('registration', __name__)


@blp.route('/registrations/<string:roll_no>')
@jwt_required()
@blp.response(200, RegistrationSchema)
def get_registration(roll_no):
    data = registration_controller.get_registration(roll_no)
    if not data:
        abort(404, message=f'Registration data for roll no {roll_no} not found')
    return data[0]


@blp.route('/registrations')
@access_level(roles=['admin'])
@jwt_required()
@blp.response(200, RegistrationSchema(many=True))
def get_all_registrations():
    data = registration_controller.get_all_registrations()
    if not data:
        abort(404, message=f'Registration data not found')
    return data


@blp.post('/registrations')
@access_level(roles=['admin'])
@jwt_required(fresh=True)
@blp.arguments(RegistrationSchema)
@blp.response(201, RegistrationSchema)
def create_registration(request_data):
    roll_no = request_data.get('roll_no')
    course_id = request_data.get('course_id')
    time = datetime.now(timezone.utc)  # current utc time
    date_of_registration = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    registration = registration_controller.get_registration(roll_no)
    if registration and registration[0].get('course_id') == course_id:
        abort(400, message=f'Registration already exists')

    registration_controller.add_registration(roll_no, course_id, date_of_registration)
    data = registration_controller.get_registration(roll_no)
    return data[0]


@blp.patch('/registrations/<string:roll_no>')
@access_level(roles=['admin'])
@jwt_required(fresh=True)
@blp.arguments(RegistrationUpdateSchema)
@blp.response(200, RegistrationSchema)
def update_registration(request_data, roll_no):
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        abort(400, message=f'Registration data for roll no {roll_no} not found')

    course_id = request_data.get('course_id')
    new_course_id = request_data.get('new_course_id')

    registration_controller.update_registration(roll_no, course_id, new_course_id)
    data = registration_controller.get_registration(roll_no)
    return data[0]


@blp.delete('/registrations/<string:roll_no>')
@access_level(roles=['admin'])
@jwt_required(fresh=True)
@blp.arguments(RegistrationDeleteSchema)
def delete_registration(request_data, roll_no):
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        abort(400, message=f'Registration data for roll no {roll_no} not found')

    course_id = request_data.get('course_id')
    
    registration_controller.delete_registration(roll_no, course_id)
    return {'message': f'Registration of {roll_no} deleted for {course_id}'}
