
'''
 * 문제 링크: https://www.acmicpc.net/problem/2805
 * 메모리: 258500 KB
 * 시간: 444 ms
 * 시간 복잡도: O(N log(max(tree)))
 * 공간 복잡도: O(N)

'''

N, M = map(int, input().split())
tree = list(map(int, input().split()))

left = 0
# right = 10 ** 11
right = max(tree)

H = 0

# 이진 탐색
while left <= right:
    mid = (left + right) // 2

    # 조건을 충족할 수 있게 만드는 코드 구현
    cutting = 0

    for i in range(N):
        if tree[i] > mid:                   # 나무가 절단기 높이보다 높은 경우만 (아니면 - 값이 들어갈 수 있음.)
            cutting += (tree[i] - mid)

    # 필요한 나무 길이 M 이상을 얻을 수 있는 경우
    if cutting >= M:                        # 가능한 절단기 높이 업데이트
        # left = high
        H = mid
        left = mid + 1                      # 더 높은 절단기 높이를 탐색 (더 길게 자르기 가능)
    else:
        right = mid - 1                     # 필요한 나무가 부족하므로 절단기 높이를 낮춤

print(H)