import allure
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser-choice", choices=["webkit", "chromium", "firefox"], default="chromium", help="Browser choice")
    parser.addoption("--device-type", choices=["desktop", "iphone"], default="desktop", help="Device type")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@allure.title("Open browser incognito")
@pytest.fixture(scope="function")
def incognito(request):
    browser_choice = request.config.getoption("--browser-choice")
    device_type = request.config.getoption("--device-type")
    headless_mode = request.config.getoption("--headless")

    with sync_playwright() as playwright:
        if browser_choice == "webkit":
            browser = playwright.webkit.launch(headless=headless_mode)
        elif browser_choice == "chromium":
            browser = playwright.chromium.launch(headless=headless_mode)
        elif browser_choice == "firefox":
            browser = playwright.firefox.launch(headless=headless_mode)

        if device_type == "desktop":
            context = browser.new_context()
        elif device_type == "iphone":
            iphone_13 = playwright.devices['iPhone 13']
            context = browser.new_context(**iphone_13)
        page = context.new_page()
        yield page
        browser.close()
