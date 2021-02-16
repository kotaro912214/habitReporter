import os
import glob


class FileUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_recursive_file_paths(target_dir) -> [str]:
        file_paths = []
        if not os.path.isdir(target_dir):
            return [target_dir]
        unknown_paths = glob.glob(target_dir + "/*")
        for unknown_path in unknown_paths:
            file_paths += FileUtil.get_recursive_file_paths(unknown_path)
        return file_paths

    @staticmethod
    def read_lines(file_path) -> [str]:
        with open(file_path, 'r') as f:
            return list(map(lambda s: s.strip(), f.readlines()))
