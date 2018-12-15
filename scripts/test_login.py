import os
import sys
sys.path.append(os.getcwd())

import time

import pytest

from base.get_catdriver import get_driver
from page.page_login import PageLogin



from base.read_data import ReadData



def get_data():
    list = []
    for data in ReadData("data.yaml").raad_data().values():
        list.append((data.get("username"), data.get("password")))
    return list


class TestLogin():
    # 实例化
    def setup_class(self):
        self.login = PageLogin(get_driver())


    # 关闭app
    def teardown_class(self):
        self.login.driver.quit()
        time.sleep(3)

    @pytest.mark.parametrize("username,password",[("18309150000","123456")])
    # 输入用户名.密码.点击登录
    def test_login(self, username, password):
        self.login.page_click_me()  # 点击我的
        self.login.page_click_login()  # 点击登录按钮
        self.login.page_click_phone()  # 点击手机号登录
        self.login.page_input_user(username)  # 输入手机号
        self.login.page_input_pwd(password)  # 输入密码
        self.login.page_click_btn()  # 点击按钮
if __name__ == '__main__':
    pytest.main()