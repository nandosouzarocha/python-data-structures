import random

'''
    The parameters of the function bellow are:
    * list_size: Size of the list. How many elements should the list have. Default is ten.
    * sup_lim: Which is the largest integer that the list should have. Default is ninety nine.
    * allow_repeated: Determines if the list should allow repeated elements. Default is true.
'''
def gen_random_list(list_size=10, sup_lim=99, allow_repeated=True):
    randomic_list = []

    while len(randomic_list) < list_size:
        if not len(randomic_list): # If the lists has no elements yet
            randomic_list.append(random.randint(1, sup_lim))
            continue
        
        element = random.randint(1, sup_lim)
        if not allow_repeated and already_in_the_list(randomic_list, element):
            continue

        randomic_list.append(element)

    return randomic_list

'''
    The function bellow compares if an element, 'elem' parameter, is in a list given, 
    'a_list' parameter. It will return true in case the element is already in the list given.
'''
def already_in_the_list(a_list, elem):
    if elem in a_list:
        return True
    return False
