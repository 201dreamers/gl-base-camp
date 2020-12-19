import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    dr = webdriver.Firefox()
    yield dr
    dr.close()


@pytest.fixture
def timeout():
    return 10


def test_first_task(driver, timeout):
    driver.get('https://www.google.com')

    google_search_field = driver.find_element_by_name('q')
    google_search_field.clear()
    google_search_field.send_keys(
        'selenium install ubuntu python',
        Keys.RETURN
    )

    WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="yuRUbf"]')
        )
    )

    pypi_selenium_link = driver.find_element_by_partial_link_text('pypi.org')
    pypi_selenium_link.click()

    pypi_search_field = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )
    pypi_search_field.clear()
    pypi_search_field.send_keys('selenium', Keys.RETURN)

    list_of_pypi_packages = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'package-snippet'))
    )

    list_of_pypi_packages[1].click()

    assert driver.title == 'amazon-selenium · PyPI'


def test_task_2(driver, timeout, capsys):
    driver.get('https://www.globallogic.com/ua/careers/')

    gl_search_field = driver.find_element_by_id('by_keyword')
    gl_search_field.clear()
    gl_search_field.send_keys('QA', Keys.RETURN)

    first_card = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="career-pagelink"][1]//p[1]')
        )
    )
    with capsys.disabled():
        print(f'\nHEADER OF FIRST RESULT:\n\t{first_card.text}\n')

    assert first_card.text
