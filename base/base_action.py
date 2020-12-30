from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def click_tab(self, feature,index):
        self.find_elements(feature)[index].click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    def skip_start(self):
        # 选择体验
        appstart = By.ID, "llbt.ccb.ynga:id/bt_appstart_skip"
        # 同意
        agree = By.ID, "llbt.ccb.ynga:id/tv_agree"

        # # 华为-设备信息权限
        # allow = By.XPATH,"//*[@text='始终允许']"

        # time.sleep(2)
        # # 华为-设备信息权限
        # try:
        #     # 华为-设备照片、文件权限
        #     self.click(allow)
        # except Exception:
        #     #不是华为的跳过
        #     pass
        # time.sleep(2)
        for i in range(3):
            time.sleep(3)
            self.scroll_page_one_time("left")
        # 选择体验，启动向导
        self.click(appstart)
        # time.sleep(2)
        # try:
        #     # 华为-设备照片、文件权限
        #     self.click(allow)
        # except Exception:
        #     # 不是华为的跳过
        #     pass
        #同意
        time.sleep(6)
        self.click(agree)


    """
    未登陆会弹框确定登陆
    :param username&password：用户名密码
    """
    def click_confirm_login(self,username,password):
        # 用户名
        username_edit_text = By.XPATH, "//*[@text='手机号码/用户名/身份证号']"
        # 密码
        password_edit_text = By.XPATH, "//*[@text='请输入登录密码']"

        # 登录
        login_button = By.XPATH, "//*[@text='登录']"

        # 确定登录弹框
        confirm_login_button = By.XPATH, "//*[@text='确定']"
        time.sleep(1)
        try:
            self.click(confirm_login_button)
            # 登录
            try:
                # 如果用户名不为空,有缓存，没有获取到元素会抛异常
                self.input(username_edit_text, username)
            except Exception:
                pass
            self.input(password_edit_text, password)
            self.click(login_button)
            time.sleep(6)
        except Exception:
            pass


    """
    根据部分内容，判断toast是否存在
    :param message：部分内容
    :return 是否存在
    """
    def is_toast_exist(self,message):
        message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message
        try:
            self.find_element(message_xpath,5,0.1)
            return True
        except TimeoutException:
            return False

    """
    根据部分内容，判断toast上的所有内容
    :param message：部分内容
    :return 所有内容
    """
    def get_toast_exist(self,message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath,5,0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    def scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param direction:方向
        "up"：从下往上
        "down"：从上往下
        "left"：从右往左
        "down"：从左往右
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2
        left_x = width / 10 * 1
        left_y = center_y
        right_x = width / 10 * 9
        right_y = center_y
        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 1000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找某个元素的特征
        :param feature:元素的特征
        :param direction:方向
        "up"：从下往上
        "down"：从上往下
        "left"：从右往左
        "down"：从左往右
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source