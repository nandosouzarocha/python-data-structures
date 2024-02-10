import random
from utils import *

'''
    This list will receive an unordered list and sort it's items based on the
    selection sort algorithm
'''
def selection_sort(a_list):
    for i in range(len(a_list)):
        smaller_position = i # Holds the index of the smaller element in the list

        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[smaller_position]:
                smaller_position = j

        aux = a_list[i]
        a_list[i] = a_list[smaller_position]
        a_list[smaller_position] = aux


if __name__ == '__main__':
    list_type_choice = select_list_type()
    random_list = program_startup(list_type=list_type_choice)
    print(random_list)
    selection_sort(random_list)
    print(random_list)
