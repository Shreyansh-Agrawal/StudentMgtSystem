from pydantic import BaseModel, Field


class CourseSchema(BaseModel):
    course_id: str = Field(pattern='[A-Z0-9{7}]')
    course_name: str = Field(pattern="[a-zA-Z {5,}]")
    course_credits: int
    course_discipline: str = Field(pattern="[A-Za-z {2,25}]")


class CourseUpdateSchema(BaseModel):
    new_course_name: str = Field(pattern="[a-zA-Z {5,}]")


class RegistrationSchema(BaseModel):
    roll_no: int
    course_id: str = Field(pattern="[A-Z0-9{7}]")


class RegistrationUpdateSchema(BaseModel):
    course_id: str = Field(pattern="[A-Z0-9{7}]")
    new_course_id: str = Field(pattern="[A-Z0-9{7}]")


class RegistrationDeleteSchema(BaseModel):
    course_id: str = Field(pattern="[A-Z0-9{7}]")


class StudentSchema(BaseModel):
    roll_no: int
    name: str = Field(pattern="^[A-Za-z {2,25}$]")
    age: int
    gender: str = Field(pattern="[M|F]")
    phone: str = Field(pattern="^[1-9][0-9]{9}")
    date_of_joining: str


class StudentUpdateSchema(BaseModel):
    new_name: str = Field(pattern="[A-Za-z {2,25}]")


class AuthSchema(BaseModel):
    username: str
    password: str
    role: str
