import pytest
# Because flask app needs to be called "app" in order to work on Azure devops,
# and pytest fixture needs to be named "app" in order to work with pytest-flask.
from application import app as application

@pytest.fixture
def app():
    return application