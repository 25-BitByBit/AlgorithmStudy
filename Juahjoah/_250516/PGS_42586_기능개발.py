# 42586. 기능 개발

def solution(progresses, speeds):
    answer = []
    days = 0
    cnt = 0
    
    while progresses:
        # 시간을 계산해서 맨 앞에 값을 확인하기
        if (progresses[0] + days * speeds[0]) >= 100:
            # 작업 끝나면 리스트에서 제거하기
            progresses.pop(0)
            speeds.pop(0)
            
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:  # 완료된 기능이 없는 경우에는 날짜 + 1
                days += 1
                
    answer.append(cnt)
    
    return answer