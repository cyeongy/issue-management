from collections import Counter


def solution(topping):
    answer = 0

    one_set = Counter(topping)
    ohter_set = set()

    while topping:
        element = topping[-1]
        ohter_set.add(element)

        if one_set[element] > 1:
            one_set[element] -= 1
        else:
            del one_set[element]

        del topping[-1]
        if len(one_set) == len(ohter_set):
            answer += 1
    return answer
