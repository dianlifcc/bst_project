from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class StartPage (BaseAction):
    #选择体验
    appstart = By.ID,"llbt.ccb.ynga:id/bt_appstart_skip"
    # 同意
    agree = By.ID, "llbt.ccb.ynga:id/tv_agree"

    #跳过向导
    @allure.step(title='向导页点击选择体验')
    def click_start(self):
        self.click(self.appstart)

    #同意
    @allure.step(title='首页点击同意')
    def click_agree(self):
        self.click(self.agree)
