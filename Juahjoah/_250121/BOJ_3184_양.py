'''
 * 문제 링크: https://www.acmicpc.net/problem/1303
 * 메모리: 34992 KB
 * 시간: 120 ms
 * 시간 복잡도: O(R*C)
 * 공간 복잡도: O(R*C)


1. 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250)
  → 최대 62,500개의 노드. 완전탐색(O(N), O(NlogN))을 해도 가능하기는 하지만, O(N²)은 안됨 = visited를 활용!
2. 농장의 모든 셀을 순회하며, 울타리가 아니고 방문하지 않은 셀에서 BFS 시작
3. BFS로 인접한 셀을 탐색하며 양의 수(cnt_S)와 늑대의 수(cnt_W)를 비교
4. 양과 늑대의 수를 비교해 더 많은 수를 0으로 설정
5. 결과를 누적해 농장에서 생존한 양(answer_Sheep)과 늑대(answer_Wolf)의 수를 출력
'''

from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i,j))

    # 현재 영역에서 양과 늑대의 수 초기화
    cnt_S = 0
    cnt_W = 0

    while queue:
        x, y = queue.popleft()

        # 맨 처음 들어오는 값도 판단해주기 위해 양, 늑대를 nx, ny로 확인하지 않고 x,y로 확인
        # 현재 위치가 양인지 늑대인지 판단
        if farm[x][y] == 'o':  # 양 발견 시
            cnt_S += 1
        if farm[x][y] == 'v':  # 늑대 발견 시
            cnt_W += 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 다음 위치가 유효한 범위 내에 있고, 방문하지 않았으며, 울타리가 아닌 경우
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and farm[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

    # 양과 늑대의 수 비교
    if cnt_S > cnt_W:        # 양이 더 많으면 늑대는 모두 도망감
        cnt_W = 0
    else:                    # 늑대가 더 많으면 양은 모두 잡아먹힘
        cnt_S = 0

    return cnt_S, cnt_W


R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
answer_Sheep = 0
answer_Wolf = 0


for i in range(R):
    for j in range(C):
        # 울타리가 아니고 방문하지 않은 셀에서만 BFS 시작
        if farm[i][j] != '#' and not visited[i][j]:
            sheep = 0
            wolf = 0
            visited[i][j] = 1        # 현재 위치 방문 처리

            sheep, wolf = bfs(i, j)

            answer_Sheep += sheep
            answer_Wolf += wolf

print(answer_Sheep, answer_Wolf)
