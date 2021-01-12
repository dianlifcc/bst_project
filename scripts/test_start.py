import time
import yaml
import pytest
import allure
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file
from base.base_analyze import read_excel_sheet_row_data
from base.base_analyze import save_excel_sheet
from base.base_analyze import save_docx


matter_list = read_excel_sheet_row_data()
normal = "正常"
fail = "失败"
print("TestStart:================")
print(matter_list)

@allure.feature('启动-首页选择地区-健康码功能')
class TestStart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @allure.story('启动并登录')
    # @pytest.mark.skipif('启动并登录' in matter_list, reason="skip")
    # def test_start(self):
    #     #选择体验，启动向导
    #     self.page.start.skip_start()
    #     # self.page.home.login_if_not(self.page)
    #     save_docx("test")

    # @allure.story('首页 左上角选择地区')
    # @pytest.mark.skipif('首页-地区选择' not in matter_list, reason="skip")
    # def test_area(self):
    #     time.sleep(6)
    #     try:
    #         matter = "首页-地区选择"
    #         # 点击左上角地区
    #         self.page.home.clickArea()
    #         save_excel_sheet(1, matter_list, matter, normal,"")
    #     except Exception:
    #         save_excel_sheet(1, matter_list, matter, fail,"开小差")
    #         assert False

    @allure.story('首页-搜索栏')
    @pytest.mark.skipif('首页-搜索栏' not in matter_list, reason="skip")
    def test_area(self):
        time.sleep(6)
        try:
            matter = "首页-搜索栏"
            # 点击左上角地区
            self.page.home.clickHomeSearch("公积金密码找回")
            save_excel_sheet(1, matter_list, matter, normal,"")
        except Exception:
            save_excel_sheet(1, matter_list, matter, fail,"开小差")
            assert False


    # @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    # @allure.story('首页 云南健康码')
    # @pytest.mark.skipif('云南健康码' not in matter_list, reason="skip")
    # def test_jiankangma(self,args):
    #     try:
    #         matter = "云南健康码"
    #         # 解析yaml数据
    #         username = args["username"]
    #         password = args["password"]
    #         realname = args["realname"]
    #         time.sleep(6)
    #         # 健康码
    #         self.page.home.clickJangKangMa()
    #         #如果未登陆则登陆,再点击
    #         try:
    #             self.page.login.confirm_login(username,password)
    #             time.sleep(3)
    #             # 健康码 云南健康码
    #             self.page.home.clickJangKangMa()
    #         except Exception:
    #             pass
    #         #“付聪聪”是否在page_source中
    #         if self.page.start.is_keyword_in_page_source(realname):
    #             save_excel_sheet(2, matter_list, matter, normal, "")
    #         else:
    #             save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False


