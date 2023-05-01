from app.app import App

def test_install_func(app_file_json_data):
    a = App(app_file_json_data)
    a.app_direct_install()

if __name__ == '__main__':
    test_install_func('caps_bili.json')
