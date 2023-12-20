from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class MyMenu(Page):

    """ My Menu Page Constant Element Locators """
    MY_MENU_TXT = (By.CSS_SELECTOR, ".h1-menu")
    BECOME_PART_BTN = (By.CSS_SELECTOR, "a[class*=part]")
    ADD_PROJECT_BTN = (By.CSS_SELECTOR, "a.card-button-menu[href*=project]")
    ADD_AGENCY_BTN = (By.CSS_SELECTOR, "a.card-button-menu[href*=market]")
    VIEW_ALL_SPEAKERS_BTN = (By.CSS_SELECTOR, "a.speakers-button[href*=edu]")
    OFF_PLAN_PROJECTS_BTN = (By.CSS_SELECTOR, "a.project-location-block[href*=off-plan]")

    # Base methods to be utilized in My Menu Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def verify_sign_in(self):
        self.verify_text("My menu", *self.MY_MENU_TXT)