import time
import yaml
import pytest
import allure
from base.base_driver import init_driver
from page.page import Page
from base.base_action import BaseAction
from base.base_analyze import analyze_file
from base.base_analyze import read_excel_sheet_row_data
from base.base_analyze import save_excel_sheet

matter_list = read_excel_sheet_row_data()
normal = "正常"
fail = "失败"
print("=======================================================本次巡检事项===================================================")
print(matter_list)


@allure.feature('top10功能')
class TestTop10:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    @pytest.mark.skipif('公积金信息查询' not in matter_list, reason="skip")
    def test_top1(self, args):
        try:
            matter = "公积金信息查询"
            # 解析yaml数据
            username = args["username"]
            password = args["password"]
            # #选择体验，启动向导save_docx
            # self.page.start.skip_start()
            self.page.home.checkTopByNameFromMoreService(matter)
            # 如果未登陆则登陆,再点击
            try:
                self.page.login.confirm_login(username, password)
                time.sleep(3)
                # 公积金信息查询
                self.page.home.checkTopByNameFromMoreService(matter)
            except Exception:
                pass
            # time.sleep(6)
            # 退回主页面
            # self.driver.find_element_by_id("llbt.ccb.ynga:id/backbtn").click()
            # time.sleep(1)
            save_excel_sheet(2, matter_list, matter, normal, "")
        except Exception:
            save_excel_sheet(2, matter_list, matter, fail, "开小差")
            assert False

    @pytest.mark.skipif('查城镇职工养老保险缴费' not in matter_list, reason="skip")
    def test_top2(self):
        try:
            matter = "查城镇职工养老保险缴费"
            self.page.home.checkTopByNameFromMoreService(matter)
            save_excel_sheet(2, matter_list, matter, normal, "")
        except Exception:
            save_excel_sheet(2, matter_list, matter, fail, "开小差")
            assert False

    # @pytest.mark.skipif('公积金明细查询' not in matter_list, reason="skip")
    # def test_top3(self):
    #     try:
    #         matter = "公积金明细查询"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('事业单位招聘' not in matter_list, reason="skip")
    # def test_top4(self):
    #     try:
    #         matter = "事业单位招聘"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Excetion:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('查重名' not in matter_list, reason="skip")
    # def test_top5(self):
    #     try:
    #         matter = "查重名"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Excetion:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('查行政区划' not in matter_list, reason="skip")
    # def test_top6(self):
    #     try:
    #         matter = "查行政区划"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Excetion:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('行驶证二维码' not in matter_list, reason="skip")
    # def test_top7(self):
    #     try:
    #         matter = "行驶证二维码"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('律师律所查询' not in matter_list, reason="skip")
    # def test_top8(self):
    #     try:
    #         matter = "律师律所查询"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('查出入境业务办理进度' not in matter_list, reason="skip")
    # def test_top9(self):
    #     try:
    #         matter = "查出入境业务办理进度"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
    #
    # @pytest.mark.skipif('驾驶证二维码' not in matter_list, reason="skip")
    # def test_top10(self):
    #     try:
    #         matter = "驾驶证二维码"
    #         self.page.home.checkTopByNameFromMoreService(matter)
    #         save_excel_sheet(2, matter_list, matter, normal, "")
    #     except Exception:
    #         save_excel_sheet(2, matter_list, matter, fail, "开小差")
    #         assert False
