"""Selenium WebDriver tests

You need a webdriver binary, pytest-webdriver, selenium, and flask-selenium
installed, and specify the webdriver on the command line, eg.

pytest --driver Chrome --driver-path /path/to/chromedriver

"""


import pytest
import time
from .data import edit_distance_test_data


SLEEP_LEN = 1


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    edit_distance_test_data
)
def test_webdriver(live_server, selenium, source, target, distance):
    """All known edit distances are shown correctly in the browser"""
    selenium.get('http://localhost:{}/'.format(live_server.port))
    selenium.find_element_by_id('source').send_keys(source)
    selenium.find_element_by_id('target').send_keys(target)
    selenium.find_element_by_id('submit').click()
    time.sleep(SLEEP_LEN)  # too long?
    assert int(selenium.find_element_by_id('result').text) == distance


def test_webdriver_same_browser(live_server, selenium):
    """All known edit distances show correctly in *the same* browser"""
    selenium.get('http://localhost:{}'.format(live_server.port))
    sourcefield = selenium.find_element_by_id('source')
    targetfield = selenium.find_element_by_id('target')
    submitbut = selenium.find_element_by_id('submit')
    resultdiv = selenium.find_element_by_id('result')
    for source, target, distance in edit_distance_test_data:
        sourcefield.send_keys(source)
        targetfield.send_keys(target)
        submitbut.click()
        time.sleep(SLEEP_LEN)
        assert int(resultdiv.text) == distance
        sourcefield.clear()
        targetfield.clear()
        time.sleep(SLEEP_LEN)