from playwright.sync_api import Page
from consts.consts import BASE_URL
from ui.pages.base_page import BasePage


class StartPage(BasePage):
    URL = BASE_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.donat_button = self.locator("//*[@id='XBGSFAMB']")
