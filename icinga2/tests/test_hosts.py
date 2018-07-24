from __future__ import absolute_import

import copy

import pytest

from icinga2 import Icinga2API
from .constants import constants


@pytest.mark.run(order=1)
def test_host_add():
    """
    Testing the addition of a host
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    data = copy.deepcopy(constants.TestHost_data)

    response = api.hosts.add(data)

    assert response['results'][0]['code'] == 200


@pytest.mark.run(order=2)
def test_host_exists():
    """
    Testing if the host was added correctly
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.hosts.exists(constants.TestHost_data['attrs']['name'])

    assert response


@pytest.mark.run(order=8)
def test_host_list():
    """
    Listing all Hosts, and check if created host is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.hosts.list()

    assert constants.TestHost_data['attrs']['name'] in response


@pytest.mark.run(order=9)
def test_host_objects():
    """
    Get all Host Objects and check if created host is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.hosts.objects()

    assert any(res.get('name', None) == constants.TestHost_data['attrs']['name'] for res in response)


@pytest.mark.run(order=10)
def test_host_delete():
    """
    Delete the created Host
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=False)

    response = api.hosts.delete(constants.TestHost_data['attrs']['name'])

    assert response != None
