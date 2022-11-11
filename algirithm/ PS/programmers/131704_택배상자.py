def solution(order):
    answer = 0

    sub_convey = []
    idx = 0
    for box in range(1, len(order) + 1):
        while sub_convey and sub_convey[-1] == order[idx]:
            del sub_convey[-1]
            idx += 1
            answer += 1
        if order[idx] == box:
            idx += 1
            answer += 1
        else:
            sub_convey.append(box)
    while sub_convey and sub_convey[-1] == order[idx]:
        del sub_convey[-1]
        idx += 1
        answer += 1
    return answer