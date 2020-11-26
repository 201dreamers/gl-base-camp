from selenium.webdriver.common.by import By

from base_app import BaseApp
import config


class GoogleSearchPage(BaseApp):

    URI = config.GOOGLE_URL

    LOCATOR_SEARCH_FIELD = (By.NAME, 'q')
    LOCATOR_SEARCH_BUTTON = (
        By.CSS_SELECTOR, '.FPdoLc > center:nth-child(1) > input:nth-child(1)'
    )

    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(self.URI)

    def search_by_phrase(self, phrase):
        self.write_into_input_field(self.LOCATOR_SEARCH_FIELD,
                                    phrase)
        self.click_element(self.LOCATOR_SEARCH_BUTTON)

        return GoogleResultsPage(self.browser)


class GoogleResultsPage(BaseApp):

    LOCATOR_ALL_SEARCH_RESULTS = (By.XPATH, '//div[@class="yuRUbf"]')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.open_page(config.GOOGLE_URL + urn)

    def open_result_that_contains_in_link(self, partial_link):
        self.wait_for_presence_of_all_elements_located(
            self.LOCATOR_ALL_SEARCH_RESULTS)
        LOCATOR_PYPI_LINK_RESULT = (By.PARTIAL_LINK_TEXT, partial_link)
        self.click_element(LOCATOR_PYPI_LINK_RESULT)


class PyPIMainPage(BaseApp):

    URI = config.PYPI_URL

    LOCATOR_SEARCH_FIELD = (By.ID, 'search')
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, 'search-form__button')

    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(self.URI)

    def search_python_project_by_phrase(self, phrase):
        self.write_into_input_field(self.LOCATOR_SEARCH_FIELD, phrase)
        self.click_element(self.LOCATOR_SEARCH_BUTTON)

        return PyPIResultsPage(self.browser)


class PyPIResultsPage(BaseApp):

    LOCATOR_PYPI_SEARCH_RESULTS = (By.CLASS_NAME, 'package-snippet')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.open_page(config.PYPI_URL + urn)

    def open_python_project_by_number(self, number_of_project):
        self.click_element_from_list_of_elements(
            PyPIResultsPage.LOCATOR_PYPI_SEARCH_RESULTS, number_of_project)


class GLCareersPage(BaseApp):

    URI = config.GLOBAL_LOGIC_URL + '/ua/careers/'

    LOCATOR_SEARCH_FIELD = (By.ID, 'by_keyword')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//div[1]/section[1]//button')
    LOCATOR_COOKIE_ALLOW_ALL_BUTTON = (
        By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(self.URI)

    def allow_cookies(self):
        self.click_element(GLCareersPage.LOCATOR_COOKIE_ALLOW_ALL_BUTTON)

    def search_vacansy(self, vacansy):
        self.write_into_input_field(GLCareersPage.LOCATOR_SEARCH_FIELD,
                                    vacansy)
        self.click_element(GLCareersPage.LOCATOR_SEARCH_BUTTON)

        return GLCareersResultsPage(self.browser)


class GLCareersResultsPage(BaseApp):

    LOCATOR_GL_SEARCH_RESULTS = (By.XPATH,
                                 '//div[@class="career-pagelink"]//p[1]')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.open_page(GLCareersPage.URI + urn)

    def open_vacansy_by_number(self, number_of_vacansy):
        self.click_element_from_list_of_elements(
            self.LOCATOR_GL_SEARCH_RESULTS, number_of_vacansy)
        
        return GLCareersVacancyPage(self.browser)


class GLCareersVacancyPage(BaseApp):

    LOCATOR_VACANCY_TITLE = (By.CLASS_NAME, 'job-title')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.open_page(GLCareersPage.URI + urn)

    @property
    def vacancy_title(self):
        return self.find_element(
            self.LOCATOR_VACANCY_TITLE).text
