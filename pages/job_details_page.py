from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobDetailsPage(BasePage):

    def verify_lever_form_page(self):
        # Store the current window handle
        original_window = self.driver.current_window_handle

        # Wait until a new window is opened (there should be exactly 2 tabs)
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        # Now we are in the new tab. Wait for the page to load completely.
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Verify URL contains lever.co (or use a unique element on Lever page)
        assert "lever.co" in self.driver.current_url, "Did not redirect to Lever application form page"

        # Optionally, you can check for a unique element on the Lever form
        # For example, Lever's job application pages often have an element like:
        # <div class="lever-application-form"> or a unique form container
        # If needed, uncomment and adjust the locator below:
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".lever-application-form"))
        # )
