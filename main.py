from enum import Enum
import glob
import dash


DAILY_REPORT_BASE_PATH = '/Users/kotaro-seki/Documents/my-knowledge/report/daily/'


class Tag(Enum):
    weight = 'weight'
    calorie = 'kcal'

    def get_tag(self):
        return '#' + self.value


def main():
    weight_list = []
    calorie_list = []
    file_paths = glob.glob(DAILY_REPORT_BASE_PATH + '*')
    for file_path in file_paths:
        datalist = read_data(file_path)
        for data in datalist:
            if Tag.weight.get_tag() in data:
                weight_list.append(extract_value(data))
                continue
            if Tag.calorie.get_tag() in data:
                calorie_list.append(extract_value(data))
                continue
    print(weight_list)
    print(calorie_list)


def read_data(filepath):
    f = open(filepath, 'r', encoding='UTF-8')
    datalist = f.readlines()
    f.close()
    return datalist


def extract_value(data):
    strings = data.split()
    for string in strings:
        if '#' not in string:
            return string


if __name__ == '__main__':
    main()
