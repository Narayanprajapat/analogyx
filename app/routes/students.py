from flask import Blueprint, request
from app.services.students import create_student_api, otp_verify_api, show_courses_api, add_courses_enrollment_api

student = Blueprint('student', __name__)


@student.route('/create-student', methods=['GET'])
def create_student():
    return create_student_api(request)


@student.route('/otp-verify', methods=['GET'])
def otp_verify():
    return otp_verify_api(request)


@student.route('/show-courses', methods=['GET'])
def show_courses():
    return show_courses_api(request)


@student.route('/add-courses-enrollment', methods=['GET'])
def add_courses_enrollment():
    return add_courses_enrollment_api(request)
