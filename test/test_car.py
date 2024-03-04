from files.car import Car
import pytest


def test_miles_limit_set_none():
    car2 = Car('Ford', 'Focus')
    assert car2.miles_limit == 0


@pytest.mark.parametrize("set_miles_limit", [1, 0, 2.4])
def test_miles_limit_pos(set_miles_limit):
    car2 = Car('Ford', 'Focus', set_miles_limit)
    assert car2.miles_limit == set_miles_limit


@pytest.mark.xfail
@pytest.mark.parametrize("set_miles_limit", [-1, 'a', True, None, [1, 3, 'asd'], {'asd', 'sffq', 3}])
def test_miles_limit_neg(set_miles_limit):
    car2 = Car('Ford', 'Focus', set_miles_limit)
    raise 'Some Error'


def test_stop_stopped_engine(create_car):
    assert create_car.stop_engine() == "Engine is already off."


def test_stop_running_engine(create_car):
    create_car.start_engine()
    assert create_car.stop_engine() == "Engine stopped."


def test_start_stopped_engine(create_car):
    assert create_car.start_engine() == "Engine started."


def test_start_running_engine(create_car):
    create_car.start_engine()
    assert create_car.start_engine() == "Engine is already running."


@pytest.mark.parametrize(" miles_to_drive,  expected_message,", [
    (0, 'Cannot drive. Engine is off.',),
    (1, 'Cannot drive. Engine is off.',),
    (999, 'Cannot drive. Engine is off.',),
    (1000, 'Cannot drive. Engine is off.',),
    (1001, 'Cannot drive. Engine is off.',),
])
def test_drive_stopped_engine_check_message(create_car, miles_to_drive, expected_message):
    assert create_car.drive(miles_to_drive) == expected_message


@pytest.mark.parametrize("miles_to_drive,", [0, 1, 500, 999, 1000, 1001])
def test_drive_stopped_engine_check_miles_limit(create_car, miles_to_drive, get_miles_limit):
    create_car.drive(miles_to_drive)
    assert create_car.miles_limit == get_miles_limit


@pytest.mark.parametrize("miles_to_drive, expected_message", [
    (0, 'Driving 0 miles.',),
    (1, 'Driving 1 miles.',),
    (999, 'Driving 999 miles.',),
    (1000, 'Driving 1000 miles.',),
    (1001, 'The miles limit has been exceeded',),
    (3000, 'The miles limit has been exceeded',),
])
def test_drive_miles_limit_check_message(create_car, miles_to_drive, expected_message):
    create_car.start_engine()
    assert create_car.drive(miles_to_drive) == expected_message


@pytest.mark.parametrize("miles_to_drive", [0, 1, 500, 999, 1000,])
def test_drive_miles_limit_check_before_limit(create_car, get_miles_limit, miles_to_drive):
    create_car.start_engine()
    create_car.drive(miles_to_drive)
    assert create_car.miles_limit == get_miles_limit - miles_to_drive


@pytest.mark.parametrize("miles_to_drive", [1001, 2000])
def test_drive_miles_limit_check_after_limit(create_car, get_miles_limit, miles_to_drive):
    create_car.start_engine()
    create_car.drive(miles_to_drive)
    assert create_car.miles_limit == get_miles_limit


@pytest.mark.parametrize("miles_to_drive, expected_message", [
    (0, 'Driving 0 miles.',),
    (1, 'Driving 1 miles.',),
    (500, 'Driving 500 miles.',),
    (501, 'The miles limit has been exceeded',),
    (1001, 'The miles limit has been exceeded',),
    (3000, 'The miles limit has been exceeded',),
])
def test_double_drive_miles_limit_check_message(create_car, miles_to_drive, expected_message):
    create_car.start_engine()
    assert [create_car.drive(miles_to_drive) for _ in range(2)][-1] == expected_message


@pytest.mark.parametrize("miles_to_drive", [0, 1, 500,])
def test_double_drive_miles_limit_check_before_limit(create_car, get_miles_limit, miles_to_drive):
    create_car.start_engine()
    [create_car.drive(miles_to_drive) for _ in range(2)]
    assert create_car.miles_limit == get_miles_limit - miles_to_drive * 2


@pytest.mark.parametrize("miles_to_drive", [1001, 2000])
def test_double_drive_miles_limit_check_after_limit(create_car, get_miles_limit, miles_to_drive):
    create_car.start_engine()
    [create_car.drive(miles_to_drive) for _ in range(2)]
    assert create_car.miles_limit == get_miles_limit


@pytest.mark.parametrize("miles_to_drive", [501, 1000])
def test_double_drive_miles_limit_check_mix_limit(create_car, get_miles_limit, miles_to_drive):
    create_car.start_engine()
    [create_car.drive(miles_to_drive) for _ in range(2)]
    assert create_car.miles_limit == get_miles_limit - miles_to_drive
