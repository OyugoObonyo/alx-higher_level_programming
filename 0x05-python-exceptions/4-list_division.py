#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except TypeError:
            print("wrong type")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            result_list.append(divide)
    return result_list
