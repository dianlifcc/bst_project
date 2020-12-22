import time
from base.base_driver import init_driver
from page.page import Page


class TestStart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_start(self):
        time.sleep(2)
        while True:
            try:
                self.page.start.click_start()
                break
            except Exception:
                self.swipeLeft()
        # 向左滑动跳过引导页
        # x = 0
        # while x < 3:
        #     self.swipeLeft()
        #     x += 1
        # #选择体验，启动向导
        # self.page.start.click_start()
        # 同意
        time.sleep(5)
        self.page.start.click_agree()
        time.sleep(6)
        # 点击左上角地区
        self.driver.find_element_by_id("llbt.ccb.ynga:id/ll").click()
        time.sleep(4)
        # 昆明市
        self.driver.find_element_by_xpath("//*[@text='昆明市']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='五华区']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='确认']").click()
        time.sleep(4)
        # 健康码
        self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_name1").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        time.sleep(2)
        #登录
        self.page.login.input_username("15198938874")
        self.page.login.input_password("改自己的密码")
        self.page.login.click_login()
        time.sleep(6)
        # 健康码
        self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_name1").click()
        time.sleep(6)
        # self.driver.find_element_with_scroll((By.XPATH, "//*[@text='提交']")).click()
        # time.sleep(4)
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 向左滑动

    def swipeLeft(self):

        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y1)