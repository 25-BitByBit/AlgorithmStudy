# 11725. 트리의 부모 찾기

'''
 * 문제 링크: https://www.acmicpc.net/problem/11725
 * 메모리: 65240 KB
 * 시간: 360 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

 * 인접 리스트에 저장된 트리에서 BFS를 통해 부모 노드를 찾는 문제
    * 트리니까 각 너비에 맞게 접근해야 함. = BFS
'''

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        node = queue.popleft()

        for n in adj_list[node]:
            if not visited[n]:
                answer_list[n] = node
                queue.append(n)
                visited[n] =True

    return


N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N-1)]

adj_list = [[] for _ in range(N + 1)]

for x, y in input_list:
    adj_list[x].append(y)
    adj_list[y].append(x)

answer_list = [0] * (N + 1)
visited = [False] * (N + 1)
bfs()

for answer in range(2, N + 1):
    print(answer_list[answer])