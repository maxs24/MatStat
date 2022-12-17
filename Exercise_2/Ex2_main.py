from scipy.stats import chisquare
from MatStat import workWithFile


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

    data_one, data_two = workWithFile.get_data_from_file_vertical(FILE_NAME)

    print("Проверка первой выборки")
    is_normal(data_one, PHI)
    print("\n")

    print("Проверка второй выборки")
    is_normal(data_two, PHI)