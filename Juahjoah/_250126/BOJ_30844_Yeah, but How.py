'''
 * 문제 링크: https://www.acmicpc.net/problem/30844
 * 메모리: 34364 KB
 * 시간: 76 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

 1. 애초에 균형 잡힌 괄호 문자열이 주어짐 = 잘못된 괄호 문자열이 주어지는 일은 없음.
 2. 괄호들 사이에 적절하게 1과 +를 넣어 줘야 함.

'''

def vps(sentence):
    answer = ''

    for inp in sentence:
        if inp == '(':
            if answer:
                if answer[-1] == '(':
                    answer += inp
                elif answer[-1] == ')':
                    answer += '+'
                    answer += inp
            else:
                answer += inp
        else:
            if answer[-1] == '(':
                answer += '1'
                # answer += '1+1'
                answer += inp
            else:
                answer += inp

    return answer

sentence = list(input())
print(vps(sentence))


