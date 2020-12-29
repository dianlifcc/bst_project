from appium import webdriver

def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '9f4bd427'
    desired_caps['appPackage'] = 'llbt.ccb.ynga'
    desired_caps['appActivity'] = 'com.ccb.fintech.app.productions.ynga.ui.starter.StartPageActivity'
    #toast
    desired_caps['automationName'] = 'Uiautomator2'
    #是否重置应用True:不重置 False：重置,没有登录状态
    desired_caps['noReset'] = no_reset

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
