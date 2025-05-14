// 43238. 입국심사

function solution(n, times) {
    var answer = 0;
    
    let start = 0;
    let end = Math.max(...times) * n;
    
    while (start <= end) {
        // mid 시간 동안 처리할 수 있는 사람의 수
        let mid = Math.floor((start + end) / 2);
        let total = 0;
        
        for (t of times) {
            total += Math.floor(mid / t);
            if (total >= n) {
                break;
            }
        }
        
        if (total >= n) {
            answer = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return answer;
}