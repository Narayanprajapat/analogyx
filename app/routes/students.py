from flask import Blueprint, request
from app.services.students import create_student_api, show_all_courses_api, add_courses_enrollment_api

student = Blueprint('student', __name__)


@student.route('/create-student', methods=['POST'])
def create_student():
    return create_student_api(request)


@student.route('/show-all-courses', methods=['POST'])
def show_all_courses():
    return show_all_courses_api()


@student.route('/add-courses-enrollment', methods=['POST'])
def add_courses_enrollment():
    return add_courses_enrollment_api(request)
