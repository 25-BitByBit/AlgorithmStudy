'''
 * 문제 링크: https://www.acmicpc.net/problem/4949
 * 메모리: 32412 KB
 * 시간: 220 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''

def vps(sentence):
    stack = []

    for inp in sentence:
        if inp == '(' or inp == '[':
            stack.append(inp)
        elif inp == ')':
            if not stack:
                return 'no'
            elif stack[-1] == '(':
                stack.pop()
            else:
                return 'no'

        elif inp == ']':
            if not stack:
                return 'no'
            elif stack[-1] == '[':
                stack.pop()
            else:
                return 'no'

    if stack:
        return 'no'
    return 'yes'

while True:
    sentence = list(input())
    if sentence == ['.']:
        break

    print(vps(sentence))
