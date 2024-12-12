from .base_page import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):
    CAREER_OUR_LOCATION_SECTION = (By.ID, "career-our-location")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//h2[text()='Life at Insider']")
    QUALITY_ASSURANCE_LINK = (By.XPATH, "//h3[contains(text(), 'Quality Assurance')]//ancestor::a")

    def verify_page_sections(self):
        assert self.find_element(self.CAREER_OUR_LOCATION_SECTION).is_displayed(), "Locations section not visible"
        assert self.find_element(self.TEAMS_SECTION).is_displayed(), "Teams section not visible"
        assert self.find_element(self.LIFE_AT_INSIDER_SECTION).is_displayed(), "Life at Insider section not visible"

    def go_to_quality_assurance_page(self):
        self.click(self.QUALITY_ASSURANCE_LINK)
