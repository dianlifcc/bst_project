from page.login_page import LoginPage
from page.start_page import StartPage
from page.home_page import HomePage
from page.register_page import RegisterPage
from page.me_page import MePage

class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def start(self):
        return StartPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

