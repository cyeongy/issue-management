from heapq import heappush, heappop
from collections import deque


def solution(cards):
    answer = 0

    card_counts = []
    visited = [False for _ in range(len(cards) + 1)]

    for cur in range(len(cards)):
        cur += 1
        if visited[cur]:
            continue
        count = 0

        while True:
            nxt = cards[cur - 1]
            if visited[nxt]:
                break
            visited[nxt] = True
            count += 1
            cur = nxt
        heappush(card_counts, -count)

    if len(card_counts) > 2:
        a = heappop(card_counts)
        b = heappop(card_counts)
        return a * b
    return 0
# 1 2 3 4 5 6 7 8 idx
# 8 6 3 7 2 5 1 4 value
# 1 : 8 4 7 1
# 2 : 6 5 2
# 3 : 3