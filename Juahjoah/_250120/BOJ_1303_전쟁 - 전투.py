
'''
 * 문제 링크: https://www.acmicpc.net/problem/1303
 * 메모리: 34984 KB
 * 시간: 68 ms
 * 시간 복잡도: O(N*M)
 * 공간 복잡도: O(N*M)


1. 인접해 있는 같은 병사들의 정보를 찾기 위해 BFS로 탐색
2. M×N 배열을 순회하며 방문하지 않은 병사에서 BFS 탐색 시작
3. BFS로 같은 색의 연결된 병사 수(cnt)를 계산
4. 계산된 병사 수를 제곱해 해당 색깔의 점수에 더함
5. 모든 셀 탐색이 끝나면 흰색 점수와 검은색 점수를 출력
'''

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))

    cnt = 1                                                     # 숫자를 셀 때, 처음 들어 오는 값도 고려해야 하기 때문에 꼭 1로 두고 시작!

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내에 있고, 아직 방문하지 않았으며, 같은 색깔의 병사인 경우
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and input_list[nx][ny] == input_list[i][j]:
                visited[nx][ny] = 1        # 방문 처리
                queue.append((nx, ny))     # 큐에 추가
                cnt += 1                   # 숫자 세기

    return cnt


N, M = map(int, input().split())
input_list = [list(input()) for _ in range(M)]

# 방문 여부를 저장하는 배열
visited = [[0]*N for _ in range(M)]
answer_W = 0
answer_B = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and input_list[i][j] == 'W':      # 방문하지 않았고, 흰색 병사인 경우
            # BFS(i, j)
            visited[i][j] = 1                                   # 방문 처리
            answer_W += BFS(i, j)**2                            # BFS 결과의 제곱을 점수에 추가
        elif visited[i][j] == 0 and input_list[i][j] == 'B':    # 방문하지 않았고, 검은색 병사인 경우
            # BFS(i, j)
            visited[i][j] = 1
            answer_B += BFS(i, j)**2  


print(answer_W, answer_B)
