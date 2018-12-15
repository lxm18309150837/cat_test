from appium import webdriver


def get_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = '192.168.125.101:5555'
    # APP包名
    desired_caps['appPackage'] = 'com.kalemao.thalassa'
    desired_caps['appActivity'] = '.ui.main.MainActivity'



    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)




