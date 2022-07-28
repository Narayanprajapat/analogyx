from app.helper.response_maker import response_maker
from app.helper import match_value
from app.models.courses import Course


def create_course_api(request):
    # try:
    #     print(request.form)
    # except Exception as e:
    #     print(e)
    #     return response_maker({"message": "Invalid input"}, 400)

    try:
        print("Create")
        Course().create({"name": "Narayan"})
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)
