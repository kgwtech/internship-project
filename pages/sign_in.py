from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class SignIn(Page):

    """ Sign In Page Constant Element Locators """

    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASS_FIELD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button")

    # Base methods to be utilized in Sign In Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_sign_in(self):
        self.open_url("https://soft.reelly.io/sign-in")

    # def login(self, email, password):
    #     self.input_credentials(email, password)
    #     self.click_continue()

    def input_credentials(self, email, password):
        self.wait_for_visibility(*self.EMAIL_FIELD)
        self.input_text(email, *self.EMAIL_FIELD)
        self.wait_for_visibility(*self.PASS_FIELD)
        self.input_text(password, *self.PASS_FIELD)

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)
