# 42862. 체육복

'''
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)
'''

def solution(n, lost, reserve):
    answer = 0
    
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)

    clothes_list = [1] * (n + 1)
    # 도난당한 체육복 반영
    for l in real_lost:
        clothes_list[l] = 0
    
    # 빌려줄 수 있는 체육복 채우기
    for r in real_reserve:
        # 일단 내꺼가 없으면 그것부터 채우기
        # if clothes_list[r] == 0:
        #     clothes_list[r] = 1
        #     for i in range(len(reserve)):
        #         if reserve[i] == r:
        #             reserve.discard(r)
        # 다른 친구에게 빌려줄 수 있는 경우
        # else:
        if r > 1 and clothes_list[r - 1] == 0:
                clothes_list[r - 1] = 1
                continue
        elif r < n and clothes_list[r + 1] == 0:
            clothes_list[r + 1] = 1
            continue
    
    for c in range(1, n + 1):
        if clothes_list[c] == 1:
            answer += 1
    
    return answer