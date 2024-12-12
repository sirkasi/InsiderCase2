import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from datetime import datetime
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name.lower() == 'chrome':
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        # Block notifications
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    elif browser_name.lower() == 'firefox':
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        firefox_options = FirefoxOptions()
        # Disable notifications
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

    else:
        raise ValueError("Unsupported browser!")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook for taking screenshot on failure
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "browser" in item.fixturenames:
            web_driver = item.funcargs['browser']
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_file = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            web_driver.save_screenshot(screenshot_file)
