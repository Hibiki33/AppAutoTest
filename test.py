from app.app import App

def test_install_func(app_file_json_data):
    a = App(app_file_json_data)
    a.app_uninstall

if __name__ == '__main__':
    test_install_func('./conf/caps_bili.json')
