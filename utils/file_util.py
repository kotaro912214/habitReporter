import os
import glob


class FileUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_recursive_file_paths(target_dir) -> [str]:
        file_paths = []
        unknown_paths = glob.glob(target_dir)
        while len(unknown_paths) > 0:
            for i, unknown_path in enumerate(unknown_paths):
                if os.path.isdir(unknown_path):
                    unknown_paths += glob.glob(unknown_path + '/*')
                else:
                    file_paths.append(unknown_path)
                unknown_paths = unknown_paths[:i] + unknown_paths[i + 1:]
        return file_paths

    @staticmethod
    def read_lines(file_path) -> [str]:
        with open(file_path, 'r') as f:
            return list(map(lambda s: s.strip(), f.readlines()))
