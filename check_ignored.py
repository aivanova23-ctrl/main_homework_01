import os
import argparse
formats = []
filenames = []
def scan_gitignore(dir_name):
    gitignore_path = os.path.join(dir_name,".gitignore")
    with open(gitignore_path, encoding = 'utf-8') as file:
        for name in file:
            name = name.strip()
            if "*" in name:
            else:
                file_name = os.path.basename(name)
                filenames.append(file_name)
#check ignored.py
parser = argparse.ArgumentParser( description = "checking files")
args = parser.parse_args()
scan_gitignore(args.dir_name)
for root, dirs, files  in os.walk(args.dir_name):
    for file in files:
        format_extraction = str(file).split(".")[-1]
        path_in_dir = os.path.join(root, file)
        path_with_dir = f"{args.dir_name}/{path_in_dir}"
        if file in filenames:
            print(f"{path_with_dir} ignored by expression {path_in_dir}")
        elif format_extraction in formats:
            print(f"{path_with_dir} ignored by expression *.{format_extraction}")