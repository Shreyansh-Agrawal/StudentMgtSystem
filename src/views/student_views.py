from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from src.controllers import student_controller
from src.models.schemas import StudentSchema, StudentUpdateSchema
from src.utils.rbac import access_level

router = APIRouter(tags=['Student'])


#@access_level(roles=['admin'])
@router.get('/students')
def get_all_students():
    data = student_controller.get_all_students()
    if not data:
        raise HTTPException(404, detail='No students present')
    return data


#@access_level(roles=['admin'])
@router.post('/students')
def add_student(request_data: StudentSchema):
    request_data = dict(request_data)
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
        raise HTTPException(400, f'Roll no {roll_no} already exists')

    student_controller.add_student(
            roll_no, name, age, gender, phone, date_of_joining, date_of_entry
        )
    data = student_controller.get_student(roll_no)
    return data[0]


@router.get('/students/{roll_no}')
def get_student(roll_no: int):
    data = student_controller.get_student(roll_no)
    if not data:
        raise HTTPException(404, detail=f'Roll no {roll_no} does not exists')

    return data[0]


#@access_level(roles=['admin'])
@router.patch('/students/{roll_no}')
def update_student(request_data: StudentUpdateSchema, roll_no: int):
    request_data = dict(request_data)
    student = student_controller.get_student(roll_no)
    if not student:
        raise HTTPException(400, detail=f'Roll no {roll_no} does not exists')

    new_name = request_data.get('new_name')

    student_controller.update_student(roll_no, new_name)
    data = student_controller.get_student(roll_no)
    return data[0]


#@access_level(roles=['admin'])
@router.delete('/students/{roll_no}')
def delete_student(roll_no: int):
    student = student_controller.get_student(roll_no)
    if not student:
        raise HTTPException(400, detail=f'Roll no {roll_no} does not exists')
    
    student_controller.delete_student(roll_no)
    return {'message': f'Roll no {roll_no} deleted'}
