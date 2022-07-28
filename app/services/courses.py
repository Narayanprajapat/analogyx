from app.helper.response_maker import response_maker
from app.helper import match_value


def create_course_api(request):
    try:
        print(request.form)
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        return response_maker({}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)
