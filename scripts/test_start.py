import time
import yaml
import pytest
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file


class TestStart:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    def test_start(self):
        #选择体验，启动向导
        self.page.start.skip_start()

    def test_area(self,args):
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

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_jiankangma(self,args):
        # 解析yaml数据
        username = args["username"]
        password = args["password"]
        time.sleep(6)
        # 健康码
        self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_name1").click()
        #如果未登陆则登陆,再点击
        try:
            self.page.login.confirm_login(username,password)
            time.sleep(3)
            # 健康码
            self.driver.find_element_by_id("llbt.ccb.ynga:id/tv_name1").click()
        except Exception:
            pass
        time.sleep(5)


