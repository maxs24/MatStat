from scipy.stats import chisquare

def get_data_from_file(file_name):
    data_one = []
    data_two = []

    with open(file_name, 'r') as file:
        for line in file:
            values = []
            mas_line = line.split(" ")
            for elem in mas_line:
                if elem != '':
                    values.append(elem)
            data_one.append(float(values[0]))
            data_two.append(float(values[1]))

    return data_one, data_two

def is_normal(data, phi):
    statistic, p = chisquare(data)
    print("p-значение: ", p)
    if p > phi:
        print("Распределение выборки является нормальным")
    else:
        print("Распределение выборки не является нормальным")

if __name__ == '__main__':
    FILE_NAME = 'Ex2_DAT8.TXT'
    PHI = 0.05

    data_one, data_two = get_data_from_file(FILE_NAME)

    print("Проверка первой выборки")
    is_normal(data_one, PHI)
    print("\n")

    print("Проверка второй выборки")
    is_normal(data_two, PHI)