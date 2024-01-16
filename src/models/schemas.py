from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    # define fields and how they behave in terms of input and output
    # for only returning data use dump_only=True
    # load_only=True means only in req not in res
    # required=True means must be present in the request
    course_id = fields.Str(required=True, validate=validate.Regexp("[A-Z0-9]{7}"))
    course_name = fields.Str(required=True, validate=validate.Regexp("[a-zA-Z ]{5,}"))
    course_credits = fields.Int(required=True)
    course_discipline = fields.Str(required=True, validate=validate.Regexp("[A-Za-z ]{2,25}"))
    date_of_entry = fields.Str(format="%Y-%m-%d", dump_only=True) # validation not working


class CourseUpdateSchema(Schema):
    new_course_name = fields.Str(required=True, validate=validate.Regexp("[a-zA-Z ]{5,}"))


class RegistrationSchema(Schema):
    roll_no = fields.Int(required=True)
    name = fields.Str(dump_only=True, validate=validate.Regexp("[A-Za-z ]{2,25}"))
    course_id = fields.Str(required=True, validate=validate.Regexp("[A-Z0-9]{7}"))
    course_name = fields.Str(dump_only=True, validate=validate.Regexp("[a-zA-Z ]{5,}"))
    date_of_registration = fields.Str(format="%Y-%m-%d", dump_only=True)


class RegistrationUpdateSchema(Schema):
    course_id = fields.Str(required=True, validate=validate.Regexp("[A-Z0-9]{7}"))
    new_course_id = fields.Str(required=True, validate=validate.Regexp("[A-Z0-9]{7}"))


class RegistrationDeleteSchema(Schema):
    course_id = fields.Str(required=True, validate=validate.Regexp("[A-Z0-9]{7}"))


class StudentSchema(Schema):
    roll_no = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Regexp("^[A-Za-z ]{2,25}$"))
    age = fields.Int(required=True)
    gender = fields.Str(required=True, validate=validate.Regexp("[M|F]"))
    phone = fields.Str(required=True, validate=validate.Regexp("^[1-9][0-9]{9}"))
    date_of_joining = fields.Str(format="%Y-%m-%d", required=True)
    date_of_entry = fields.Str(format="%Y-%m-%d", dump_only=True)


class StudentUpdateSchema(Schema):
    new_name = fields.Str(required=True, validate=validate.Regexp("[A-Za-z ]{2,25}"))


class AuthSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str()
