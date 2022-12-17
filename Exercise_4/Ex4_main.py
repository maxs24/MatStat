import scipy
from MatStat import workWithFile


def is_ttest_ind(datas, phi, alternative):
    stat, p = scipy.stats.ttest_ind(datas[0], datas[1], alternative=alternative)
    print('p: ', p)
    if p > phi:
        print("Гипотеза о равенстве средних принимается")
    else:
        print("Гипотеза о равенстве средних отклоняется и принимается альтернативная")


def run(file_name, phi):
    data_1, data_2 = workWithFile.get_data_from_file_for_gorizontal(file_name)

    print("Первая альтернативная гипотеза: средние значения распределений, лежащих в основе выборок, неравны.")
    is_ttest_ind((data_1, data_2), phi, 'two-sided')
    print("\n")
    print("Вторая альтернативная гипотеза: среднее значение распределения, лежащего в основе первой выборки, "
          "меньше среднего значения распределения, лежащего в основе второй выборки.")
    is_ttest_ind((data_1, data_2), phi, 'less')
    print("\n")
    print("Третья альтернативаня гипотеза: среднее значение распределения, лежащего в основе первой выборки, больше, "
          "чем среднее значение распределения, лежащего в основе второй выборки")
    is_ttest_ind((data_1, data_2), phi, 'greater')


if __name__ == '__main__':
    FILE_NAME = 'Ex4_DAT8.TXT'
    PHI = 0.05

    run(FILE_NAME, PHI)

