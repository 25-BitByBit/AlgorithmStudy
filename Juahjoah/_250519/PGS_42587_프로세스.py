# 42587. 프로세스

'''
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
 * 시간 복잡도: O(N²)
 * 공간 복잡도: O(N)

 * 다른 사람의 풀이를 참고하여 any()를 활용한 방법으로 구현
    * deque의 다양한 활용 방식 파악
    * any()를 활용하여 queue에 있는 값 중 현재 값보다 큰 값이 있는지 확인
        * queue에 있는 값 중 현재 값보다 큰 값이 있으면 append()로 다시 넣어주고
        * 없으면 answer를 1 증가시키고, 현재 값의 인덱스가 location과 같으면 answer를 return
'''

# 2
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        
        else:
            answer += 1
            if current[1] == location:
                return answer
    
    return answer


# 1
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    # queue = deque([priorities])
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    while queue:
        current = queue.popleft()
        find_queue = False
        
        for q in queue:
            if current[0] < q[0]:
                find_queue = True
                break
                
        if find_queue:
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer
    
    return answer
'''