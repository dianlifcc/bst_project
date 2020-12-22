from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

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
        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
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
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)

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