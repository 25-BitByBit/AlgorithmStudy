'''
 * 문제 링크: https://www.acmicpc.net/problem/9012
 * 메모리: 32412 KB
 * 시간: 44 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''


def vps(inp):
    stack = []

    for i in inp:
        if i == "(":
            stack.append(i)
        # elif i == ")":
        else:
            # 스택이 비어있는 경우 코드에 오류가 발생하기 때문에 미리 처리
            if len(stack) == 0:
                return "NO"
            stack.pop()

    if stack:
        return "NO"
    return "YES"

N = int(input())
for _ in range(N):
    sentence = list(input())
    # sentence = input().rstrip()
    print(vps(sentence))