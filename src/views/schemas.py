from marshmallow import Schema, fields

class CourseSchema(Schema):
    # define fields and how they behave in terms of input and output
    # for only returning data use dump_only=True
    # required=True means must be present in the request
    course_id = fields.Str(required=True)
    course_name = fields.Str(required=True)
    course_credits = fields.Int(required=True)
    course_discipline = fields.Str(required=True)
    date_of_entry = fields.Str(format="%Y-%m-%d", dump_only=True) # validation not working


class CourseUpdateSchema(Schema):
    new_course_name = fields.Str(required=True)


class RegistrationSchema(Schema):
    roll_no = fields.Int(required=True)
    name = fields.Str(dump_only=True)
    course_id = fields.Str(required=True)
    course_name = fields.Str(dump_only=True)
    date_of_registration = fields.Str(format="%Y-%m-%d", dump_only=True)


class RegistrationUpdateSchema(Schema):
    course_id = fields.Str(required=True)
    new_course_id = fields.Str(required=True)


class RegistrationDeleteSchema(Schema):
    course_id = fields.Str(required=True)


class StudentSchema(Schema):
    roll_no = fields.Int(required=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)
    phone = fields.Str(required=True)
    date_of_joining = fields.Str(format="%Y-%m-%d", required=True)
    date_of_entry = fields.Str(format="%Y-%m-%d", dump_only=True)


class StudentUpdateSchema(Schema):
    new_name = fields.Str(required=True)
