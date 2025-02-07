
'''
 * 문제 링크: https://www.acmicpc.net/problem/1941
 * 메모리: 33432 KB
 * 시간: 6504 ms → 260ms(answer_list를 set으로 변경했을 때)
 * 시간 복잡도: O(N×4⁷) → O(4⁷)
 * 공간 복잡도: O(N)

 * DFS를 이용
    * 7명의 학생을 뽑는 모든 경우의 수를 구해야 하므로 DFS를 사용
    * 7명의 학생을 뽑을 때, 'S'인 학생이 4명 이상인지 확인
'''


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(crews, y_cnt):

    if len(crews) == 7:
        check_crews = tuple(sorted(crews, key = lambda x:(x[0], x[1])))
        if check_crews not in answer_list:
            answer_list.append(check_crews)
            # answer_list.add(check_crews)  # set으로 변경하면 시간이 260ms로 줄어듦.
            global answer
            answer += 1
        return

    for x, y in crews:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 'Y':
                    y_cnt += 1

                if y_cnt <= 3:
                    crews.append((nx, ny))
                    dfs(crews, y_cnt)

                # 다시 원상태로 되돌려 주기
                    crews.pop()
                if board[nx][ny] == 'Y':
                    y_cnt -= 1
                visited[nx][ny] = False


board = [list(input()) for _ in range(5)]

visited = [[False] * 5 for _ in range(5)]
answer = 0
answer_list = []
# answer_list = set()

for i in range(5):
    for j in range(5):
        visited[i][j] = True
        if board[i][j] == 'S':
            dfs([(i, j)], 0)
        else:
            dfs([(i, j)], 1)

print(answer)


'''
# 1 bfs로 문제를 풀었다가 실패

from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    visited = [[False]*5 for _ in range(5)]
    visited[i][j] = True

    crew = 1
    y_crew = 0
    global answer

    while queue:
        x, y = queue.popleft()

        if crew == 7:
            answer += 1
            break

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 크루의 수를 세면서 진행
            if y_crew <= 3:
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    crew += 1
                    if board[nx][ny] == 'Y':
                        y_crew += 1
            else:
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and board[nx][ny] == 'S':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    crew += 1

    return 0


board = [list(input()) for _ in range(5)]

answer = 0

# 다솜 파에서 bfs를 시작 → 이렇게 되면 '모든' 경우의 수를 구하기는 어려움.
for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            bfs(i, j)

print(answer)
'''
