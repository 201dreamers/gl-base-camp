from requests.exceptions import HTTPError

import pytest

from api.reqres_api_client import ReqResApiClient


def test_reqres_returns_users_list():
    users_list = ReqResApiClient.list_users()
    assert users_list['per_page'] == len(users_list['data'])


def test_reqres_can_create_user():
    user_details = {
        'name': 'morpheus',
        'job': 'leader'
    }
    user = ReqResApiClient.create_user(user_details)
    assert (user['name'] == 'morpheus' and user['job'] == 'leader' and
            user.get('id') is not None)


def test_reqres_can_register():
    user_credentials = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }
    registration_info = ReqResApiClient.register(user_credentials)
    assert registration_info == {'id': 4, 'token': 'QpwL5tke4Pnpja7X4'}


def test_reqres_fails_on_register():
    user_credentials = {
        'password': 'pistol'
    }
    with pytest.raises(HTTPError):
        ReqResApiClient.register(user_credentials)

    user_credentials = {
        'email': 'eve.holt@reqres.in'
    }
    with pytest.raises(HTTPError):
        ReqResApiClient.register(user_credentials)


def test_reqres_can_login():
    user_credentials = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    login_info = ReqResApiClient.login(user_credentials)
    assert login_info == {'token': 'QpwL5tke4Pnpja7X4'}


def test_reqres_fails_on_login():
    user_credentials = {
        'email': 'eve.holt@reqres.in',
    }
    with pytest.raises(HTTPError):
        ReqResApiClient.login(user_credentials)

    user_credentials = {
        'password': 'cityslicka'
    }
    with pytest.raises(HTTPError):
        ReqResApiClient.login(user_credentials)


def test_reqres_returns_list_of_unknown():
    list_of_unknown = ReqResApiClient.list_unknown()
    assert list_of_unknown['total_pages'] >= list_of_unknown['page']