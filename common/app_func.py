from common.app_op import AppOp
from common.read_json import get_json_value

class AppFunc:
    
    def __init__(self, driver, app_file_func_json_data):
        self.driver = driver
        self.access_button = AppOp(get_json_value(app_file_func_json_data, "access_button"))
        self.search_frame_id = AppOp(get_json_value(app_file_func_json_data, "search_frame_id"))
        self.search_edit_bar = AppOp(get_json_value(app_file_func_json_data, "search_edit_bar"))
        self.search_button = AppOp(get_json_value(app_file_func_json_data, "search_button"))
        self.exit = AppOp(get_json_value(app_file_func_json_data, "exit"))
        tasks = get_json_value(app_file_func_json_data, "tasks")
        self.tasks = {}
        self.in_search_panel = False
        for task_name in tasks:
            self.tasks[task_name] = []
            for key in tasks[task_name]:
                self.tasks[task_name].append(AppOp(tasks[task_name][key]))
    
    def __call__(self, search_keyword, task_name):
        self.search(search_keyword)
        self.do_task(task_name)
        self.exit(self.driver)

    def search(self, keyword):
        if self.in_search_panel:
            raise Exception("Already in search panel but calling search()")
        self.access_button(self.driver)
        self.search_frame_id(self.driver)
        self.search_edit_bar(self.driver, keyword)
        self.search_button(self.driver)
        self.in_search_panel = True
    
    def get_task_list(self):
        return list(self.tasks.keys())
    
    def do_task(self, task_name):
        if not self.in_search_panel:
            raise Exception("Not in search panel but calling do_task()")
        if task_name not in self.tasks:
            raise Exception(f"Task {task_name} not found")
        for op in self.tasks[task_name]:
            op(self.driver)