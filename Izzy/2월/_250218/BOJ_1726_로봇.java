package bfsdfs;

import java.util.*;
import java.io.*;

/**
 * 동(1), 서(2), 남(3), 북(4)
 * 명령은 2가지
 * 1. Go k : k는 1,2,3 현재 향하고 있는 방향으로 k만큼 회전
 * 2. Turn dir : dir은 left 또는 right이며 각각 왼쪽, 오른쪽으로 90도 회전(오른쪽 회전, 왼쪽 회전, 회전x)
 *
 *
 * 2번 명령 먼저 하고 그 이후 1번 명령을 내린다.
 *
 * 0 : 로봇 이동 가능
 * 1 : 로봇 이동 불가능
 *
 * 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한가?
 */

'''
 * 문제 링크: https://www.acmicpc.net/problem/1726
 * 메모리: 12372 KB
 * 시간: 84 ms
 * 시간 복잡도: O(NM)
 * 공간 복잡도: O(NM)
 * 
 * 1. 시작점에서 bfs 돌림
 * 2. 거리 1,2,3 이동시키기
 * 3. 방향 회전하기 
'''
public class BOJ_1726_로봇 {
    static int N,M;
    static int[][] map;
    static boolean[][][] visited;
    static int endR, endC, endD;
    static int[] mover = {0,0,1,-1};
    static int[] movec = {1,-1,0,0};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for(int i=0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j < M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //solve
        st = new StringTokenizer(br.readLine());
        int startR = Integer.parseInt(st.nextToken())-1;
        int startC = Integer.parseInt(st.nextToken())-1;
        int startD = Integer.parseInt(st.nextToken())-1;

        st = new StringTokenizer(br.readLine());
        endR = Integer.parseInt(st.nextToken())-1;
        endC = Integer.parseInt(st.nextToken())-1;
        endD = Integer.parseInt(st.nextToken())-1;

        bfs(startR, startC, startD);

        //print
        System.out.println(answer);
    }

    public static void bfs(int r, int c, int dir){
        Queue<int[]> q = new ArrayDeque<>();
        visited = new boolean[N][M][4]; //방향 4가지
        q.add(new int[]{r,c,dir, 0});
        visited[r][c][dir] = true;

        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int cr = tmp[0];
            int cc = tmp[1];
            int cd = tmp[2];
            int cnt = tmp[3]; //명령 카운트

            //도착지에 도착했으면 끝
            if(cr == endR && cc == endC && cd == endD){
                answer = cnt;
                return;
            }

            //이동하기
            for(int dist=1; dist <=3; dist++){
                int nr = cr + (dist*mover[cd]);
                int nc = cc + (dist*movec[cd]);
                if(nr < 0 || nr >= N || nc <0 || nc >= M) continue;
                if(visited[nr][nc][cd]) continue;
                if(map[nr][nc] == 1) break;
                //한칸씩 이동하는 칸을 늘려가는 것
                //우리는 벽을 뛰어넘을 수 없으니 중간에 벽을 만나면 무조건 멈춰야 한다.
                q.add(new int[]{nr,nc,cd,cnt+1});
                visited[nr][nc][cd] = true;
            }

            //방향 바꾸기
            int left = 0, right = 0;
            switch(cd){
                case 0 : left = 3; right = 2; break;
                case 1 : left = 2; right = 3; break;
                case 2 : left = 0; right = 1; break;
                case 3 : left = 1; right = 0; break;
            }

            if(!visited[cr][cc][left]){
                q.add(new int[]{cr,cc,left, cnt+1});
                visited[cr][cc][left] = true;
            }

            if(!visited[cr][cc][right]){
                q.add(new int[]{cr,cc,right, cnt+1});
                visited[cr][cc][right] = true;
            }


        }

    }
}
