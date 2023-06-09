import json
import os

def get_desired_caps(caps_file_name):
    with open(os.path.join("conf", caps_file_name), 'r') as f:
        desired_caps = json.loads(f.read())
    return desired_caps

def get_app_func(app_func_file_name, driver):
    with open(os.path.join("conf", app_func_file_name), 'r') as f:
        app_file_json_data = json.loads(f.read())
    from common.app_func import AppFunc
    return AppFunc(driver, app_file_json_data)

def get_json_value(json_data, key):
    if key in json_data:
        return json_data[key]
    else:
        raise Exception(f'get_json_value failed, \"{key}\" not in json_data')

if __name__ == '__main__':
    x = get_desired_caps('caps_bili.json')
    print(x["appActivity"])