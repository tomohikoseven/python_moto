# users_db.py


class Users:
    def __init__(self):
        self.last_insert_id = 0
        self.rows = {}

    def insert(self, name, age):
        self.last_insert_id += 1
        self.rows[self.last_insert_id] = {
            'id': self.last_insert_id,
            'name': name,
            'age': age,
        }

    def get(self, id_):
        return self.rows[id_]