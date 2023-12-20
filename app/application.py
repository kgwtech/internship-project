from pages.base_page import Page
from pages.main import Main
from pages.market import Market
from pages.my_menu import MyMenu
from pages.off_plan import OffPlan
from pages.referral import Referral
from pages.secondary import Secondary
from pages.settings import Settings
from pages.sign_in import SignIn
from pages.workshops import Workshops


class Application:
    # Establishes links between Page Objects and Behave context
    # Give access to driver
    # Gives usability of methods from pages
    def __init__(self, driver):
        # Base
        self.page = Page(driver)

        # Page Objects
        self.main = Main(driver)
        self.market = Market(driver)
        self.my_menu = MyMenu(driver)
        self.off_plan = OffPlan(driver)
        self.referral = Referral(driver)
        self.secondary = Secondary(driver)
        self.settings = Settings(driver)
        self.sign_in = SignIn(driver)
        self.workshops = Workshops(driver)


