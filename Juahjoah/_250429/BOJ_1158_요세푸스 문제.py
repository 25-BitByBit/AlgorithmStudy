# 1158. 요세푸스 문제

'''
 * 문제 링크: https://www.acmicpc.net/problem/1158
 * 메모리: 34908 KB
 * 시간: 2356 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

 * 아이디어가 필요한 구현 방식
 * 오래간만에 Join 활용
'''

from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
answer_list = []

for i in range (1, N + 1):
    queue.append(i)

while queue:
    # if len(queue) >= K:
    #     x = queue[K]
    #     answer_list.append(x)
    #     queue.remove(queue[K])

    for _ in range(K - 1):
        queue.append(queue.popleft()) # K번째 앞에 있는 값들 꺼내서 뒤로 붙이기
    answer_list.append(queue.popleft()) # K번째 값 뽑아서 넣기

print('<' + ', '.join(map(str, answer_list)) + '>')