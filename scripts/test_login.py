import time
import yaml
import pytest
import allure
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file

@allure.feature('登录功能')
class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    @allure.story('首页 我的 登录')
    def test_login(self,args):
        #解析yaml数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        realname = args["realname"]

        self.page.start.skip_start()

        time.sleep(2)
        self.page.home.click_me()
        self.page.register.click_login()
        # 登录
        try:
           #如果用户名不为空,有缓存，没有获取到元素会抛异常
           self.page.login.input_username(username)
        except Exception:
            pass
        self.page.login.input_password(password)
        self.page.login.click_login()
        if toast is None:
            assert self.page.me.get_my_name_text() == realname,"登录后的用户名和输入的用户名不一致"
        else:
            #找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            self.page.login.is_toast_exist(toast)



#allure generate report/ -o report/html --clean
#pytest --html=./report/report.html --self-contained-html
#hrnecrerpkftbjih
