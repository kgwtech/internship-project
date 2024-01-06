from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class OffPlanSubPages(Page):

    """ Off Plan Sub Pages Constant Element Locators """
    VISUALISATIONS_TABS = (By.CSS_SELECTOR, "a[class*='w-tab-link']")

    # Base methods to be utilized in Off-Plan Page Steps
    """ Base Methods"""  # //////////////////////////////////////////////

    def verify_visualisations(self):
        tabs = self.find_elements(*self.VISUALISATIONS_TABS)
        assert len(tabs) == 3

    def click_visualisations(self):
        c = 0
        s = self.find_elements(*self.VISUALISATIONS_TABS)
        for i in s:
            self.click()
            c += 1
            yield i
        assert c == 3

