'''
 * 문제 링크: https://www.acmicpc.net/problem/1487
 * 메모리: 32412 KB
 * 시간: 36 ms
 * 시간 복잡도: O(N²)
 * 공간 복잡도: O(N)
'''


# 최대 이익 제공하는 최적의 판매 가격을 반환하는 함수
def find_price():
    max_profit = 0          # 최대 이익을 저장할 변수
    best_price = 0          # 최적 판매 가격을 저장할 변수

    # 모든 구매자의 지불 가능 금액을 판매 가격 후보로 설정
    for price in [p[0] for p in consumer_list]:
        profit = 0          # 이익을 이 단계에서 초기화 = 그래야 금액 별로 이익을 파악 가능
        for max_price, delivery_fee in consumer_list:
            if price <= max_price:                      # 구매자가 해당 금액에 구매할 수 있는 경우,
                benefit = price - delivery_fee
                if benefit > 0 :                        # 이익이 양수인 경우에만 이익으로 고려
                    profit += benefit

        # 최대 이익을 계산하고, 이익이 동일하다면 낮은 가격 선택
        if profit > max_profit:
            max_profit = profit
            best_price = price
        elif profit == max_profit and price < best_price:
            best_price = price

    # 이익이 없는 경우 0을 반환
    if max_price == 0:
        return 0

    return best_price

N = int(input())
consumer_list = [list(map(int, input().split())) for _ in range(N)]

# 지불할 최대 가격, 배송비가 낮은순으로 정렬
consumer_list.sort(key = lambda x:(x[0], x[1]))


print(find_price())

