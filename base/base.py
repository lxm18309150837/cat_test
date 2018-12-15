"""
公共方法: 卡乐猫进入我的页面,点击登录,输入账号
    1.点击
    2.输入
    3.定位

"""
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    # 封装定位方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
       return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 封装输入方法
    def base_input(self,loc,value):
        ele = self.base_find_element(loc)
        ele.clear()
        ele.send_keys(value)

    # 封装点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()