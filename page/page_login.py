import page
from base.base import Base


class PageLogin(Base):
    # 定位我的
    def page_click_me(self):
        self.base_click(page.loc_me)

    # 定位登录
    def page_click_login(self):
        self.base_click(page.loc_login)

    # 定位使用手机号注册
    def page_click_phone(self):
        self.base_click(page.loc_phone)

    # 输入手机号
    def page_input_user(self,username):
        self.base_input(page.loc_iphone,username)

    # 输入密码
    def page_input_pwd(self,password):
        self.base_input(page.loc_pwd,password)

    # 点击登录
    def page_click_btn(self):
        self.base_click(page.loc_btn)