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
        self.accessed = False
        for task_name in tasks:
            self.tasks[task_name] = []
            for cur_op_dict in tasks[task_name]:
                self.tasks[task_name].append(AppOp(cur_op_dict))
    
    def __call__(self, search_keyword, task_name):
        self.search(search_keyword)
        res = self.do_task(task_name)
        self.exit(self.driver)
        return res

    def search(self, keyword):
        if not self.accessed:
            self.access_button(self.driver)
            self.accessed = True
        if not self.in_search_panel:
            self.search_frame_id(self.driver)
            self.in_search_panel = True
        self.search_edit_bar(self.driver, keyword)
        self.search_button(self.driver)
    
    def get_task_list(self):
        return list(self.tasks.keys())
    
    def do_task(self, task_name):
        if not self.in_search_panel:
            raise Exception("Not in search panel but calling do_task()")
        if task_name not in self.tasks:
            raise Exception(f"Task {task_name} not found")
        res = []
        for op in self.tasks[task_name]:
            res.append(op(self.driver))
        return res