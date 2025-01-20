# 🖥️ AlgorithmStudy

## 🤖 스터디 멤버

<!--- 스택 뱃지 -->
<!---
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><br/>
<img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white"><br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
--->
<table>
 <tr>
    <td align="center"><a href="https://github.com/Juahjoah"><img src="https://avatars.githubusercontent.com/Juahjoah" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/izzy80"><img src="https://avatars.githubusercontent.com/izzy80" width="130px;" alt=""></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Juahjoah"><b>Juahjoah</b></a></td>
    <td align="center"><a href="https://github.com/izzy80"><b>izzy80</b></a></td>
  </tr>
  <tr> 
    <td align="center"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><br/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"><br/>
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>
    </td>
    <td align="center"><img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white"><br/>
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>
    </td>
  </tr> 
</table>

<br/>

## 📌 스터디 규칙

- 1주 5알고리즘 -> 무조건 🔥🔥🔥
- 불이행시 다음번에 문제 더 풀기 

<br/>

## 🔍 참여 방법

1. 생성된 저장소에 `Github ID`로 폴더를 생성한다.
2. 알고리즘 풀이 후 원본 저장소에 `PR`를 보낸다.

<br/>

## 📁 Repository 폴더 구조

```
{Github ID}/{날짜}/{코드.java}
```

- 💡 예시: `izzy80/_240701/PGS_소수_찾기.java`

<br/>

## 📝 코드 작성 가이드

[](https://github.com/Ogu-Family/algorithm#-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1-%EA%B0%80%EC%9D%B4%EB%93%9C)

풀이 코드와 함께 아래의 내용을 주석으로 작성합니다.

-   코드 앞 부분에 문제 링크 / 메모리 / 시간 / 시간복잡도 / 공간복잡도 작성
-   주요 알고리즘과 문제에서 중요한 부분 설명
-   필요한 경우 코드 내에 주석 추가
```
/**
 * 문제 링크: https://www.acmicpc.net/problem/1000
 * 메모리: 14448 KB
 * 시간: 132 ms
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(1)
 */

/*
1. 두 정수 A와 B를 입력받은 후
2. A+B 계산
3. 결과 출력
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        // 입력을 받아 공백으로 분리
        String[] input = bufferedReader.readLine().split(" ");

        // 분리 된 문자열을 정수로 변환
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);

        System.out.println(a + b);
    }
}
```


## ⚠️ commit 컨벤션

```
{태그}: {클래스 이름(플랫폼_문제 번호_문제 제목)} {커밋 메시지}
```

- 플랫폼에 따라 없는 내용은 생략 가능
- 💡 예시: `✨feat: PGS_소수_찾기 알고리즘 구현`

### 플랫폼

| 플랫폼                | 태그 |
| :-------------------- | :--- |
| 백준                  | BOJ  |
| 프로그래머스          | PGS  |
| 삼성SW Expert Academy | SEA  |
| 그외                  | ETC  |

### 이모지 및 태그

- 이모지는 선택에 따라 활용한다.

| 이모지 | 태그     | 설명                                  |
| :----- | :------- | :------------------------------------ |
| ✨     | feat     | 새로운 기능 추가                      |
| 🐛     | fix      | 버그 수정                             |
| ♻️     | refactor | 코드 리팩토링                         |
| ✏️     | comment  | 주석 추가(코드 변경 X) 혹은 오타 수정 |
| 📝     | docs     | README와 같은 문서 수정               |
| 🔀     | merge    | merge                                 |
| 🚚     | rename   | 파일, 폴더명 수정 혹은 이동           |

<br/>

## ⚠️ PR 규칙

```
[날짜] {플랫폼 or 언어} {문제 제목 or 문제 유형} - {기타 내용}
```

- 💡 예시: `[240701] PGS 소수 찾기 - 1문제`

<br/>

## ⚠️ (option)코드리뷰 규칙
- PR에서 각자 코드리뷰를 한다.
- 전체 코드 흐름을 파악한 뒤, 이해가 되지 않는다면 풀이에 대한 질문 달기
- 코드의 일부분에다 코드리뷰를 해도 되고 전체 코드 밑 or PR 하나 밑에다 코멘트 작성으로 리뷰를 해도 됩니다.
  <br/>

---

해당 README는 다음 레포지토리를 참고해서 제작하였습니다.

- [Algorithm-Study](https://github.com/CodeSquad-2023-BE-Study/Algorithm-Study)
- [algorithm](https://github.com/Ogu-Family/algorithm)

commit 컨벤션은 [gitmoji](https://gitmoji.dev/)와 [AngularJS Git Commit Message Conventions](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)을 참고했습니다.
