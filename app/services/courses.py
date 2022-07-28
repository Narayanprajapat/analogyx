from app.helper.response_maker import response_maker
from app.helper import match_value
from app.models.courses import Courses
from datetime import datetime


def create_course_api(request):
    try:
        req = request.get_json()
        title = req['title']  # Python
        price = req['price']  # 10000
        level = req['level']  # 10000
        course_type = req['course_type']  # live courses, e-book, video

        instructor = req['instructor_detail']
        instructor_name = instructor['name']  # XYZ
        instructor_email = instructor['email']  # xyz@gmail.com

        module = req['module']
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        if not match_value(title, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid title"}, 400)

        if not match_value(str(price), "^\\d+$"):
            return response_maker({"message": "Invalid price"}, 400)

        if not match_value(level, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid level"}, 400)

        if not match_value(course_type, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid course type"}, 400)

        if not match_value(instructor_name, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid instructor name"}, 400)

        if not match_value(instructor_email, r"^\S+@\S+\.\S+$"):
            return response_maker({"message": "Invalid instructor email"}, 400)

        payload = {
            "title": title,
            "price": price,
            "level": level,
            "course_type": course_type,
            "instructor_detail": {
                "name": instructor_name,
                "email": instructor_email
            },
            "module": module,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }
        Courses().create(payload)
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)
