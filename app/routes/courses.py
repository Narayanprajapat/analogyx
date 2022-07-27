from flask import Blueprint, request

from app.services.courses import create_course_api

course = Blueprint('course', __name__)


@course.route('/admin/create-course', methods=['GET'])
def create_course():
    return create_course_api(request)
