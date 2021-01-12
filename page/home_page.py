from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
import time
import os

class HomePage(BaseAction):

    #我的
    me_button = By.ID,"llbt.ccb.ynga:id/iv_tab_icon"
    # 未登录显示"点击登录"
    no_login_button = By.XPATH,"//*[@text='点击登录']"
    #更多服务
    moreservice = By.ID,"llbt.ccb.ynga:id/tv_name44"
    #云南健康码
    jiankangma = By.ID,"llbt.ccb.ynga:id/tv_name1"
    #选择地区
    area =  By.ID,"llbt.ccb.ynga:id/ll"

    km_area = By.XPATH,"//*[@text='昆明市']"
    wh_area = By.XPATH,"//*[@text='五华区']"
    quereng = By.XPATH,"//*[@text='确认']"

    #首页-搜索
    home_search = By.ID,"llbt.ccb.ynga:id/tv_serarch"
    home_search_input = By.XPATH,"//*[@text='请输入关键字搜索']"

    #点击我的
    @allure.step(title='主页点击我的')
    def click_me(self):
        self.click_tab(self.me_button,3)

    @allure.step(title='主页登录（如果没有登录的话）')
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
            page.login.input_password("Birdfcc@12345")
            # 登录
            page.login.click_login()
        except Exception:
            pass

    @allure.step(title='点击首页-搜索')
    def clickHomeSearch(self,content):
        keyword = By.XPATH, "//*[@text='" + content + "']"
        keyword2 = By.XPATH, "//*[@text='搜索']"

        time.sleep(2)
        self.click(self.home_search)
        os.system('adb shell ime set com.sohu.inputmethod.sogou.vivo/.SogouIME')
        self.find_element_with_scroll(self.home_search_input).click()
        time.sleep(2)
        self.input(self.home_search_input, content)

        time.sleep(2)
        self.find_element_with_scroll(keyword).click()


        time.sleep(2)
        self.driver.press_keycode(66)
        time.sleep(2)
        self.driver.press_keycode(66)
        # self.driver.press_keycode(66)
        # self.find_element_with_scroll(keyword).click()
        # self.driver.press_keycode(66)
        time.sleep(3)

    @allure.step(title='从主页更多服务进入')
    def clickJangKangMa(self):
        self.click(self.jiankangma)

    @allure.step(title='选择地区')
    def clickArea(self):
        self.click(self.area)
        time.sleep(4)
        # 昆明市
        self.find_element(self.km_area).click()
        time.sleep(3)
        self.find_element(self.wh_area).click()
        time.sleep(2)
        self.find_element(self.quereng).click()

    def checkTopByNameFromMoreService(self, text):
        topname = By.XPATH, "//*[@text='" + text + "']"
        time.sleep(3)
        # 更多服务
        self.click(self.moreservice)
        time.sleep(3)
        self.find_element_with_scroll(topname).click()
        time.sleep(6)

    @allure.step(title='获取toast内容')
    def get_toast_text(self,name):
        topname = By.XPATH, "//*[@text='" + name + "']"
        return self.find_element(topname).text


