# 12851. 숨바꼭질 2

'''
 * 문제 링크: https://www.acmicpc.net/problem/12851
 * 메모리: 45532 KB
 * 시간: 136 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs(N, K):
    queue = deque()
    queue.append((N, 0))
    visited = [[0, 0] for _ in range(100001)] # [개수, 시간]
    visited[N][0] += 1

    while queue:
        node, time = queue.popleft()

        if node == K:
            return time, visited[node][0]

        for cur_node in [node + 1, node - 1, node * 2]:         # 현재 위치에서 이동 가능한 다음 위치들
            if 0 <= cur_node <= 100000:
                if visited[cur_node][1] == time + 1:            # 이미 방문했지만 동일한 시간(time+1)으로 도달 가능한 경우
                    visited[cur_node][0] += visited[node][0]    # 지금 위치까지 오는데 걸린 경로 수를 누적
                elif visited[cur_node][1] == 0:                 # 아직 방문한 적 없는 위치
                    visited[cur_node][0] += visited[node][0]    # 현재까지의 경로 수를 그대로 복사
                    visited[cur_node][1] = time + 1
                    queue.append((cur_node, time + 1))

N, K = map(int, input().split())

answer, result = bfs(N, K)
print(answer)
print(result)
