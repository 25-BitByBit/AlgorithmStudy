'''
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43238
 * 공간 복잡도: O(1)

'''

def solution(n, times):
    left = 0
    right = max(times) * n
    
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 처리할 수 있는 사람
        total = 0
        for t in times:
            total += mid // t
            # n을 초과했다면 중지
            if total>= n:
                break
                
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer