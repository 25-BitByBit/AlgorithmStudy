'''
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389479
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(1)
'''

# 주어진 players를 돌면서 각 시간에 맞는 유저의 수 확인 & 서버 개수 확인
# k를 cnt_user에 어떻게 반영할 것인가?

import math

def solution(players, m, k):
    answer = 0
    
    server_list = [1] * 24

    # for p in players:
    for i in range(24):
        # m * server_list[i] - 1: 현재 시간대에서 서버에서 감당 가능한 사용자 수
        cnt_server = math.ceil((players[i] - (m * server_list[i] - 1)) / m)
        if cnt_server > 0:              # 서버가 필요한 경우에는
            answer += cnt_server
            # 각 시간대에 늘어난 서버의 개수 정보를 저장해주기
            for j in range(i, i+k):
                if j >= 24:
                    break
                server_list[j] += cnt_server

    return answer