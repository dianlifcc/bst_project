from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class RegisterPage(BaseAction):

    #未登录
    login_button = By.XPATH,"//*[@text='点击登录']"

    #点击 去登录
    def click_login(self):
        self.click(self.login_button)