from utils import *


def heap_sort(a_list):
    list_size = len(a_list)
    i = list_size // 2 - 1

    while i >= 0:
        max_heapfy(a_list, list_size, i)
        i -= 1

    i = list_size - 1

    while i > 0:
        aux = a_list[0]
        a_list[0] = a_list[i]
        a_list[i] = aux

        max_heapfy(a_list, i, 0)
        i -= 1


def max_heapfy(a_list, list_size, position):
    root = position
    left = 2 * position + 1
    right = 2 * position + 2

    if left < list_size and a_list[left] > a_list[root]:
        root = left

    if right < list_size and a_list[right] > a_list[root]:
        root = right

    if root != position:
        aux = a_list[root]
        a_list[root] = a_list[position]
        a_list[position] = aux

        max_heapfy(a_list, list_size, root)


if __name__ == '__main__':
    list_type_choice = select_list_type()
    random_list = program_startup(list_type=list_type_choice)
    print(random_list)
    heap_sort(random_list)
    print(random_list)