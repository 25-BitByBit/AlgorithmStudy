# 2346. 풍선 터뜨리기

'''
 * 문제 링크: https://www.acmicpc.net/problem/2346
 * 메모리: 34924 KB
 * 시간: 56 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

 * deque의 다양한 활용 방식 파악
    * deque.rotate()를 활용하여 인덱스 이동을 구현
    * rotate()는 양수일 경우 오른쪽으로, 음수일 경우 왼쪽으로 회전
      * 회전 후 인덱스는 0부터 시작

'''

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
input_list = list(map(int, input().split()))

queue = deque()
for i in range(N):
    queue.append((i + 1, input_list[i]))

answer_list = []

while queue:
    idx, move = queue.popleft()
    answer_list.append(idx)

    if not queue:
        break

    if move > 0:
        queue.rotate(-(move - 1))
    else:
        queue.rotate(-move)

print(*answer_list)