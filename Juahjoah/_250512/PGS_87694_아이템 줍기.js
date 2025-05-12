// 87694. 아이템 줍기

/*
 * 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87694

*/

function bfs(map, startX, startY, endX, endY) {
    const dx = [0, -1, 0, 1];
    const dy = [1, 0, -1, 0];
    let visited = Array.from({length : map.length}, () => Array(map[0].length).fill(false));
    
    let queue = [];
    queue.push([startX, startY, 0]);
    visited[startX][startY] = true;
    
    while (queue.length) {
        let [x, y, cnt] = queue.shift();
        
        if (x === endX && y === endY) {
            return cnt;
        }
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if (0 <= nx && nx < map.length && 0 <= ny && ny < map[0].length && !visited[nx][ny] && map[nx][ny] === 1) {
                queue.push([nx, ny, cnt + 1]);
                visited[nx][ny] = true;
            }
        }  
    }
}

function solution(rectangle, characterX, characterY, itemX, itemY) {
    let answer = 0;
    const size = 102;
    
    // 이동할 수 있는 구역을 1로 표시한 배열
    let map = Array.from({length : size}, () => Array(size).fill(0));
    
    // map을 채우기
    for (let [x1, y1, x2, y2] of rectangle) {
        for (let i = x1 * 2; i <= x2 * 2; i++) {
            for (let j = y1 * 2; j <= y2 * 2; j++) {
                map[i][j] = 1;
            }
        }
    }
    
    for (let [x1, y1, x2, y2] of rectangle) {
        for (let n = x1 * 2 + 1; n < x2 * 2; n++) {
            for (let m = y1 * 2 + 1; m < y2 * 2; m++) {
                map[n][m] = 0;
            }
        }
    }
    
    answer = bfs(map, characterX * 2, characterY * 2, itemX * 2, itemY * 2) / 2
    
    return answer;
}