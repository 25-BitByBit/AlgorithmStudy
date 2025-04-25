# 9742. 순열

'''
 * 문제 링크: https://www.acmicpc.net/problem/9742
 * 메모리: 32412 KB
 * 시간: 732 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''

from itertools import permutations

while True:
    try:
        text, num = input().split()
        num = int(num)

        cnt = 0
        flag = False

        for p in permutations(text, len(text)):
            cnt += 1
            if cnt == num :
                print(text, num, '=', ''.join(p))
                flag = True
                break

        if not flag:
            print(text, num, '=', 'No permutation')

    except EOFError:
        break
