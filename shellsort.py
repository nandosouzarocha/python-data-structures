from utils import *


def shell_sort(a_list):
    h = 1
    n = len(a_list)

    while h < n:
        h = 3 * h + 1
    h = h // 3

    while h > 0:
        for i in range(h, n):
            element = a_list[i]
            j = i

            while j >= h and a_list[j - h] > element:
                a_list[j] = a_list[j - h]
                j -= h

            a_list[j] = element
        h //= 2


if __name__ == '__main__':
    list_type_choice = select_list_type()
    random_list = program_startup(list_type=list_type_choice)
    print(random_list)
    shell_sort(random_list)
    print(random_list)
