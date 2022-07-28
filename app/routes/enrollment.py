from flask import Blueprint, request
from app.services.enrollment import add_enrollment_api

enrollment = Blueprint('enrollment', __name__)


@enrollment.route('/add-enrollment', methods=['GET'])
def add_enrollment():
    return add_enrollment_api(request)
