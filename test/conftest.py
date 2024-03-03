import pytest
from files.car import Car


@pytest.fixture()
def get_brand():
    return 'Ford'


@pytest.fixture()
def get_model():
    return 'Focus'


@pytest.fixture()
def get_miles_limit():
    return 1000


@pytest.fixture()
def create_car(get_brand, get_model, get_miles_limit):
    return Car(get_brand, get_model, get_miles_limit)


@pytest.fixture(scope='function', autouse=False)
def stop_engine(create_car):
    create_car.stop_engine()
    yield
    create_car.stop_engine()


