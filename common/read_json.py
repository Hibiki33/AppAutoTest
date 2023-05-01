import json
import os

from app_op import AppOp

def get_desired_caps(caps_file_name):
    with open(os.path.join("..", "conf", caps_file_name), 'r') as f:
        desired_caps = json.loads(f.read())
    return desired_caps

def get_json_value(json_data, key):
    if key in json_data:
        return json_data[key]
    else:
        raise Exception(f'get_json_value failed, \"{key}\" not in json_data')

def get_app_ops(app_file_name):
    with open(os.path.join("..", "conf", app_file_name), 'r') as f:
        json_data = json.loads(f.read())
    app_ops = {}
    app_ops["access_button"] = AppOp(get_json_value(json_data, "access_button"))
    app_ops["search_frame_id"] = AppOp(get_json_value(json_data, "search_frame_id"))
    app_ops["search_edit_bar"] = AppOp(get_json_value(json_data, "search_input_id"))
    app_ops["search_button"] = AppOp(get_json_value(json_data, "search_button_id"))
    tasks = get_json_value(json_data, "tasks")
    app_ops["tasks"] = {}
    for task_key in tasks:
        app_ops["tasks"][task_key] = AppOp(get_json_value(tasks, task_key))
    return app_ops

if __name__ == '__main__':
    x = get_desired_caps('caps_bili.json')
    print(x["appActivity"])