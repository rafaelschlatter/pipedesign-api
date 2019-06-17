import pytest
from application import app as application

@pytest.fixture
def app():
    return application