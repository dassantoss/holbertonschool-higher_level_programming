#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    scores = [score for score, weight in my_list]
    weights = [weight for score, weight in my_list]

    weights_sum = sum(map(lambda x, y: x * y, scores, weights))
    total_weight = sum(weights)

    return (weights_sum / total_weight)
