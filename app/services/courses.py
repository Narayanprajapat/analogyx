from app.helper.response_maker import response_maker
from app.helper import match_value
from app.models.courses import Courses


def create_course_api(request):
    try:
        print(request.get_json())
        title = request.form['title']  # Python
        price = request.form['price']  # 10000
        level = request.form['level']  # 10000
        course_type = request.form['course_type']  # live courses, e-book, video
        instructor_name = request.form['instructor_name']  # XYZ
        instructor_email = request.form['instructor_email']  # xyz@gmail.com

    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:
        payload = {
            "title": title,
            "price": price,
            "course_type": course_type,
            "level": level,
            "instructor": {
                "name": instructor_name,
                "email": instructor_email
            }
        }
        name = match_value('Name Narayan', "^[a-zA-Z ]{0,}$")
        print(name)
        resp = Courses().create({"name": 1})
        print(resp)
        return response_maker({"message": "Success"}, 201)
    except Exception as e:
        print(e)
        return response_maker({"message": "Internal server error"}, 500)


modules = [
    {
        "title": '',
        "sub_modules": [{"title": "", "duration": "", "video_url": "", "show_preview": True}]
    }
]
