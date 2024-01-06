from controllers import student_controller
from flask import jsonify, Blueprint, request

app = Blueprint('students', __name__)


@app.route('/students/<string:roll_no>')
def get_student(roll_no):
    data = student_controller.get_student(roll_no)
    if not data:
        return jsonify({'response': f'Student data for roll no {roll_no} not found'})

    return jsonify({'data': data})


@app.route('/students')
def get_all_students():
    data = student_controller.get_all_students()
    if not data:
        return jsonify({'response': f'Student data not found'})
    return jsonify({'data': data})


@app.post('/students')
def create_student():
    request_data = request.get_json()

    roll_no = request_data.get('roll_no')
    name = request_data.get('name')
    age = request_data.get('age')
    gender = request_data.get('gender')
    phone = request_data.get('phone')
    date_of_joining = request_data.get('date_of_joining')
    date_of_entry = request_data.get('date_of_entry')

    student_controller.add_student(
            roll_no, name, age, gender, phone, date_of_joining, date_of_entry
        )
    return request_data, 201


@app.patch('/students/<string:roll_no>')
def update_student(roll_no):
    student = student_controller.get_student(roll_no)
    if not student:
        return jsonify({'response': f'student data not found'})
    
    request_data = request.get_json()
    new_name = request_data.get('new_name')

    student_controller.update_student(roll_no, new_name)
    return request_data, 200


@app.delete('/students/<string:roll_no>')
def delete_student(roll_no):
    student = student_controller.get_student(roll_no)
    if not student:
        return jsonify({'response': f'student data not found'})
    
    student_controller.delete_student(roll_no)
    return jsonify({'response': 200})
