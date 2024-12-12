from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")


    def open_home_page(self, url="https://useinsider.com/"):
        self.open_url(url)

    def click_company_and_careers(self):
        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)
