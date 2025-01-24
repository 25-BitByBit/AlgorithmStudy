'''
 * 문제 링크: https://softeer.ai/practice/9657
 * 메모리: 37.53 MB
 * 시간: 0.108 초
 * 시간 복잡도: O(N*M) / 5줄 2번 도는 for문을 돌게 됨. (10+N)*M
 * 공간 복잡도: O(N*M)

1. 문제에서 요구하는 방식대로 for문을 구현
    1-1. board의 인덱스는 0부터, 입력값은 1부터 시작하기 때문에 -1을 함.
2. 남은 환경 파괴범의 숫자를 확인하기 위해 for문을 돌며 1의 개수를 확인
'''

import sys

# N, M = map(int, input().split())
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(N)]

L1, R1 = map(int, input().split())
L2, R2 = map(int, input().split())

answer = 0

for i in range(L1-1, R1):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j] = 0
            break

for k in range(L2-1, R2):
    for l in range(M):
        if board[k][l] == 1:
            board[k][l] = 0
            break

# 보드를 탐색하며 남은 환경 파괴범의 숫자을 확인
# 미리 숫자를 세두고 위에서 for문을 돌릴 때마다 숫자도 빼줬다면, 좀 더 효율적인 코드 작성이 가능할 것이라고 생각
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            answer += 1

print(answer)