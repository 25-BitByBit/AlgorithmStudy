'''
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340213
 * 시간 복잡도: O(N)
 * 공간 복잡도: O(1)
'''

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    input_list = []
    input_list = [video_len, pos, op_start, op_end]
    
    # input 값을 int로 변경해주는 과정 필요
    # for i in range(len(input_list)):
    for i, inp in enumerate(input_list):
        minute, second = inp.split(":")
        int_input = int(minute) * 60 + int(second)
        
        input_list[i] = int_input
    
    video_len, pos, op_start, op_end = input_list
    now_play = pos
    
    # 시작할 때 오프닝 포함인지 미리 확인해서 건너뛰기
    def opening(now_play):
        if op_start <= now_play <= op_end:
            return op_end
        return now_play
    
    # 10초 전 함수
    def prev(now_play):
        prev_play = now_play - 10
        if prev_play < 0:
            return 0
                
        # 오프닝 구간 처리
        elif op_start <= prev_play <= op_end:
            return op_end
        return prev_play
    
    
    # 10초 뒤 함수
    def next(now_play):
        next_play = now_play + 10
        if next_play > video_len:
            return video_len
        
        # 오프닝 구간 처리
        elif op_start <= next_play <= op_end:
            return op_end
        return next_play
    
    # 주어진 입력 값 꺼내서 함수 처리
    for command in commands:
        # 안맞던 테스트 케이스 이 함수 추가해서 성공
        now_play = opening(now_play)
        if command == "next":
            now_play = next(now_play)
        else:
            now_play = prev(now_play)
            
        
    # 값을 다시 string 형태로 변환
    if now_play > 0:
        minute = now_play // 60
        second = now_play % 60
        # answer += (minute + ":" + second)
        answer = f"{minute:02}:{second:02}"
    else:
        answer = "00:00"
    
    return answer