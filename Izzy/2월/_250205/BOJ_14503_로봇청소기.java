package bfsdfs;

import java.util.*;
import java.io.*;

/**
 * 로봇청소기의 방향 : 동서남북
 *
 * 1. 현재 칸 청소 X -> 청소
 * 2. 다음 칸 이동
 * 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이
 * 2-1. 없는 경우
 * 바라보는 방향 유지
 * 2-1-1. 벽이라 후진X -> 작동 멈춤
 * 2-1-2. 후진 가능 -> 한 칸 후진하고 1번으로 돌아감
 *
 * 2-2. 있는 경우
 * 2-2-1. 반시계 방향으로 90도 회전 -> (방향 이동)
 * - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸이라면 한 칸 전진
 * - 1번으로 돌아감
 *
 * 0 북 1 동 2 남 3 서
 * 청소되지 않은 빈 칸 0
 * 벽 1
 *
 * 청소하는 칸의 개수
 */
'''
 * 문제 링크: https://www.acmicpc.net/problem/9205
 * 메모리: 11864 KB
 * 시간: 72 ms
 * 시간 복잡도: O(NM)
 * 공간 복잡도: O(NM)
'''
public class BOJ_14503_로봇청소기 {
    static int N, M;
    static int[][] map;
    static int answer = 1; //처음 빈칸은 항상 청소되지 않음
    static int[] mover = {-1,0,1,0};
    static int[] movec = {0,1,0,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        //처음 값 초기화
        st = new StringTokenizer(br.readLine());
        int startr = Integer.parseInt(st.nextToken());
        int startc = Integer.parseInt(st.nextToken());
        int startd = Integer.parseInt(st.nextToken());//초기 방향

        //지도 초기화
        map = new int[N][M];
        for(int i=0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j < M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //solve
        simul(startr, startc, startd);

        //print
        System.out.println(answer);
    }

    public static void simul(int r, int c, int d) {
        //1. 현재 칸 청소
        map[r][c] = -1;

        //2. 주변 탐색
        for (int m = 0; m < 4; m++) {
            d = (d + 3) % 4; // 반시계로 90도 이동

            int nr = r + mover[d];
            int nc = c + movec[d];

            if (inRange(nr, nc) &&map[nr][nc] == 0) {
                answer++;
                simul(nr, nc, d);
                return;
            }
        }

        //여기까지 왔다는 것은 위에서 이동할 곳을 찾지 못 했다는 것

        int bd = (d + 2) % 4; //반대방향으로 후진
        int br = r + mover[bd];
        int bc = c + movec[bd];
        if (inRange(br, bc) && map[br][bc] != 1){
            simul(br, bc, d); //방향은 그대로 유지
        }
    }

    public static boolean inRange(int r, int c){
        return (0 <= r && r < N && 0 <= c && c < M);
    }
}
