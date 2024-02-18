from utils import *


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        element = a_list[i]
        j = i - 1

        while j >= 0 and a_list[j] > element:
            a_list[j + 1] = a_list[j]
            j -= 1

        a_list[j + 1] = element


if __name__ == '__main__':
    list_type_choice = select_list_type()
    random_list = program_startup(list_type=list_type_choice)
    print(random_list)
    insertion_sort(random_list)
    print(random_list)
