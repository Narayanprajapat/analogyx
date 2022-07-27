from app.helper.response_maker import response_maker


def create_course_api(request):
    print(request)
    return response_maker({}, 200)
