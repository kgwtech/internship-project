from support.logger import logger
from pages.base_page import Page

class MyMenu(Page):

    # Base methods to be utilized in My Menu Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_main(self):
        self.open_url("")