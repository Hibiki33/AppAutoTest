import os
from common.read_json import get_json_value, get_desired_caps

class App(object):

    def __init__(self, app_file_json):
        # device_name='emulator-5554 device', 
        # app_name='tv.danmaku.bili', 
        # apk_path='./App/iBiliPlayer-bili.apk'):
        app_file_json_data = get_desired_caps(app_file_json)
        self.device_name = get_json_value(app_file_json_data, 'deviceName')
        self.app_name = get_json_value(app_file_json_data, 'appPackage')
        self.apk_path = get_json_value(app_file_json_data, 'installApkPath')
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

