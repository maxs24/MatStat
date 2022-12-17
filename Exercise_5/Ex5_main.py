import scipy
from MatStat import workWithFile
import numpy


def f_test(data_1, data_2, alternative):
    data_1 = numpy.array(data_1)
    data_2 = numpy.array(data_2)
    f = numpy.var(data_1, ddof=1)/numpy.var(data_2, ddof=1)
    df1 = data_1.size - 1
    df2 = data_2.size - 1

    if alternative == 'greater':
        p = 1.0 - scipy.stats.f.cdf(f, df1, df2)
    elif alternative == 'less':
        p = scipy.stats.f.cdf(f, df1, df2)
    else:
        p = 2.0 * (1.0 - scipy.stats.f.cdf(f, df1, df2))

    return f, p


def is_f_test(datas, phi, alternative):
    stat, p = f_test(datas[0], datas[1], alternative)
    print('p: ', p)
    if p > phi:
        print("Гипотеза о равенстве дисперсий принимается")
    else:
        print("Гипотеза о равенстве дисперсий отклоняется и принимается альтернативная")


def run(file_name, phi):
    data_1, data_2 = workWithFile.get_data_from_file_for_gorizontal(file_name)

    print("Первая альтернативная гипотеза: "
          "дисперсии распределений, лежащих в основе выборок, неравны.")
    is_f_test((data_1, data_2), phi, "two_sided")
    print('\n')

    print("Вторая альтернативная гипотеза: "
          "дисперсия распределения, лежащего в основе первой выборки, "
          "меньше дисперсии распределения, лежащего в основе второй выборки.")
    is_f_test((data_1, data_2), phi, "less")
    print('\n')

    print("Третья альтернативная гипотеза: "
          "дисперсия распределения, лежащего в основе первой выборки, "
          "больше дисперсии распределения, лежащего в основе второй выборки.")
    is_f_test((data_1, data_2), phi, "greater")


if __name__ == '__main__':
    FILE_NAME = 'Ex5_DAT8.TXT'
    PHI = 0.05

    run(FILE_NAME, PHI)


