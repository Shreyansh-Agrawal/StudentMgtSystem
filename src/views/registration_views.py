from controllers import registration_controller
from flask import jsonify, Blueprint, request

app = Blueprint('registration', __name__)


@app.route('/registrations/<string:roll_no>')
def get_registration(roll_no):
    data = registration_controller.get_registration(roll_no)
    if not data:
        return jsonify({'response': f'Registration data for roll no {roll_no} not found'})

    return jsonify({'data':data})


@app.route('/registrations')
def get_all_registrations():
    data = registration_controller.get_all_registrations()
    if not data:
        return jsonify({'response': f'Registration data for not found'})
    return jsonify({'data':data})


@app.post('/registrations')
def create_registration():
    request_data = request.get_json()

    roll_no = request_data.get('roll_no')
    course_id = request_data.get('course_id')
    date_of_entry = request_data.get('date_of_entry')

    registration_controller.add_registration(roll_no, course_id, date_of_entry)
    return request_data, 201


@app.patch('/registrations/<string:roll_no>')
def update_registration(roll_no):
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        return jsonify({'response': f'registration data not found'})
    
    request_data = request.get_json()
    course_id = request_data.get('course_id')
    new_course_id = request_data.get('new_course_id')

    registration_controller.update_registration(roll_no, course_id, new_course_id)
    return request_data, 200


@app.delete('/registrations/<string:roll_no>')
def delete_registration(roll_no):
    registration = registration_controller.get_registration(roll_no)
    if not registration:
        return jsonify({'response': f'registration data not found'})

    request_data = request.get_json()
    course_id = request_data.get('course_id')
    
    registration_controller.delete_registration(roll_no, course_id)
    return jsonify({'response': 200})
