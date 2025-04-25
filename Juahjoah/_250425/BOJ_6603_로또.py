# 6603. 로또

'''
 * 문제 링크: https://www.acmicpc.net/problem/6603
 * 메모리: 32412 KB
 * 시간: 36 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''

from itertools import combinations

while True:
    input_num = input().split()
    # 여기서 input을 list로 받기 때문에 [0]으로 확인해야 정상 작동 (런타임에러 유의!)
    if input_num[0] == '0':
        break

    K = int(input_num[0])
    S = input_num[1:]

    for i in combinations(S, 6):
        print(' '.join(i))
    print()
