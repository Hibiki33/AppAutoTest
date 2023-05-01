import os
import _thread

class RunAppium():
    def __init__(self):
        _thread.start_new_thread(self.run_appium, ())
    
    def run_appium(self):
        os.system('adb kill-server')
        os.system('appium -a localhost -p 4723')