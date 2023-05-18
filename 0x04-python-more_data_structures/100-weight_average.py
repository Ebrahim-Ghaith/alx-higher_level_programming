#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_of_products = 0
    sum_of_weights = 0

    for score, weight in my_list:
        sum_of_products += score * weight
        sum_of_weights += weight

    average = sum_of_products / sum_of_weights
    return average
