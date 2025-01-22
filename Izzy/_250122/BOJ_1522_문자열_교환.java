
'''
 * 문제 링크: https://www.acmicpc.net/problem/1522
 * 메모리: 11496 KB
 * 시간: 68 ms
 * 시간 복잡도: O(N²)
 * 공간 복잡도: O(N)


1. 주어진 단어 안의 a의 갯수 구하기
2. 단어를 a의 갯수만큼 쪼개서 for문을 돌음
    2-1. 내부에 b의 갯수를 센다. 
    2-2. 가장 작은 b의 갯수를 반환
'''

package boj;

import java.util.*;
import java.io.*;

public class BOJ_1522_문자열_교환 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int aCnt = 0;
        int answer = Integer.MAX_VALUE;

        //1. 단어 안의 a의 갯수 구하기
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(c == 'a') aCnt++;
        }

        //2 str의 내부의 a의 갯수만큼 자릿수를 자른다.
        //슬라이딩 윈도우를 사용해서 그 자릿수 내부에 b의 개수가 몇 개인지 센다.
        for(int i=0; i < str.length(); i++){
            int bCnt = 0;
            for(int j=i; j<i+aCnt; j++){//슬라이딩 윈도우
                if(str.charAt((j+str.length()) % str.length()) == 'b') bCnt++;
            }
            answer = Math.min(answer, bCnt);
        }

        //출력
        System.out.println(answer);
    }
}
