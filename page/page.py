from page.login_page import LoginPage
from page.start_page import StartPage


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def start(self):
        return StartPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)