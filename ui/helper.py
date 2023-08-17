import random
import string
import allure

from playwright.sync_api import Page


def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def make_failure_screenshot(page: Page):
    allure.attach(page.page.screenshot(type="png"), name="allure-report/failure",
                  attachment_type=allure.attachment_type.PNG)
