from collections import Counter


def solution(want, number, discount):
    answer = 0

    plist = {}
    for w, n in zip(want, number):
        plist[w] = n

    plist = Counter(plist)

    for i in range(len(discount) - 9):
        if len(plist - Counter(discount[i:i + 10])):
            continue
        answer += 1

    return answer