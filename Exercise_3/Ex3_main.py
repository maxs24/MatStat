import scipy
import statistics
from MatStat import workWithFile


def is_ttest(data, mean, phi, alternative):
    stat, p = scipy.stats.ttest_1samp(data, popmean=mean, alternative=alternative)
    print('p: ', p)
    if p > phi:
        print("Гипотеза о равенстве средних принимается")
    else:
        print("Гипотеза о равенстве средних отклоняется и принимается альтернативная")


def data_ttest(data, mean, phi):
    print("Первая альтернативная гипотеза: "
          "среднее базового распределения выборки "
          "отличается от заданного среднего значения генеральной совокупности")
    is_ttest(data, mean, phi, "two-sided")
    print("\n")
    print("Вторая альтернативная гипотеза: "
          "среднее значение базового распределения выборки "
          "меньше заданного среднего значения генеральной совокупности")
    is_ttest(data, mean, phi, "less")
    print("\n")
    print("Третья альтернативаня гипотеза: "
          "среднее значение базового распределения выборки "
          "больше, чем заданное среднее значение генеральной совокупности")
    is_ttest(data, mean, phi, "greater")
    print("\n")


def run(file_name, phi):
    data_1, data_2 = workWithFile.get_data_from_file_vertical(file_name)
    mean_1 = statistics.mean(data_1)
    mean_2 = statistics.mean(data_2)

    print("Сравнение первой выборки")
    data_ttest(data_1, mean_2, phi)
    print("\n")
    print("Сравнение второй выборки")
    data_ttest(data_2, mean_1, phi)


if __name__ == '__main__':
    FILE_NAME = 'Ex3_DAT8.TXT'
    PHI = 0.05

    run(FILE_NAME, PHI)
