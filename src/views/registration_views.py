from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from src.controllers import registration_controller
from src.models.schemas import RegistrationSchema, RegistrationUpdateSchema, RegistrationDeleteSchema
from src.utils.rbac import access_level

router = APIRouter(tags=['Registration'])


#@access_level(roles=['admin'])
@router.get('/registrations')
def get_all_registrations():
    data = registration_controller.get_all_registrations()
    if not data:
        raise HTTPException(404, detail=f'Registration data not found')
    return data


#@access_level(roles=['admin'])
@router.post('/registrations')
def add_registration(request_data: RegistrationSchema):
    request_data = dict(request_data)
    roll_no = request_data.get('roll_no')
    course_id = request_data.get('course_id')
    time = datetime.now(timezone.utc)  # current utc time
    date_of_registration = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    registration = registration_controller.get_registration(roll_no)
    if registration and registration[0].get('course_id') == course_id:
        raise HTTPException(400, detail=f'Registration already exists')

    registration_controller.add_registration(roll_no, course_id, date_of_registration)
    data = registration_controller.get_registration(roll_no)
    return data[0]


@router.get('/registrations/{roll_no}')
def get_registration(roll_no: int):
    data = registration_controller.get_registration(roll_no)
    if not data:
        raise HTTPException(404, detail=f'Registration data for roll no {roll_no} not found')
    return data[0]


#@access_level(roles=['admin'])
@router.patch('/registrations/{roll_no}')
def update_registration(request_data: RegistrationUpdateSchema, roll_no: int):
    request_data = dict(request_data)
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        raise HTTPException(400, detail=f'Registration data for roll no {roll_no} not found')

    course_id = request_data.get('course_id')
    new_course_id = request_data.get('new_course_id')

    registration_controller.update_registration(roll_no, course_id, new_course_id)
    data = registration_controller.get_registration(roll_no)
    return data[0]


#@access_level(roles=['admin'])
@router.delete('/registrations/{roll_no}')
def delete_registration(request_data: RegistrationDeleteSchema, roll_no: int):
    request_data = dict(request_data)
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        raise HTTPException(400, detail=f'Registration data for roll no {roll_no} not found')

    course_id = request_data.get('course_id')
    
    registration_controller.delete_registration(roll_no, course_id)
    return {'message': f'Registration of {roll_no} deleted for {course_id}'}
