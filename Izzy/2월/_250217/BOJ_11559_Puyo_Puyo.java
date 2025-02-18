package bfsdfs;

import java.util.*;
import java.io.*;

/*
. : 빈공간
R : 빨강 / G : 초록 / B : 파랑 / P : 보라 / Y : 노랑
입력으로 주어진 것은 뿌요들이 전부 아래로 떨어진 뒤의 상황

1. for문 돌면서 색이 들어간 칸을 찾음
BFS돌려서 4개 이상 터지는 칸을 bomb에 집어넣음
2. bomb의 사이즈가 4개 이상이면 색을 .으로 바꿈
3. 한 depth가 돌아가면 부셔진 것들이 있으니, 아래로 이동시켜주기
 */

'''
 * 문제 링크: https://www.acmicpc.net/problem/11559
 * 메모리: 11864 KB
 * 시간: 68 ms
 * 시간 복잡도: O(NM)
 * 공간 복잡도: O(NM)
'''
public class BOJ_11559_Puyo_Puyo {
    static final int N = 12;
    static final int M = 6;
    static char[][] map = new char[N][M];
    static int[] mover = {0,0,-1,1};
    static int[] movec = {-1,1,0,0};
    static Queue<int[]> bomb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0; i < N; i++){
            String str = br.readLine();
            for(int j=0; j < M; j++){
                map[i][j] = str.charAt(j);
            }
        }
        //solve
        int answer = 0;
        while(true){
            boolean flag = false;
            for(int i=0; i < N; i++){
                for(int j=0; j < M; j++){
                    if(map[i][j] != '.') {//색이 있다면
                        bfs(i, j, map[i][j]);

                        if (bomb.size() >= 4) {
                            while(!bomb.isEmpty()){
                                int[] tmp = bomb.poll();
                                map[tmp[0]][tmp[1]] = '.';
                            }
                            flag = true;
                        }
                    }
                }
            }
            if(!flag) break; //더 이상 터질게 없음
            //내려주기
            moveDown();
            answer++;
        }

        //print
        System.out.println(answer);
    }



    static public void moveDown(){
        //아래로 이동시켜주기

        for(int j = 0; j < M; j++){
            Stack<Character> s = new Stack<>();
            for(int i=0; i < N; i++){
                if(map[i][j] != '.'){
                    //stack에 넣고 초기화
                    s.push(map[i][j]);
                    map[i][j] = '.';
                }
            }

            if(s.size() != 0){
                for(int i = N-1; i >= 0 ; i--){
                    if(s.isEmpty()) break;
                    char c = s.pop();
                    map[i][j] = c;
                }
            }
        }


    }

    static public void bfs(int r, int c, char color){
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];
        bomb = new ArrayDeque<>();

        q.add(new int[]{r,c});
        bomb.add(new int[]{r,c});
        visited[r][c] = true;

        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int cr = tmp[0];
            int cc = tmp[1];


            for(int m =0; m < 4; m++){
                int nr = cr + mover[m];
                int nc = cc + movec[m];

                if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                if(visited[nr][nc]) continue;
                if(map[nr][nc] == color){
                    visited[nr][nc] = true;
                    q.add(new int[]{nr,nc});
                    bomb.add(new int[]{nr,nc});
                }
            }
        }
    }
}
