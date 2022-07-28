from app.helper.response_maker import response_maker
from app.helper import match_value
from app.models.students import Students
from datetime import datetime


def create_student_api(request):
    try:
        req = request.get_json()
        fname = req['fname']
        lname = req['lname']
        email = req['email']
        mobile_no = req['mobile_no']
        college = req['college']
        expected_graduation = req['expected_graduation']
        address = req['address']
        state = address['state']
        pincde = address['pincde']
        district = address['district']
        town = address['town']
    except Exception as e:
        print(e)
        return response_maker({"message": "Invalid input"}, 400)

    try:

        if not match_value(fname, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid first name"}, 400)

        if not match_value(lname, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid last name"}, 400)

        if not match_value(email, r"^\S+@\S+\.\S+$"):
            return response_maker({"message": "Invalid instructor email"}, 400)

        if not match_value(str(mobile_no), "^\\+?[1-9][0-9]{7,14}$"):
            return response_maker({"message": "Invalid mobile no"}, 400)

        if not match_value(college, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid college name"}, 400)

        if not match_value(str(expected_graduation), "^\\d+$"):
            return response_maker({"message": "Invalid expected graduation"}, 400)

        if not match_value(state, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid state"}, 400)

        if not match_value(str(pincde), "^\\d+$"):
            return response_maker({"message": "Invalid pincode"}, 400)

        if not match_value(district, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid district"}, 400)

        if not match_value(town, "^[a-zA-Z ]{0,}$"):
            return response_maker({"message": "Invalid town"}, 400)

        payload = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "mobile_no": mobile_no,
            "college": college,
            "expected_graduation": expected_graduation,
            "address": {
                "state": state,
                "pincde": pincde,
                "district": district,
                "town": town
            },
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }
        query = {"email": email}
        resp = Students().read_one(query, {"email": 1})
        print(resp)
        if resp is None:
            Students().create(payload)
            return response_maker({"message": "Success"}, 201)
        return response_maker({"message": "User already exist"}, 400)
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
