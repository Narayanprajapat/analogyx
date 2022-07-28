from app.models import database


class Students:
    def __init__(self):
        self._filter = None
        self.query = None
        self.data = None

    def create(self, data):
        self.data = data
        return database.students.insert_one(self.data)

    def read(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.students.find(self._filter, self.query)

    def read_one(self, _filter, query):
        self._filter = _filter
        self.query = query
        return database.students.find_one(self._filter, self.query)

    def update(self, _filter, data):
        self._filter = _filter
        self.data = data
        return database.students.find_one(self._filter, self.data)
