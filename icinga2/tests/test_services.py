from __future__ import absolute_import

import pytest

from icinga2 import Icinga2API
from .constants import constants


@pytest.mark.run(order=3)
def test_service_add():
    """
    Testing the addition of a service
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.services.add(servicename=constants.TestService_name,
                                hostname=constants.TestHost_data['attrs']['name'], data=constants.TestService_data)

    assert response['results'][0]['code'] == 200


@pytest.mark.run(order=4)
def test_service_exists():
    """
    Testing if the service was added correctly
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.services.exists(constants.TestService_name)

    assert response


@pytest.mark.run(order=5)
def test_service_list():
    """
    Listing all services, and check if created service is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.services.list(hostname=constants.TestHost_data['attrs']['name'])

    assert constants.TestHost_data['attrs']['name'] + "!" + constants.TestService_name in response.values()


@pytest.mark.run(order=6)
def test_service_objects():
    """
    Get all service Objects and check if created service is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.services.objects()

    assert any(result['attrs'].get('name', None) == constants.TestService_name for result in response)


@pytest.mark.run(order=7)
def test_service_delete():
    """
    Delete the created service
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.services.delete(servicename=constants.TestService_name,
                                   hostname=constants.TestHost_data['attrs']['name'])

    assert response != None
