import json
import os

def get_desired_caps(caps_file_name):
    with open(os.path.join("..", "conf", caps_file_name), 'r') as f:
        desired_caps = json.loads(f.read())
    return desired_caps

def get_test_data(test_data_file_name):
    with open(os.path.join("..", "data", test_data_file_name), 'r') as f:
        test_data = json.loads(f.read())
    return test_data

if __name__ == '__main__':
    x = get_desired_caps('caps_bili.json')
    print(x["appActivity"])