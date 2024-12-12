from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_element_clickable(locator).click()

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def open_url(self, url):
        self.driver.get(url)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def accept_cookies_if_present(self):
        try:
            # Adjust the locator strategy as needed
            accept_button_locator = (By.ID, "wt-cli-accept-all-btn")

            # Wait a short time for the cookie banner to appear, if it doesn't appear, move on
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(accept_button_locator)
            )

            accept_button = self.driver.find_element(*accept_button_locator)
            accept_button.click()
        except:
            # If the cookie banner does not appear, just continue
            pass
