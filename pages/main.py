from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class Main(Page):

    """ Main Page Constant Element Locators """

    SIGN_IN_BTN = (By.CSS_SELECTOR, "a.button-hero[href*=sign-in]")


    # Base methods to be utilized in Main Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_main(self):
        self.open_url("https://www.reelly.io/")
    def click_open_browser_btn(self):
        self.click(*self.SIGN_IN_BTN)
