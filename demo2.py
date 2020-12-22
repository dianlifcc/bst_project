import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HelloWorld(unittest.TestCase):
    def test_enterFilter(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '9f4bd427'
        desired_caps['appPackage'] = 'llbt.ccb.ynga
        desired_caps['appActivity'] = 'com.ccb.fintech.app.productions.ynga.ui.starter.StartPageActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver.implicitly_wait(5)

        # 向左滑动跳过引导页
        x = 0
        while x < 3:
            self.swipeLeft()
            x += 1
        enterApp = self.driver.find_element_by_id("llbt.ccb.ynga:id/bt_appstart_skip")
        enterApp.click()
        #同意
        number = 3
        for i in range(number):
            loc=("xpath","//*[@text='同意']")
        try:
            WebDriverWait(self.driver,1,0.5).until(EC.presence_of_all_elements_located(loc)).click()
        except:
            pass
        time.sleep(2)
        # self.driver.find_element_by_xpath("//*[@text='同意']").click()
        # self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_agree").click()
        # 点击左上角地区
        driver.find_element_by_id("llbt.ccb.ynga:id/ll").click()
        time.leep(3)
        # 昆明市
        driver.find_element_by_name("昆明市").click()
        time.sleep(2)
        driver.find_element_by_name("盘龙区").click()
        time.sleep(1)
        driver.find_element_by_name("确认").click()
        time.sleep(1)
        # 健康码
        driver.find_element_by_id("llbt.ccb.ynga:id/tv_name1").click()
        time.sleep(10)



    # 获取屏幕宽度和高度
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
        time.sleep(1)
        self.driver.swipe(x1, y1, x2, y1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
