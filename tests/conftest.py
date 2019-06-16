import pytest
from application import application


@pytest.fixture
def app():
    return application