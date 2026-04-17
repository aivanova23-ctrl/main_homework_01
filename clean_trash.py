import os
import argparse
import time
parser=argparse.ArgumentParser( description = "checking files")
parser.add_argument("trash_folder", type = str, help = "назови папку")
parser.add_argument("--age_thr", type = int, help = "назови время")
args = parser.parse_args()
with open("../clean_trash.log", "a") as log_file:
    while True:
        for root, dirs, files in os.walk(args.trash_folder, topdown=False):
            for file in files:
                current_time = time.time()
                last_changes = os.path.getmtime(os.path.join(root, file))
                interval=current_time-last_changes
                if interval>args.age_thr:
                    old_file_path = os.path.join(root, file)
                    log_file.write(f"{old_file_path}\n")
                    os.remove(old_file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                stuff = os.listdir(dir_path)
                if len(stuff) == 0:
                    log_file.write(f'{dir_path}\n')
                    os.rmdir(dir_path)
        time.sleep(1)
