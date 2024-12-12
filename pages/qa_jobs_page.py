from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class QAJobsPage(BasePage):
    SEE_ALL_QA_JOBS_BUTTON = (By.LINK_TEXT, "See all QA jobs")
    FILTER_DEPARTMENT = (By.ID, "select2-filter-by-department-container")
    FILTER_LOCATION = (By.ID, "select2-filter-by-location-container")
    JOB_LISTINGS = (By.CSS_SELECTOR, "div.position-list-item")
    VIEW_ROLE_BUTTON = (By.XPATH, ".//a[contains(text(), 'View Role')]")

    def open_page(self, url="https://useinsider.com/careers/quality-assurance/"):
        self.open_url(url)
        self.accept_cookies_if_present()

    def click_see_all_jobs(self):
        self.click(self.SEE_ALL_QA_JOBS_BUTTON)

    def wait_for_filter_to_complete(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return typeof jQuery === 'undefined' || jQuery.active === 0")
        )

    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        # Wait until department is automatically set to "Quality Assurance"
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "select2-filter-by-department-container"), department)
        )

        # Click location filter to open dropdown
        self.click(self.FILTER_LOCATION)

        # Wait for the location option to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//li[contains(@class, 'select2-results__option') and text()='{location}']"))
        )
        # Select the location from the dropdown
        location_option = self.find_element(
            (By.XPATH, f"//li[contains(@class, 'select2-results__option') and text()='{location}']"))
        location_option.click()


    def verify_jobs_listed(self):
        jobs = self.find_elements(self.JOB_LISTINGS)
        assert len(jobs) > 0, "No jobs found after filtering!"
        return jobs

    def verify_jobs_details(self, jobs, position,department, location):
        for job in jobs:
            pos = job.find_element(By.CSS_SELECTOR, ".position-title").text
            dep = job.find_element(By.CSS_SELECTOR, ".position-department").text
            loc = job.find_element(By.CSS_SELECTOR, ".position-location").text

            # Check that the required text is contained in each field
            assert ( position in pos or "QA" in pos), f"Position does not contain '{position}' or 'QA': {pos}"
            assert department in dep, f"Department does not contain '{department}': {dep}"
            assert location in loc, f"Location does not contain '{location}': {loc}"

    def click_view_role(self):
        # Find the first job element
        jobs = self.find_elements(self.JOB_LISTINGS)
        if not jobs:
            raise Exception("No job listings found.")
        first_job = jobs[0]

        # Hover over the job element’s wrapper
        wrapper = first_job.find_element(By.CSS_SELECTOR, ".position-list-item-wrapper.bg-light")
        ActionChains(self.driver).move_to_element(wrapper).perform()

        # Once hovered, the "View Role" button should be visible; now click it
        view_role_btn = wrapper.find_element(*self.VIEW_ROLE_BUTTON)
        view_role_btn.click()
