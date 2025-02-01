'''
 * 문제 링크: https://www.acmicpc.net/problem/14442
 * 메모리: 223184 KB
 * 시간: 1580 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

1. 기존 문제들과 달리 벽을 부술 수 있는 가능성(K)이 존재하는 문제
2. 벽을 부순 횟수를 저장할 수 있도록 visited 배열을 생성
3. 벽을 부순 횟수가 K보다 작은 경우에만 함수를 진행하도록 설정
4. bfs 함수를 통해 이동 횟수를 계산

 * python으로 진행하면 시간 초과가 나지만, pypy3로 진행하면 통과됨.
 * sys.readline()을 사용한 경우에도 통과함. 
'''

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j):
    queue = deque()
    # 초기 시작점과 이동 횟수를 queue에 추가
    queue.append((i, j, 1)) # 초기 이동 횟수를 1로 설정해야 문제에서 요구한 조건과 일치

    while queue:
        x, y, step = queue.popleft()

        if x == N - 1 and y == M - 1:
            return step

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                # 지나간 벽의 수를 세야 하기 때문에 해당 방식으로 계산
                break_cnt = board[nx][ny] + visited[x][y]
                # 부순 벽의 수가 주어진 K 값 이내인 경우만 진행
                if break_cnt <= K and break_cnt < visited[nx][ny]:
                    visited[nx][ny] = break_cnt
                    queue.append((nx, ny, step + 1))

    return -1

N, M, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
board = [list(map(int, input().rstrip())) for _ in range(N)]

answer = 1
# K보다 큰 값을 설정해서 벽을 부순 횟수를 저장할 수 있도록 설정
visited = [[11]*M for _ in range(N)]
# 시작점 방문처리
visited[0][0] = 0

print(bfs(0, 0))
