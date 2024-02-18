from utils import *


def quick_sort(a_list, left, right):
    if left < right:
        p = partition(a_list, left, right)
        quick_sort(a_list, left, p)
        quick_sort(a_list, p + 1, right)


def partition(a_list, left, right):
    pivot = a_list[(left + right) // 2]
    i = left - 1
    j = right + 1

    while True:
        i += 1
        while i <= j and a_list[i] < pivot:
            i += 1

        j -= 1
        while i <= j and a_list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        aux = a_list[i]
        a_list[i] = a_list[j]
        a_list[j] = aux


if __name__ == '__main__':
    list_type_choice = select_list_type()
    random_list = program_startup(list_type=list_type_choice)
    print(random_list)
    quick_sort(random_list, 0, len(random_list) - 1)
    print(random_list)
