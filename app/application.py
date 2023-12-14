from pages.base_page import Page
from pages.main_page import MainPage


class Application:
    # Establishes links between Page Objects and Behave context
    # Give access to driver
    # Gives usability of methods from pages
    def __init__(self, driver):
        # Base
        self.page = Page(driver)

        # Page Objects
        self.main_page = MainPage(driver)
