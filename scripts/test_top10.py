import time
import yaml
import pytest
from base.base_driver import init_driver
from page.page import Page
from base.base_action import BaseAction
from base.base_analyze import analyze_file


class TestTop10():

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    # def test_top1(self,args):
    #     # 解析yaml数据
    #     username = args["username"]
    #     password = args["password"]
    #     # 选择体验，启动向导
    #     # self.page.start.skip_start()
    #     self.checkTopByName("公积金信息查询")
    #     # 如果未登陆则登陆,再点击
    #     try:
    #         self.page.login.confirm_login(username, password)
    #         time.sleep(3)
    #         # 公积金信息查询
    #         self.driver.find_element_by_xpath("//*[@text='公积金信息查询']").click()
    #     except Exception:
    #         pass
    #     time.sleep(6)
    #     # 退回主页面
    #     self.driver.find_element_by_id("llbt.ccb.ynga:id/backbtn").click()
    #     time.sleep(1)
    #
    # def test_top2(self):
    #     self.checkTopByName("查城镇职工养老保险缴费")
    #
    # def test_top3(self):
    #     self.checkTopByName("公积金明细查询")
    #
    # def test_top4(self):
    #     self.checkTopByName("事业单位招聘")
    #
    # def test_top5(self):
    #     self.checkTopByName("查重名")
    #
    # def test_top6(self):
    #     self.checkTopByName("查行政区划")
    #
    # def test_top7(self):
    #     self.checkTopByName("行驶证二维码")
    #
    # def test_top8(self):
    #     self.checkTopByName("律师律所查询")

    def test_top9(self):
        self.checkTopByName("查出入境业务办理进度")

    # def test_top10(self):
    #     self.checkTopByName("驾驶证二维码")

    def checkTopByName(self,text):
        time.sleep(3)
        # 更多服务
        self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_name44").click()
        time.sleep(3)
        self.find_matter_with_slide("//*[@text='"+text+"']")
        time.sleep(6)

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)


    def swipeDown(self):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        y2 = int(l[1] * 0.1)
        time.sleep(1)
        self.driver.swipe(x1, y1, x1, y2)

    def back_to_top(self):
        count = 0
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[1] * 0.9)
        time.sleep(1)
        while count < 5:
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(3)
            count += 1

    def find_matter_with_slide(self, element):
        while True:
            try:
                self.driver.find_element_by_xpath(element).click()
                break
            except Exception:
                self.swipeDown()