# adding pytesting for solar.py script
# test
from solar import print_position
from solar import get_observer_location
from solar import get_elevation
from solar import get_sun_position


def test_print_position():
    result = print_position(float, float)


def test_get_observer_location():
    result = get_observer_location()
