from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class MePage(BaseAction):

    #姓名
    my_name_text_view = By.ID,"llbt.ccb.ynga:id/tv_mine_name"

    def get_my_name_text(self):
        return self.find_element(self.my_name_text_view).text
