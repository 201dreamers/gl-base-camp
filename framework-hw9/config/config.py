import os


class Config:

    REQRES_BASE_URL = os.getenv('TESTS_BASE_URL', 'https://reqres.in')
