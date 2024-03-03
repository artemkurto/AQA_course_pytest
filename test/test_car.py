from files.car import Car
import pytest


@pytest.mark.parametrize("set_miles_limit, expected_miles_limit", [
    (1, 1,),
    (None, 0,),
    (-1, -1,),
    (0, 0,)
])
def test_miles_limit(set_miles_limit, expected_miles_limit):
    if set_miles_limit is None:
        car2 = Car('Ford', 'Focus')
    else:
        car2 = Car('Ford', 'Focus', set_miles_limit)
    assert car2.miles_limit == expected_miles_limit


def test_start_stopped_engine(create_car):
    assert create_car.start_engine() == "Engine started."


def test_start_running_engine(create_car):
    assert create_car.start_engine() == "Engine started."
    assert create_car.start_engine() == "Engine is already running."


def test_stop_stopped_engine(create_car):
    assert create_car.stop_engine() == "Engine is already off."


def test_stop_running_engine(create_car):
    create_car.start_engine()
    assert create_car.stop_engine() == "Engine stopped."
    assert create_car.stop_engine() == "Engine is already off."


@pytest.mark.parametrize("start_engine_in_test, miles_to_drive,  expected_message,", [
    (True, -1, 'Driving -1 miles.',),
    (True, 0, 'Driving 0 miles.',),
    (True, 1, 'Driving 1 miles.',),
    (True, 999, 'Driving 999 miles.',),
    (True, 1000, 'Driving 1000 miles.',),
    (True, 1001, 'The miles limit has been exceeded',),
    (False, -1, 'Cannot drive. Engine is off.',),
    (False, 0, 'Cannot drive. Engine is off.',),
    (False, 1, 'Cannot drive. Engine is off.',),
    (False, 999, 'Cannot drive. Engine is off.',),
    (False, 1000, 'Cannot drive. Engine is off.',),
    (False, 1001, 'Cannot drive. Engine is off.',),
])
def test_drive(create_car, get_miles_limit, start_engine_in_test, miles_to_drive, expected_message):
    if start_engine_in_test is False:
        assert create_car.drive(miles_to_drive) == expected_message
        assert create_car.miles_limit == get_miles_limit
        return
    create_car.start_engine()
    if miles_to_drive > get_miles_limit:
        assert create_car.drive(miles_to_drive) == expected_message
        assert create_car.miles_limit == get_miles_limit
        return
    assert create_car.drive(miles_to_drive) == expected_message
    assert create_car.miles_limit == get_miles_limit - miles_to_drive


@pytest.mark.parametrize("start_engine_in_test, miles_to_drive,  expected_message, num_of_drive", [
    (True, -1, 'Driving -1 miles.', 1,),
    (True, 0, 'Driving 0 miles.', 1,),
    (True, 1, 'Driving 1 miles.', 1,),
    (True, 999, 'Driving 999 miles.', 1,),
    (True, 1000, 'Driving 1000 miles.', 1,),
    (True, 1001, 'The miles limit has been exceeded', 1,),
    (False, 150, 'Cannot drive. Engine is off.', 1,),
    (True, -1, 'Driving -1 miles.', 2,),
    (True, 0, 'Driving 0 miles.', 2,),
    (True, 1, 'Driving 1 miles.', 2,),
    (True, 500, 'Driving 500 miles.', 2,),
    (True, 501, 'The miles limit has been exceeded', 2,),
    (True, 1001, 'The miles limit has been exceeded', 2,),
    (False, 1500, 'Cannot drive. Engine is off.', 3,),
    (True, -1, 'Driving -1 miles.', 3,),
    (True, 0, 'Driving 0 miles.', 3,),
    (True, 1, 'Driving 1 miles.', 3,),
    (True, 500, 'The miles limit has been exceeded', 3,),
    (True, 501, 'The miles limit has been exceeded', 3,),
    (True, 1001, 'The miles limit has been exceeded', 3,),
    (False, 1500, 'Cannot drive. Engine is off.', 3,)
])
def test_drive_several_starts(create_car, start_engine_in_test, miles_to_drive, expected_message, num_of_drive):
    miles_limit_in_car = create_car.miles_limit
    if start_engine_in_test is False:
        assert [create_car.drive(miles_to_drive) for _ in range(num_of_drive)][-1] == expected_message
        assert create_car.miles_limit == miles_limit_in_car
        return
    create_car.start_engine()
    if miles_to_drive * num_of_drive > miles_limit_in_car:
        assert [create_car.drive(miles_to_drive) for _ in range(num_of_drive)][-1] == expected_message
        # assert create_car.miles_limit == miles_limit_in_car
        return
    assert [create_car.drive(miles_to_drive) for _ in range(num_of_drive)][-1] == expected_message
    assert create_car.miles_limit == miles_limit_in_car - miles_to_drive * num_of_drive
