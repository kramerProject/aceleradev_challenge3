from main import get_temperature
import pytest
from unittest.mock import patch


@patch('main.requests.get')
@pytest.mark.parametrize("farenheit,celsius",[(62,16),(32,0),(70,21),(110,43),(0,-17)])
def test_get_temperature_by_lat_lng(mock_get,farenheit,celsius):
    """
    :param mock_get: Object that imitates requests.get in the main function
    :param farenheit: Temperature in Farenheit
    :param celsius: Temperature in Celsius
    :return: Expected and Celsius must be equal.
    """
    lat = -14.235004
    lng = -51.92528
    mock_get = mock_get.return_value
    mock_data = mock_get.json.return_value
    mock_data.get.return_value.get.return_value=farenheit
    expected = get_temperature(lat,lng)

    assert expected == celsius

errors=[(1000,10,{'code': 400, 'error': 'The given location is invalid.'}),
        (10,1000,{'code': 400, 'error': 'The given location is invalid.'}),
        ('teste',1000,{'code': 400, 'error': 'Poorly formatted request'})]

@pytest.mark.parametrize("lat,lng,error", errors)
def test_get_temperature_by_valid_lat_lng(lat,lng,error):
    """
    :param lat: Latitude value
    :param lng: Longitude value
    :return: We expect some kind of error since at least one of the values are not valid
    """
    expected=get_temperature(lat,lng)

    assert expected == error

