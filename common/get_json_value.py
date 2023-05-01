def get_json_value(json_data, key):
    if key in json_data:
        return json_data[key]
    else:
        raise Exception(f'get_json_value failed, \"{key}\" not in json_data')