from playwright.sync_api import Page, Frame
from ui.pages.base_page import BasePage


class CreditFrame(BasePage):
    WIDGET_LOCATOR = "//iframe[contains(@name, 'privateStripeFrame')]"
    CONTINUE_BUTTON = "//*[@data-qa='card-continue']"
    CREDIT_CARD = "//*[@data-qa='cc-button']"
    CARD_NUMBER_INPUT = "//input[@data-elements-stable-field-name='cardNumber']"
    CARD_EXPIRY_INPUT = "//input[@data-elements-stable-field-name='cardExpiry']"
    CARD_CVC_INPUT = "//input[@data-elements-stable-field-name='cardCvc']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = self.locator("//*[@class='title-2 text-ellipsis']")

    def fill_card_data(self, parent_frame: Frame, card_data: dict):
        child_frames = parent_frame.child_frames
        for frame in child_frames:
            if frame.locator(self.CARD_NUMBER_INPUT).is_visible():
                frame.locator(self.CARD_NUMBER_INPUT).fill(card_data["number"])
            if frame.locator(self.CARD_EXPIRY_INPUT).is_visible():
                frame.locator(self.CARD_EXPIRY_INPUT).fill(card_data["expire"])
            if frame.locator(self.CARD_CVC_INPUT).is_visible():
                frame.locator(self.CARD_CVC_INPUT).fill(card_data["cvc"])
        parent_frame.locator(self.CONTINUE_BUTTON).click()
