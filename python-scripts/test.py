def print_log(level,msg):
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} {level} {msg}")

# print_log("INFO", "This is an info message.")
# print_log("ERROR", "This is an error message.")

# def check_status(name,status):
#     if status == 1:
#         print(f"{name} is active.")
#     else:
#         print(f"{name} is inactive.")

# check_status("nginx", 1)
# check_status("mysql", 0)

import os
def check_file_exists(file_path):
    if os.path.exists(file_path):
        print_log("INFO",f"file{file_path} exists")
    else:
        print_log("ERROR",f"file{file_path} not exists")
check_file_exists("/")