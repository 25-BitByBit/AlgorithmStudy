# 2138. 전구와 스위치

'''
 * 문제 링크: https://www.acmicpc.net/problem/2138
 * 메모리: 35544 KB
 * 시간: 88 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N)

 * i-1 번째 전구를 최우선으로 생각하기
    * i-1 번째 전구가 다르다면 누르기, 맞으면 그냥 넘어가기
 * 마지막 2개의 값이 남았을 때, 내가 스위치를 눌러서 값이 맞으면 정답을 만들 수 있는 것. 아니면 -1
'''

import sys
input = sys.stdin.readline

def check_switch(check_list):
    cnt = 0

    for i in range(1, N-1):
        # 스위치를 누르지 않는 경우
        if check_list[i - 1] == target_list[i - 1]:
            continue
        # 스위치를 누르는 경우
        else:
            cnt += 1
            convert_switch(i, check_list)

    # N번째 확인하면 끝!
    if check_list[N-2] == target_list[N-2] and check_list[N-1] == target_list[N-1]:
    # if check_list[N-1] == target_list[N-1]:
        return cnt
    elif check_list[N-2] != target_list[N-2]:
        cnt += 1
        convert_switch(N-2, check_list)

        if check_list[N-2] == target_list[N-2] and check_list[N-1] == target_list[N-1]:
            return cnt
        return -1
    
    # 이 부분에서 에러처리가 제대로 되지 않아 n-2 값이 같고, n-1 값이 다른 경우에 그냥 if문을 빠져나오면서 return이 없는 none 상태가 됨.
    # 이 상태에서 아래에서 값을 +1 하다보니 오류가 발생!
    else:
        return -1



def convert_switch(idx, convert_list):
    if idx - 1 >= 0:
        if convert_list[idx - 1] == '1':
            convert_list[idx - 1] = '0'
        else:
            convert_list[idx - 1] = '1'

    if convert_list[idx] == '1':
        convert_list[idx] = '0'
    else:
        convert_list[idx] = '1'

    if idx + 1 < N:
        if convert_list[idx + 1] == '1':
            convert_list[idx + 1] = '0'
        else:
            convert_list[idx + 1] = '1'


N = int(input())
# input_list = list(map(int, input().split()))
input_list = list(input().rstrip())
target_list = list(input().rstrip())

# switch_input_list = input_list
case1_input_list = input_list[:]
case2_input_list = input_list[:]


# 시작 시점에서 스위치를 누르고 시작 or 안 누르고 시작 2가지 경우
# case 1 : 안 누르고 시작
case1 = check_switch(case1_input_list)

# case 2: 누르고 시작
convert_switch(0, case2_input_list)

case2 = check_switch(case2_input_list)
if case2 != -1:
    case2 += 1

if case1 >= 0 and case2 >= 0:
    answer = min(case1, case2)
elif case1 == -1:
    answer = case2
elif case2 == -1:
    answer = case1
else:
    answer = -1

print(answer)