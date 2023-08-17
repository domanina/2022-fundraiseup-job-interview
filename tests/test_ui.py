import allure

from playwright.sync_api import expect
from tests.consts import NEGATIVE_CARD_DATA, TEST_PERSONAL_DATA
from ui.helper import make_failure_screenshot
from ui.pages.credit_card_page import CreditFrame
from ui.pages.donation_page import DonatFrame
from ui.pages.personal_info_page import PersonalFrame
from ui.pages.start_page import StartPage


@allure.label("negative scenario")
class TestElements:
    @allure.title("Get user verification error")
    def test_check_negative_case(self, incognito):
        with allure.step("Go to start page and click on donat button"):
            page = StartPage(incognito).goto()
            page.donat_button.click()
        with allure.step("Make sure page has right url"):
            expect(page.page).to_have_url(DonatFrame.URL)
        with allure.step("Choose monthly pay and 100$ donat"):
            donat_page = DonatFrame(incognito)
            donat_page.choose_donation("monthly", "100")
        with allure.step("Uncheck cover fee box"):
            donat_frame = donat_page.page.wait_for_selector(DonatFrame.WIDGET_LOCATOR)
            frame = donat_frame.content_frame()
            checkbox = frame.locator(DonatFrame.COVER_FEE_CHECKBOX)
            checkbox.uncheck()
            expect(checkbox, make_failure_screenshot(page)).to_have_attribute("aria-checked", "false")
            expect(frame.locator("//*[@class='subtitle-1 text-sans-serif flex-shrink-0']"),
                   make_failure_screenshot(page)).to_have_text("100")
        with allure.step("Choose payment by credit card"):
            frame.locator(DonatFrame.CREDIT_CARD).click()
        with allure.step("Fill credit card data"):
            credit_page = CreditFrame(incognito)
            credit_page.fill_card_data(frame, NEGATIVE_CARD_DATA)
        with allure.step("Fill personal data"):
            personal_page = PersonalFrame(incognito)
            personal_page.fill_personal_data(TEST_PERSONAL_DATA)
        with allure.step("Make sure got error - Your card has been declined"):
            expect(frame.locator("//*[contains(text(), 'Your card has been declined')]"),
                   make_failure_screenshot(page)).to_be_visible()
        # TODO check info in db
