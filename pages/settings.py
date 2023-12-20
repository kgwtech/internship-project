from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class Settings(Page):

    """ Settings Page Constant Element Locators """

    CONTACTS_US_BTN = (By.CSS_SELECTOR, "a.page-setting-block[href*=contact]")

    # Base methods to be utilized in Settings Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def click_contact_us(self):
        self.wait_for_visibility(*self.CONTACTS_US_BTN)
        self.click(*self.CONTACTS_US_BTN)