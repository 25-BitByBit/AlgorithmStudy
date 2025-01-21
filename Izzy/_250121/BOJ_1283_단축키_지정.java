
'''
 * 문제 링크: https://www.acmicpc.net/problem/1283
 * 메모리: 11576 KB
 * 시간: 68 ms
 * 시간 복잡도: O(N*L)
 * 공간 복잡도: O(N)


1. N으로 for문으로 돌음
2. 단어의 첫번째 알파벳을 사용했는지 안 했는데 탐색
3. 2번의 경우를 다 돌았는데도 찾지 못 하면 각각의 알파벳을 탐색
3. StringBuilder로 출력 처리
'''

package boj;

import java.util.*;
import java.io.*;

/**
 * 1. 왼쪽부터 살핌. 단어의 첫 글자를 단축키로 지정
 * 1-1. 단어의 첫 글자가 이미 선택-> 그 다음 단어의 첫 글자 선택
 * 1-2. 1-1에도 안 된다. 다시 맨 왼쪽의 단어로 돌아와서 이미 선택된 것을 제외하고
 * 선택되지 않은 알파벳을 선택한다.
 * 2. 대소문자 구분 안 함
 *
 */
public class BOJ_1283_단축키_지정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());
        boolean[] alpha = new boolean[26]; //알파벳이 선택되었는지

        String[][] word = new String[N][5];
        for(int i=0; i < N; i++){//옵션
            String s = br.readLine();
            String[] tmp = s.split(" ");

            boolean flag = false; //이미 다 첫 번째 단어를 사용했는지
            for(int j = 0; j < tmp.length; j++){ //단어의 갯수만큼 돈다
                word[i][j] = tmp[j];
                if(!flag && !alpha[Character.toLowerCase(tmp[j].charAt(0))-'a']){
                    //사용되지 않은 단어
                    word[i][j] = "["+tmp[j].charAt(0)+"]"+tmp[j].substring(1,tmp[j].length());
                    alpha[Character.toLowerCase(tmp[j].charAt(0))-'a'] = true;
                    flag = true;
                }
            }
//            System.out.println(Arrays.deepToString(word));

            if(!flag){
                //true가 아니라는 것은 첫 번째 단어의 첫번째 알파벳들이 이미 다 선택됨
                outer : for(int j = 0; j < tmp.length; j++){
                    for(int k= 0 ; k < tmp[j].length(); k++){
                        char c = tmp[j].charAt(k);
                        char lc = Character.toLowerCase(c);
                        if(!alpha[lc-'a']){
                            //사용 안 됨
                            word[i][j] = tmp[j].substring(0, k)+"["+c+"]"+tmp[j].substring(k+1, tmp[j].length());
                            alpha[lc-'a'] = true;
                            break outer;
                        }
                    }
                }
            }
        }
//        System.out.println(Arrays.deepToString(word));
        //출력
        StringBuilder sb = new StringBuilder();

        for(int i =0 ; i < N; i++){
            for(int j=0; j < 5; j++){
                if(word[i][j] == null) continue;
                sb.append(word[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }
}
