def solution(elements):
    answer = 0
    n = len(elements)
    elements.extend(elements)
    print(elements)

    answer = set()

    for i in range(n):
        for j in range(1, n + 1):
            answer.add(sum(elements[i:i + j]))
    return len(answer)