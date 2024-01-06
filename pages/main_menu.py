from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class MainMenu(Page):

    """ Main Menu Page Constant Element Locators """
    MAIN_MENU_TXT = (By.CSS_SELECTOR, ".h1-menu")
    BECOME_PART_BTN = (By.CSS_SELECTOR, "a[class*=part]")
    ADD_PROJECT_BTN = (By.CSS_SELECTOR, "a.card-button-menu[href*=project]")
    ADD_AGENCY_BTN = (By.CSS_SELECTOR, "a.card-button-menu[href*=market]")
    VIEW_ALL_SPEAKERS_BTN = (By.CSS_SELECTOR, "a.speakers-button[href*=edu]")
    OFF_PLAN_PROJECTS_BTN = (By.CSS_SELECTOR, "a.project-location-block[href*=off-plan]")
    SETTINGS_BTN = (By.CSS_SELECTOR, "a.menu-button-block[href*=set]")
    OFF_PLAN_LEFT_MENU = (By.CSS_SELECTOR, "a._1-link-menu")


    # Base methods to be utilized in Main Menu Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def click_settings_option(self):
        self.wait_for_visibility(*self.SETTINGS_BTN)
        self.click(*self.SETTINGS_BTN)

    def verify_sign_in(self):
        # self.wait_for_element_appear(*self.MAIN_MENU_TXT)
        self.wait_for_visibility(*self.MAIN_MENU_TXT)
        self.verify_text("Main menu", *self.MAIN_MENU_TXT)

    def click_off_plan_option(self):
        self.wait_for_visibility(*self.OFF_PLAN_LEFT_MENU)
        self.click(*self.OFF_PLAN_LEFT_MENU)



