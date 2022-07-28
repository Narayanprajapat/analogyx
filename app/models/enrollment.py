from app.models import database


class Enrollments:
    def __init__(self):
        self._filter = None
        self.query = None
        self.data = None

    def create(self, data):
        self.data = data
        return database.enrollments.insert_one(self.data)

    def read(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.enrollments.find(self._filter, self.query)

    def read_one(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.enrollments.find_one(self._filter, self.query)
