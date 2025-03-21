# 2877. 4와 7

'''
 * 문제 링크: https://www.acmicpc.net/problem/2877
 * 메모리: 32412 KB
 * 시간: 32 ms
 * 시간 복잡도: O(log K)
 * 공간 복잡도: O(log K)

 * 엠로 코딩테스트 4번과 유사한 문제
    * a와 b로 이루어진 수열에서 K번째 수를 찾는 문제
'''


def check_num(a, b, K):
    answer = ''
    while K > 0:            
        l = K % 2                   # 짝수, 홀수 판단 → 현재 K의 마지막 비트(짝수/홀수)를 확인
        K = K // 2                  # K를 2로 나누어 다음 비트로 이동
        if l == 0:                  # 짝수인 경우, 
            K -= 1                  # 4, 7을 번갈아가며 사용해야 하므로, 짝수인 경우 1을 빼고 7로 대체      
            answer = b + answer     # 7을 앞에 붙임
        else:                       # 홀수인 경우,  
            answer = a + answer     # 4를 앞에 붙임

    print(answer)

K = int(input())
check_num('4', '7', K)