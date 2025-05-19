# 1966. 프린터 큐

'''
 * 문제 링크: https://www.acmicpc.net/problem/1966
 * 메모리: 34908 KB
 * 시간: 64 ms
 * 시간 복잡도: O(N²)
 * 공간 복잡도: O(N)

 * 직전에 풀었던 프로세스와 동일한 유형의 문제
 * any와 enumerate를 활용
    * queue에 (문서, 인덱스) 형태로 넣어주고
    * 인덱스가 M인 문서가 출력될 때까지 cnt를 증가시킴
'''

import sys
input = sys.stdin.readline

from collections import deque

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    queue = deque([(q, i) for i, q in enumerate(input_list)])
    cnt = 0

    while queue:
        current = queue.popleft()

        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            cnt += 1
            if current[1] == M:
                print(cnt)
