# 2531. 회전초밥

'''
 * 문제 링크: https://www.acmicpc.net/problem/2531
 * 메모리: 33432 KB
 * 시간: 800 ms
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(N + d)

 * 엠로 코딩테스트 2번과 유사한 문제
    * 마실 수 있는 최대의 음료수 개수
'''

N, d, k, c = map(int, input().split())
input_list = [int(input()) for _ in range(N)]
input_list += input_list[:k - 1]                # 연결되어 있으니까 부족한 k만큼 추가

# 가장 큰 숫자는 9천만. → for 문 2개 돌리면 1억 8천개의 연산이 진행됨.
# → for문을 돌면서 매번 배열을 생성하는 게 아니라 슬라이싱 윈도우를 활용

# 연속된 k개의 초밥의 종류 파악하기
sushi_type = [0] * (d + 1)                  # 스시의 종류별 개수를 담을 리스트
answer = 0

# 쿠폰(c) 초밥 확인
sushi_type[c] += 1
sushi_cnt = 1

for i in range(k):
    if sushi_type[input_list[i]] == 0:      # 처음 등장한 초밥이라면,
        sushi_cnt += 1                      # 초밥 종류 수 추가
    sushi_type[input_list[i]] += 1          # 초밥 갯수 증가

answer = sushi_cnt

# 슬라이딩 윈도우 : 시작 값 빼고 다음 값 추가하기
for j in range(N - 1): # N까지 하면 어차피 처음 값과 같아져서 굳이 할 필요 없음.
    sushi_type[input_list[j]] -= 1
    if sushi_type[input_list[j]] == 0:
        sushi_cnt -= 1
    sushi_type[input_list[k + j]] += 1
    if sushi_type[input_list[k + j]] == 1:
        sushi_cnt += 1

    answer = max(answer, sushi_cnt)

print(answer)

''' 1번째
# 매번 윈도우를 새로 만들고, 중복 제거를 위해 리스트와 in 연산을 사용해서 시간 초과

# 연속된 k개의 초밥의 종류 파악하기
for i in range(N):
    check_sushi = []                        # 시작 초밥을 기준으로 k개를 담기

    for number in range(k):
        if i + number < N:
            check_sushi.append(input_list[i+number])
    # k개의 초밥을 선택 → 최적의 선택인지 확인
    sushi_cnt = 0
    # 중복을 제거해서 초밥의 갯수 확인
    # set_sushi = list(set(check_sushi))
    sushi_list = []
    for sushi in check_sushi:
        if sushi not in sushi_list:
            sushi_list.append(sushi)
            sushi_cnt += 1
    if c not in check_sushi:
        sushi_cnt += 1

    answer = max(answer, sushi_cnt)

print(answer)

'''
