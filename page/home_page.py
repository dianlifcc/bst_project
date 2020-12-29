from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class HomePage(BaseAction):

    #我的
    me_button = By.ID,"llbt.ccb.ynga:id/iv_tab_icon"
    # 未登录显示"点击登录"
    no_login_button = By.XPATH, "//*[@text='点击登录']"

    #点击我的
    def click_me(self):
        self.click_tab(self.me_button,3)

    def login_if_not(self,page):
        #判断登录状态
        self.click_me()
        try:
            self.find_element(self.no_login_button)
            # 没有登录，就去登录
            # 点击登录
            page.register.click_login()
            # 输入用户名
            page.login.input_username("15198938874")
            # 输入密码
            page.login.input_password("Birdfcc12345")
            # 登录
            page.login.click_login()
        except Exception:
            pass



