package bfsdfs;

import java.util.*;
import java.io.*;

/**
 * D : n을 두 배로 바꾼다. 결과값이 9999보다 큰 경우 10000으로 나눈 나머지로 취한다.
 * S : n-1, n이 0이면 9999가 저장
 * L : n의 각 자릿수를 왼편으로 회전시켜서 저장
 * d2,d3,d4,d1
 * R : n의 각 자릿수를 오른편으로 회전시켜서 저장
 * d4,d1,d2,d3
 *
 * A를 B로 바꾸는 최소한의 명령어를 생성
 * 자릿수에 0이 포함되는 경우를 주의해라
 *
 */

'''
 * 문제 링크: https://www.acmicpc.net/problem/9019
 * 메모리: 298336 KB
 * 시간: 3476 ms
 * 시간 복잡도: O(VE)
 * 공간 복잡도: O(V)
'''

public class BOJ_9019_DSLR {
    static int B;
    static final int MAX = 10_000;
    static boolean[] visited;
    static String answer = "";

    static class Node {
        int number;
        String str;

        public Node(int number, String str) {
            this.number = number;
            this.str = str;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for(int tc = 0; tc < T ; tc++){
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            bfs(A);

            System.out.println(answer);
        }
    }

    public static void bfs(int A){
        Queue<Node> q = new ArrayDeque<>();
        visited = new boolean[MAX+1];

        q.add(new Node(A, ""));
        visited[A] = true;

        while(!q.isEmpty()){
            Node n = q.poll();
            int now = n.number;
            String str = n.str;

            if(now == B) {
                answer = str;
                return;
            }

            int D = (2 * now) % 10000;
            int S = now == 0 ? 9999 : now - 1;
            int L = (now % 1000) * 10 + now / 1000;
            int R = (now % 10) * 1000 + now / 10;

            if (!visited[D]) {
                q.add(new Node(D, str+"D"));
                visited[D] = true;
            }

            if (!visited[S]) {
                q.add(new Node(S, str+"S"));
                visited[S] = true;
            }

            if (!visited[L]) {
                q.add(new Node(L, str+"L"));
                visited[L] = true;
            }

            if (!visited[R]) {
                q.add(new Node(R, str+"R"));
                visited[R] = true;
            }
        }

    }
}
