from typing import Optional
import allure

from playwright.sync_api import Page, expect
from consts.consts import BASE_URL, DONAT_QUERY
from ui.pages.base_page import BasePage


class DonatFrame(BasePage):
    URL = BASE_URL + DONAT_QUERY
    WIDGET_LOCATOR = "//iframe[@title='Donation Widget']"
    MONTHLY_BUTTON = "//*[@data-qa='more-frequent-button']"
    ONCE_BUTTON = "//*[@data-qa='less-frequent-button']"
    AMOUNT_BUTTONS = "//*[@data-qa='suggested-amount-button']"
    CONFIRM_BUTTON = "//*[@data-qa='donate-button']"
    COVER_FEE_CHECKBOX = "//*[@data-qa='cover-fee-checkbox']"
    CREDIT_CARD = "//*[@data-qa='cc-button']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = self.locator("//*[@data-qa='ask-title']")

    def choose_donation(self, regularity: Optional[str] = None, amount: Optional[str] = None):
        donat_frame = self.page.wait_for_selector(DonatFrame.WIDGET_LOCATOR)
        frame = donat_frame.content_frame()
        with allure.step("Choose regularity of payment"):
            regularity = frame.locator(self.MONTHLY_BUTTON) if regularity == "monthly" else frame.locator(self.ONCE_BUTTON)
            regularity.click()
        with allure.step("Choose amount of payment or use default value and confirm"):
            if amount is not None:
                chosen_amount = frame.locator(self.AMOUNT_BUTTONS).locator(f"//*[@title='€{amount}']")
                chosen_amount.click()
                expect(chosen_amount).to_be_checked()
            frame.locator(self.CONFIRM_BUTTON).click()









