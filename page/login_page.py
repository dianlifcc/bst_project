from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class LoginPage (BaseAction):
    #用户名
    username_edit_text = By.XPATH,"//*[@text='手机号码/用户名/身份证号']"
    #密码
    password_edit_text = By.XPATH,"//*[@text='请输入登录密码']"

    #登录
    login_button = By.XPATH,"//*[@text='登录']"

    # 登录
    login_button = By.XPATH, "//*[@text='登录']"

    # 确定登录弹框
    confirm_login_button = By.XPATH, "//*[@text='确定']"

    #输入用户名
    @allure.step(title='输入用户名')
    def input_username(self,text):
        self.input(self.username_edit_text,text)
    #输入密码
    @allure.step(title='输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)
    #点击登录
    @allure.step(title='点击登录')
    def click_login(self):
        self.click(self.login_button)

    def confirm_login(self,username,password):
        self.click_confirm_login(username,password)