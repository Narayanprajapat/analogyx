from app.helper.response_maker import response_maker
from app.helper import match_value
from app.models.students import Students


def create_student_api(request):
    try:
        print(request.form)
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        resp = Students().create({"name": 1})
        print(resp)
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)


def show_courses_api(request):
    try:
        print(request.form)
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        resp = Students().create({"name": 1})
        print(resp)
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)


def add_courses_enrollment_api(request):
    try:
        print(request.form)
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        resp = Students().create({"name": 1})
        print(resp)
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)
