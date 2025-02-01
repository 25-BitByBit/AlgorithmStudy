'''
 * 문제 링크: https://www.acmicpc.net/problem/16236
 * 메모리: 35036 KB
 * 시간: 64 ms
 * 시간 복잡도: O(N³) ~ O(N⁴)
 * 공간 복잡도: O(N²)

 * 다양한 조건을 놓치지 않는 것이 관건인 문제

 * 먹을 수 있는 물고기의 거리를 확인하는 과정도 bfs에서 내부에 진행하는 것이 탐색에 가장 최적화된 방식
    = 나를 기준으로 너비 우선 탐색을 돌렸을 때, 물고기가 먹을 수 있는 여러 마리인 경우 같은 거리 상에서 처음 만난 물고기를 먹어야 함. = 선별하는 과정
 * bfs 내부에서는 거리에 대한 탐색만 진행. 위치를 변경하는 것, 크기를 키우는 것 등 이외의 문제는 모두 bfs 밖에서 진행
    * 물고기 선별은 bfs 내부에서 진행. 이외의 작업은 전부 bfs 외부
'''

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(cx, cy):
    queue = deque()
    queue.append((cx, cy))
    visited = [[False] * N for _ in range(N)]
    visited[cx][cy] = True

    move = 0 # 거리 변수
    move_list = []

    while queue:
        move += 1
        # for문을 활용해 이동한 거리를 측정
        for q in range(len(queue)):

            x, y = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] <= size:
                    # 적어도 이동할 수는 있는 자리
                    visited[nx][ny] = True

                    # 먹을 수 있는지, 없는지 판단
                    if 0 < board[nx][ny] < size:
                        move_list.append((nx, ny))          # 먹을 수 있는게 여러 개인 경우를 판단하기 위해 일단 값을 저장
                    else:                                   # 먹을 수 없다면, 그냥 이동
                        queue.append((nx, ny))

        # 먹을 수 있는 물고기가 있다면 값을 변경
        if move_list:
            move_list.sort(key=lambda x:(x[0], x[1]))
            return list(move_list[0]) + [move]

    # 먹을 수 있는 물고기가 없는 경우 - 물고기 없는 경우, 큰 물고기만 있는 경우 = while문을 다 돌아서 찾지 못한 경우.
    return [-1, -1, move]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

size = 2
fish_cnt = 0

cx = 0
cy = 0
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            cx, cy = i, j

while True:
    # 물고기의 위치, 거리를 반환
    fx, fy, move = bfs(cx, cy)

    # 먹을게 없는 경우에 종료
    if fx == -1:
        break

    # 물고기를 잡아 먹는 과정
    board[fx][fy] = 9
    board[cx][cy] = 0
    fish_cnt += 1
    cx, cy = fx, fy

    # 물고기 크기 키우기
    if fish_cnt == size:
        fish_cnt = 0
        size += 1

    answer += move

print(answer)