from appium import webdriver


def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '9f4bd427'
    desired_caps['appPackage'] = 'llbt.ccb.ynga'
    desired_caps['appActivity'] = 'com.ccb.fintech.app.productions.ynga.ui.starter.StartPageActivity'
    desired_caps['automationName'] = 'uiautomator2'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
