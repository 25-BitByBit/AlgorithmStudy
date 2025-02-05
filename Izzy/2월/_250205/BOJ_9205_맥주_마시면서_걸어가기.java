package bfsdfs;

import java.util.*;
import java.io.*;

/**
 * 문제 요약
 * 송도(상근이네 집) -> 펜타포트 락 페스티벌
 * 맥주 한 박스(20개) 들고 출발
 * 50m에 한 병씩 마신다. 50m 가려면 직전에 한 병 마심
 * 편의점에서 빈 병은 버리고 새 맥주 병 살 수 있음. 단 상자의 맥주는 20병을 넘을 수 없음
 *
 * 행복하게 페스티벌에 갈 수 있다면 "happy"
 * 중간에 맥주가 바닥나면 "sad"
 */

/**
 * 그냥 정점, 간선이 있는 그래프 형태라고 생각하기
 * 편의점, 맥주라는 조건이 있지만 사실 이 부분은 큰 의미가 없다
 * 도착지 외에 편의점을 경유하고, 편의점에 들리기만 하면 병 20개를 채울 수 있음
 * 병의 갯수와 상관없이 현재 위치에서 다음위치까지 맨해튼 거리가 1000이하이면 항상 이동 가능
 * 1000인 이유는 50m * 20병 = 1000 이기 때문
 */

'''
 * 문제 링크: https://www.acmicpc.net/problem/9205
 * 메모리: 12656 KB
 * 시간: 88 ms
 * 시간 복잡도: O(TN)
 * 공간 복잡도: O(N)

1. place에 위치 집어넣기
2. BFS 돌리면서 탐색
    2-1. 맨해튼 거리가 1000이하이면 이동 가능
    2-2. 방문한 곳은 이동 금지
    2-3. 도착지에 도착하면 "happy" 실패하면 "sad"

'''
public class BOJ_9205_맥주_마시면서_걸어가기 {
    static int convenience_cnt;
    static Point[] places;
    static String answer;
    static int MIN_DISTANCE =  -32768;
    static int MAX_DISTANCE =  32768;
    static boolean[] visited;

    static class Point {
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for(int tc = 0; tc < T ; tc++){
            answer = "sad";
            //input값 입력
            convenience_cnt = Integer.parseInt(br.readLine());
            places = new Point[convenience_cnt+2];

            for(int i=0; i < convenience_cnt+2; i++){
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                places[i] = new Point(r,c);
            }
            //solve
            BFS(places[0].r, places[0].c);

            //print
            System.out.println(answer);
        }
    }
    //함수
    public static void BFS(int r, int c){
        visited = new boolean[convenience_cnt+2];
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(r,c));
        visited[0] = true; //출발지 등록

        while(!q.isEmpty()){
            Point now = q.poll();

            for(int i=1; i < convenience_cnt+2; i++){
              if(visited[i]) continue; //방문했다면
              if(!passable(now, places[i])) continue;//멘하튼 거리 내에 없으면
              if(i == convenience_cnt+1) {
                  answer = "happy";
                  return;
              }
                q.add(new Point(places[i].r,places[i].c));
                visited[i] = true;
            }

        }

    }
    static public boolean passable(Point a, Point b) {
        int distance = Math.abs(a.r - b.r) + Math.abs(a.c - b.c);
        if (distance <= 1000) {
            return true;
        } else {
            return false;
        }
    }
}
