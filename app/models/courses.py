from app.models import database


class Courses:
    def __init__(self):
        self._filter = None
        self.query = None
        self.data = None

    def create(self, data):
        self.data = data
        return database.courses.insert_one(self.data)

    def read(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.courses.find(self._filter, self.query)

    def read_one(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.courses.find_one(self._filter, self.query)
