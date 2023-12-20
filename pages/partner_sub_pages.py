from selenium.webdriver.common.by import By
from support.logger import logger
from pages.base_page import Page

class PartnerSubPages(Page):

    """ Partner Sub Pages Constant Element Locators """

    JOIN_SOCIAL_TXT = (By.CSS_SELECTOR, ".name-chat-text")
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "a.contact-button.w-inline-block[href*=https]")

    # Base methods to be utilized in Page Object Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def verify_contact_us_opened(self):
        self.wait_for_visibility(*self.JOIN_SOCIAL_TXT)
        self.verify_text("Join us in social media", *self.JOIN_SOCIAL_TXT)

    def verify_contact_us_social_icons(self, number):
        number = int(number)
        icons = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert number >= len(icons), \
            f"Verify there are at least {len(icons)} social media icons (Contact us)"


