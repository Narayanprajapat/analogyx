from flask import Blueprint, request

course = Blueprint('course', __name__)


@course.post('/admin/course', method=['POST'])
def course():
    print(request)
    return
