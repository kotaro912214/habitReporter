from enum import Enum


class Tag(Enum):
    weight = 'kg'
    calorie = 'kcal'


def main():
    datalist = read_data('sample.txt')
    weight_list = []
    calorie_list = []
    for data in datalist:
        if Tag.weight.value in data:
            weight_list.append(extract_value(data))
            continue
        if Tag.calorie.value in data:
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
    a, b = data.split()
    if '#' in a:
        return b
    return a


if __name__ == '__main__':
    main()
