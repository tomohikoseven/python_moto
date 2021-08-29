# conftest.py

import pytest

from app.users_db import Users

@pytest.fixture
def db():
    users = Users()
    users.insert('Bob', 10)
    users.insert('Alice', 12)
    return users