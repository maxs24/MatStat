import scipy
import statistics
from MatStat import workWithFile
import numpy


def run(file_name, phi):
    data_1, data_2 = workWithFile.get_data_from_file_vertical(file_name)

    interval_1 = scipy.stats.norm.interval(confidence=1.0 - phi, loc=statistics.mean(data_1), scale=numpy.std(data_1))
    interval_2 = scipy.stats.norm.interval(confidence=1.0 - phi, loc=statistics.mean(data_2), scale=numpy.std(data_2))
    print("Доверительный интервал среднего для первой выборки: ")
    print(interval_1)
    print("Доверительный интервал среднего для второй выборки: ")
    print(interval_2)


if __name__=='__main__':
    FILE_NAME = "Ex6_DAT8.TXT"
    PHI = 0.05

    run(FILE_NAME, PHI)

