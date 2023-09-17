import os
import shutil
from datetime import datetime

source_folder = '/path/to/source/dat/folder'
destination_folder = '/path/to/destination/folder'
cutoff_time = datetime(2023, 9, 1)  # 특정 시점 이후의 파일을 복사

def copy_new_files(source, destination, cutoff_time):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time > cutoff_time:
                shutil.copy(file_path, os.path.join(destination_folder, file))

copy_new_files(source_folder, destination_folder, cutoff_time)
