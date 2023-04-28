from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

import os
import _thread
import time

def run_appium():
    os.system('appium -a localhost -p 4723')


_thread.start_new_thread(run_appium, ())
time.sleep(15)

desired_caps = {
  'platformName': 'Android',                        # 连接设备为安卓系统
  'platformVersion': '9',                           # 手机安卓版本,必须与设备匹配
  'deviceName': 'emulator-5554 device',             # 设备名，cmd中使用 adb devices命令查看
  'appPackage': 'tv.danmaku.bili',                  # 启动APP Package名称
  'appActivity': 'tv.danmaku.bili.MainActivityV2',  # 启动Activity名称
  'unicodeKeyboard': True,                          # 使用自带输入法，输入中文时填True
  'resetKeyboard': True,                            # 执行完程序恢复原来输入法
  'noReset': True,                                  # 不重置App
  'newCommandTimeout': 10000,	                    # APP默认自动一分钟后关闭，开启可以延长
  # 'automationName': 'UiAutomator2',	# 获取toast信息弹出框需添加，但需要先配置UiAutomator2
  # 'app': r'd:\apk\bili.apk',	# 测试apk包的路径，如果有了app就不需要APP Package和Activity，反理同之
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(20)

# 如果有`青少年保护`界面，点击`我知道了`
try:
    iknow = driver.find_element(By.ID, 'text3')
    if iknow:
        print('Adolescent protect found!')
        iknow.click()
except:
    print('Adolescent protect not found!')

# 根据id定位搜索位置框，点击
print('Looking for search frame')
driver.find_element(By.ID, ('expand_search')).click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element(By.ID, ('search_src_text'))
sbox.send_keys('混剪视频')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
titles = driver.find_elements(By.ID, 'title')

for title in titles:
    # 打印标题
    print(title.text)
