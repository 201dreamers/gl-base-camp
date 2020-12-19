import requests
from urllib.parse import urljoin

from endpoints.endpoints import Endpoints
from config.config import Config


class ReqResApiClient():

    __slots__ = ()

    @staticmethod
    def _prepare_url(url, base_url=Config.REQRES_BASE_URL):
        return urljoin(base_url, url)

    @staticmethod
    def list_users():
        response = requests.get(
            ReqResApiClient._prepare_url(Endpoints.USERS_URL))
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_user(user_details):
        response = requests.post(
            ReqResApiClient._prepare_url(Endpoints.USERS_URL),
            json=user_details
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def register(user_credentials):
        response = requests.post(
            ReqResApiClient._prepare_url(Endpoints.REGISTER_URL),
            json=user_credentials
        )
        response.raise_for_status()
        return response.json() 

    @staticmethod
    def login(user_credentials):
        response = requests.post(
            ReqResApiClient._prepare_url(Endpoints.LOGIN_URL),
            json=user_credentials
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def list_unknown():
        response = requests.get(
            ReqResApiClient._prepare_url(Endpoints.UNKNOWN_URL))
        response.raise_for_status()
        return response.json()
