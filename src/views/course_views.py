from controllers import course_controller
from flask import jsonify, Blueprint, request

app = Blueprint('courses', __name__)


@app.get('/courses/<string:course_id>')
def get_course(course_id):
    data = course_controller.get_course(course_id)
    if not data:
        return jsonify({'response': f'Course with course id {course_id} does not exists'})

    return jsonify({'data':data})


@app.get('/courses')
def get_all_courses():
    data = course_controller.get_all_courses()
    if not data:
        return jsonify({'response': f'Course data not found'})
    return jsonify({'data':data})


@app.post('/courses')
def create_course():
    request_data = request.get_json()

    course_name = request_data.get('course_name')
    course_id = request_data.get('course_id')
    course_credits = request_data.get('course_credits')
    course_discipline = request_data.get('course_discipline')
    date_of_entry = request_data.get('date_of_entry')

    course_controller.add_course(
            course_id, course_name, course_credits, course_discipline, date_of_entry
        )
    return request_data, 201


@app.patch('/courses/<string:course_id>')
def update_course(course_id):
    course = course_controller.get_course(course_id)
    if not course:
        return jsonify({'response': f'Course data not found'})
    
    request_data = request.get_json()
    new_course_name = request_data.get('new_course_name')
    course_controller.update_course(course_id, new_course_name)
    return request_data, 200


@app.delete('/courses/<string:course_id>')
def delete_course(course_id):
    course = course_controller.get_course(course_id)
    if not course:
        return jsonify({'response': f'Course data not found'})
    
    course_controller.delete_course(course_id)
    return jsonify({'response': 200})
