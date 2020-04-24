### biggest / smallest function

def biggest_smallest(selection, list_of_numbers):
    # list_of_numbers = [43, 53, 27, 40, 100, 201]

    list_of_numbers.sort()

    smallest_num = (list_of_numbers[0])
    biggest_num = (list_of_numbers[-1])
    # selection = ("small")

    if selection == ("small"):
        print("smallest value = ", list_of_numbers[0])
    elif selection == ('big'):
        print("largest value = ", list_of_numbers[-1])
    else:
        print(list_of_numbers)

biggest_smallest("small", [3, 52, 27, 50, 145, 221])

biggest_smallest("big", [43, 53, 27, 40, 100, 201])