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

def select_list_type():
    choice = 0
    allowed_choices = [1, 2]
    while True:
        print("Which type of list do you want: ")
        print("1 - Default randomic list")
        print("2 - Customized randomic list")
        choice = int(input("Type your choice accordingly the options above: "))

        if choice in allowed_choices:
            break

    return choice

def customized_list_setup():
    customized_parameters = {}

    allow_repeated = True
    positive_answers = ["y", "Y", "yes", "YES", "Yes", "Yeah", "yeah"]
    negative_answers = ["n", "N", "no", "NO", "No", "Nope", "nope"]
    while True:
        answer = input("Allow repeated elements in the list (Y/n): ")

        if answer in positive_answers or answer in negative_answers:
            if answer in negative_answers:
                customized_parameters["allow_repeated"] = False
            else:
                customized_parameters["allow_repeated"] = True
            break

    list_size = 0
    while True:
        list_size = int(input("Enter how much elements do you want in the list: "))

        if list_size >= 2:
            customized_parameters["list_size"] = list_size
            break
    
    sup_lim = 0
    while True:
        sup_lim = int(input("Enter an integer as the maximum number to be generated for the list: "))
        customized_parameters["sup_lim"] = sup_lim
        
        if not customized_parameters["allow_repeated"]:
            if sup_lim >= customized_parameters["list_size"]:
                break
        else:
            if sup_lim >= 1:
                break

    return customized_parameters

def program_startup(list_type):
    random_list = []
    if list_type == 1:
        random_list = gen_random_list()
    elif list_type == 2:
        parameters = customized_list_setup()
        random_list = gen_random_list(sup_lim=parameters["sup_lim"],
                                      list_size=parameters["list_size"],
                                      allow_repeated=parameters["allow_repeated"])
        
    return random_list

