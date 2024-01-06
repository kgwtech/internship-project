from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class OffPlan(Page):

    """ Off Plan Page Constant Element Locators """
    TOTAL_PROJECTS_TXT = (By.CSS_SELECTOR, "div.page-title")
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, "a.project-card[href*='878']")
    PRODUCT_CARD_NAME = (By.CSS_SELECTOR, "[wized=projectName]")

    # Base methods to be utilized in Off-Plan Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////


    def click_first_product(self):
        self.wait_for_visibility(*self.FIRST_PRODUCT_CARD)
        self.click(*self.FIRST_PRODUCT_CARD)
        self.wait_for_visibility(*self.PRODUCT_CARD_NAME)
        self.find_element(*self.PRODUCT_CARD_NAME)

    def verify_off_plan_page(self):
        self.wait_for_visibility(*self.TOTAL_PROJECTS_TXT)
        self.verify_text("Total projects", *self.TOTAL_PROJECTS_TXT)