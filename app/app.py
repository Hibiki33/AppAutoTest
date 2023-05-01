from appium import webdriver
import os

class App(object):

    def __init__(self, 
            device_name='emulator-5554 device', 
            app_name='tv.danmaku.bili', 
            apk_path='./App/iBiliPlayer-bili.apk'):
        self.device_name = device_name
        self.app_name = app_name
        self.apk_path = apk_path
        self.adb_connect()

    def adb_connect(self): 
        devices = os.popen("adb devices")
        device_list = devices.read()

        if self.device_name not in device_list:
            self.connection_equipment() 
        
    def connection_equipment(self):
        os.system("adb connect {}".format(self.device_name))

    def app_direct_install(self):  
        install = os.popen("adb install {}".format(self.apk_path))  
        if install.read():
            print('Direct Installed', self.apk_path)     

    def app_replace_install(self): 
        install = os.popen("adb install -r {}".format(self.apk_path)) 
        if install.read():
            print('Replace Installed', self.apk_path)
            
    def app_uninstall(self):
        uninstall = os.popen("adb uninstall {}".format(self.app_name))
        if uninstall.read():
            print('Uninstall', self.app_name)


if __name__ == '__main__':
    bilibili = App()
    bilibili.app_direct_install()
    bilibili.app_uninstall()
