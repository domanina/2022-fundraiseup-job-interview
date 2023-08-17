import allure

from playwright.sync_api import Page
from ui.pages.base_page import BasePage
from ui.pages.donation_page import DonatFrame


class PersonalFrame(BasePage):
    DONATE_BUTTON = "//button[@data-qa='privacy-continue']"
    FIRST_NAME_INPUT = "//input[@data-qa='personal-first-name']"
    LAST_NAME_INPUT = "//input[@data-qa='personal-last-name']"
    EMAIL_INPUT = "//input[@data-qa='personal-email']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = self.locator("//*[@class='title-2 text-ellipsis']")

    def fill_personal_data(self, personal_data: dict):
        frame = self.page.wait_for_selector(DonatFrame.WIDGET_LOCATOR)
        frame_handler = frame.content_frame()
        with allure.step(f"Fill First mame: {personal_data['first_name']}"):
            frame_handler.locator(self.FIRST_NAME_INPUT).fill(personal_data['first_name'])
        with allure.step(f"Fill Last mame: {personal_data['last_name']}"):
            frame_handler.locator(self.LAST_NAME_INPUT).fill(personal_data['last_name'])
        with allure.step(f"Fill email: {personal_data['email']}"):
            frame_handler.locator(self.EMAIL_INPUT).fill(personal_data['email'])
        frame_handler.locator(self.DONATE_BUTTON).click()
