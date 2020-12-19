import pytest
from selenium import webdriver

from page_objects import GLCareersPage, GoogleSearchPage, PyPIMainPage


@pytest.fixture
def browser():
    dr = webdriver.Firefox()
    yield dr
    dr.close()


def test_first_task(browser):
    google_search_page = GoogleSearchPage(browser)
    google_results_page = google_search_page.search_by_phrase(
        'selenium install ubuntu python')
    google_results_page.open_result_that_contains_in_link('pypi.org')

    assert browser.current_url == 'https://pypi.org/project/selenium/'

    pypi_main_page = PyPIMainPage(browser)
    pypi_results_page = pypi_main_page.search_python_project_by_phrase(
        'selenium')
    pypi_results_page.open_python_project_by_number(1)  # from zero

    assert 'https://pypi.org/project/' in browser.current_url


def test_second_task(browser, capsys):
    gl_careers_page = GLCareersPage(browser)
    gl_careers_page.allow_cookies()
    gl_careers_results_page = gl_careers_page.search_vacansy('QA')
    gl_careers_vacancy_page = gl_careers_results_page.open_vacansy_by_number(0)

    with capsys.disabled():
        print(('\nHEADER OF FIRST RESULT:'
               f'\n\t{gl_careers_vacancy_page.vacancy_title}\n'))

    assert 'https://www.globallogic.com/ua/careers/' in browser.current_url
