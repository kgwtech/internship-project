from support.logger import logger
from pages.base_page import Page

class MainPage(Page):

    # Base methods to be utilized in Main Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_main(self):
        self.open_url("")