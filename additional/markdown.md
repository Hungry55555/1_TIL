# 안녕하세요
## 제목
### 제목
#### 제목
##### 제목
'#'은 글자 크기를 바꾸는 게 아닌 제목을 구분하기 위해 사용을 함

## 리스트
순서가 없는 리스트
* 리스트 1 (*, +, = 같은 bullet poit 로 나오게 된다.)
+ 리스트 1
- 리스트 1
    * 내부 리스트로 나옴
        * 또 내부 리스트

순서가 있는 리스트
1. 숫자. 띄우기 하면 순서가 있는 리스트가 나옵니다.
2. 두 번째 순서 있는 리스트가 나온다.
    1. 숫자는 4칸을 띄우니 내부 리스트로 나오게 됩니다.
        1. 또 내부 리스트

순서 있는 것과 없는 것 같이 사용하기
1. 순서가 있고
  * 내부에 순서가 없는 리스트

* 순서가 없고
    1. 내부에 순서가 있는 리스트


## Code Block
* 코드가 여러 줄 일 때 (백틱3개 + 언어 종류)
```python
@app.route('/lotto')
def make_lotto():
    numbers = range(1, 46)
    # sample 비복원 랜덤 추출 이미 뽑았던 것은 뽑지 않고 추출
    # random.sample(후보, 갯수)
    lotto = random.sample(numbers, 6)
    return sorted(lotto)
```

* 코드가 한 줄 일 때 (백틱 하나 앞뒤로)

로또를 뽑는 코드는 `lotto = random.sample(numbers, 6)`게 작성할 수 있다.

## 링크 & 이미지
* 링크는 [ 텍스트 ] (주소)
[구글 바로가기](https://google.com)

* 이미지는 ! [텍스트] (이미지의 위치)

    * 로컬 이미지 넣어보기
    ![피카츄](pikachu.gif)
        * 마크다운 파일을 옮길 때 로컬 이미지도 같이 옮겨야 한다.
    * 인터넷 이미지 넣어보기
    ![뮤츠](https://cloud.githubusercontent.com/assets/664177/10267523/f81296de-6a97-11e5-99d0-d2124bd6a9e3.png)

## 텍스트 관련 문법
* 글자 굵게 만들기
    * 앞뒤로 ** 를 붙여준다!
    * 이렇게 **굵게** 만들 수 있다.
* 글자 기울이기
    * 글자 앞뒤로 * 하나를 붙여준다!
    * 이렇게 *기울일* 수 있다.
* 글자 취소하기
    * 글자 앞뒤로 ~~ 을 붙여준다!
    * 이렇게 ~~취소선~~을 그을 수 있다.

## 구분선 
* -(하이픈, 대쉬, 빼기)를 3개 이상 작성하면 된다.
---

## 인용문 작성하기
> 이렇게 작성하면 인용문 형태로 만들 수 있습니다.
>>인용문 내부에도 인용문을 나타낼 수 있습니다.

## 테이블 작성
|이름|반|
| ---| ----------- |
| 김싸피 | :서울1반: |


# 개요
## CLI
Command Line Interface

명령줄 인터페이스

명령어를 통해 사용자와 컴퓨터가 상호작용하는 방식
GUI로 상호작용 하기 전에 이 방식으로 상호작용함

## GUI
Graphic User Interface

그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식

| GUI | CLI |
| ----------- | ----------- |
| 우리가 보통 보던 것 | 깃 배쉬 같은 명령어로 실행 되는 그런 것  |

## 그럼 GUI가 엄청 편한데 왜 CLI?
* GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 성능(리소스)을 상대적으로 더 많이 소모
* 수 많은 서버/ 개발 시스템이 CLI를 통한 조작 환경을 제공함

---

# 기초 문법 실습
Git bash를 실행 후 명령어 하나씩 실행해보기
CLI에서 .(점)의 역할

* .현재 디렉토리를 의미

* ..현재의 상위 디렉토리(부모 폴더) 상위 폴더

    - 깃 배쉬 맨 위~/codes 

    - 저기서 그럼 codes 가 현재 위치임

    - ~이 상위폴더 인데 ~는 Home Directory고 윈도우에서 홈 디렉토리는 C:W/Users 씨드라이브의 사용자 폴더 유저 이름 까지 여기가 홈디렉토리임

    - ~은 c드라이브 사용자 로그온 아이디이다.

## 기초문법(1/2)
* touch
    * 파일 생성
* mkdir
    * 새 디렉토리 생성 (메이크 디렉토리로 기억 폴더 만들기)
* ls
    * 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 보여줌
    * ls -a는 숨겨진 파일 까지 전부 보여주기!
---
## 기초문법(2/2)
* cd
    * 현재 작업 중인 디렉토리를 변경 (위치 이동 체인지 디렉토리, GUI로 치면 폴더 더블 클릭)
* start
    * 폴더/파일을 열기 (Mac에서는 open을 사용)
        * vs code로 열고 싶다면 앞에 code를 붙여서 작성 code server.py 이렇게
* rm
    * 파일 삭제(-r 옵션을 사용해 디렉토리 삭제)

---

# CLI에서 가장 중요한 것
내가 어디있는지 **(경로)** 알아야 한다.
* 절대 경로
    * Root디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것 ~ 홈 디렉토리 /? 얘가 뭐라고????
        * 윈도우 바탕화면 절대 경로(모든 경로를 다 명확하게 명시한 것) 예시 C:\Users\SSAFY\Desktop

* 상대 경로
    * **현재 작업하고 있는 디렉토리를 기준**으로 계산된 상대적 위치를 작성한 것(기준점을 가지고 있음)
        * 만약 현재 작업하고 있는 디렉토리가 C:\Users일 때 윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop
        * 상대경로에서 .을 많이 씀
        현재 위치를 기준으로... 라는 말이고
        * ..은 부모폴더
        * 절대경로를 쓰면 너무 길어져서 상대경로를 쓰는 경우가 많음



---
# Git
짱 중요하다고 함

버전 관리 시스템==> git (분산 **버전 관리 시스템**)

버전 관리란?

변화를 기록하고 추적하는 것
ex) goole Docs버전관리 예시
버전 관리는 이전 버전으로 부터의 변경사항을 기록하고 있다.
날짜랑 시간 기록하기
파일명에
그래도?

만약 파일 중 중간 일의 파일내용을 지우고 싶다면 어떤 내용을 지워야 할지 모름 틀림 그림 찾기 해야함

헉 파일 한개당 500메가 면 어쩌지 허어어억
???

뭔소리지
이해가 안되는데 
어떤게 병견되었는지

변경사항 한개를 하나의 커밋이라고 부름

변경사항을 작성하는 것을 깃에서는 '커밋'이라고 부름

변경사항???
원본 파일을 매번 만들어서 저장함
개선되는 부분은 변경사항만 저장을 함

변경 사항과 언제 수정되는지?
이 두 가지를 관리하는 것을 버전 관리! 라고 보면됨

그럼 분산은??

* 중앙 집중식: 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드

ex) 각직원이 파일을 가져와 일하고 파일을 다시 중앙서버에 업로드 해야함!

보안이 좀 중요한 회사의 방식임

하지만...서버에 불이나버리면 어쩔테지? 그래서 백업서버를 잘 준비해놔야함


* 분산식: 버전 정보를 모든 곳에서 관리할 수 있ㄴ는것
버전을 여러개의 복제된 젖ㅇ소에 저장 및 관리

한개가 사용이 불가능해도 다른 곳에 있는 정보로 금방 복구 가능!
그냥  쑥 전달해주면 그대로 복구가 됨!
깃? 분산식 버전관리 시스템

---
# 분산구조에서의 장점
* 중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행할 수있음
    * 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상
* 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
* 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
    * 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버와 동기화


## git의 역할
* 코드의 버전(히스토리)를 관리
* 개발되어 온 과정 파악
* 이전 버전과의 변경 사항 비교

코드의 '변경 이력'을 기록하고 협업을 원활하게 하는 도구

git=시스템
github이나 gitlab은 git이라는 시스템을 이용해서 서비스를 제고하는 업체!
허브에 작성한 내용 랩에 올릴수도 잇음!
같은 깃을 쓰기 때문!
모든 프로젝트는 깃 랩에 올려야 함

명세서?
그게뭐람

명세서가 뭔데요
알려줘

결과물은 깃헙에 올리지마시게나
막 올리고 싶어서 못견디겠다?
퍼블릭말고 프라이베이트에 작성을 하거라~

퍼블릭으로 할수 있는것?
내가 수업시간에 직접 정리한 내용!
나의 2차 창작물...ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

싸피 깃 랩은 기본이 프라이빗
싸피 깃 랩의 서버는 삼전이라 외부 노출이 안될듯!
삼스디에스에 있다능

### git의 3가지 영역
- working directory 현재 작업
- staging area 선별장
- repository 저장소

현재 작업하는 파일을 저장하는데 진짜 필요한 파일만 저장할 수 있도록 선별하는 staging area 총 3개 영역

working directory 실제 작업 중인 파일들이 위치하고 있는 영역

staging area working directory에서 병경된 파일(or 생성된 파일) 중, 다음 버전(버전관리)에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역(선별 공간) 자동 판단이 아니라 작성한 사람이 직접 선별해 줘야만행....

Repository 버전 이력과 파일들이 영구적으로 저장되는 영역
(모든 버전과 변경 이력)==> commit이 기록됨
버전 commit


commit은 버전

변경된 파일들을 저장하는 행위이며 마치 사진을 찍듯이 기록한다 하여 'snapshot' 이라고도 함

버전관리 ㅇ변경이력 언제? 누가?

### git init
로컬 저장소 설정(초기화)
- git의 버전 관리를 시작할 디렉토리에서 진행

내가 버젼 관리 하고자 하는 곳에 깃으로 git init을 해야지 그때부터 깃으로 관리할 수 가 있음
이건 초기화인데 최초 1회만 해주면 된다!
어떻게 보면 영역 선포!

현재 깃으로 관리되고 있는지 보고 싶으면 (master)라고 써있는지 보면 된다능

### git add
변경 사항이 있는 파일을 staging area 에 추가
내가 **생성/수정** 파일의 버전을 관리하기 위해 선별공간(staging area)으로 파일을 보내는 명령어

### git commit
선별하는 공간에서 저장 준비가 끝나서 저장소로 보내서 저장 관리를 하는 것

깃 배쉬에는 vim이라는게 있음 이게 CLI에서 수정할수있게함 빔 에디터라고함
나가기! 나가는 방법이 뭔지 알아보자

vim에는 2가지 모드가 있는ㄴ데 edit과 커매느가 있는ㄷ ㅔ커멘드 모드로 가야함 esc 연타
:q
를 치면됨
안된다?
esc누르고 :q!를 누르면 됨

edit 모드로 가기 위해서는 키보드 i를 눌러주면 됨
esc 눌러주면 다시 커맨드 모드로 돌아감
모드가 2개 있다!

저장은??
아까 q는 그냥 나가기
저장은 w 
저장후 나가기? wq

git status 현재 깃의 상태
WD, SA, RE

untracted files? 현재 파일 중 새로운게 존재한다 새 파일이 존재하고 있다 생성된 파일

색을 보면 알 수 있음 
* 빨: 워킹 디렉토리
    * 옮기려면?-- git add 파일명
    * 스테이징 디렉토리로 옮겨짐
    워닝?이 뜬 다면? LF 라인 피드? 무시해 무시해

* 초: 스테이징 디렉토리
    * 여기 있어야지만 commit찍을 수 있음
    이 파일은 버젼 관리 위해 보낸 것 이므로 바로 커밋 찍어도 된다능
    관리하고자 하는 파일
    git commit-m '변경사항 msg' ???뭔말이야
    중요한 msg 주요 변경사항에 대한 정보를 요 커밋 메세지로 남겨 줘 !
    습관화 해야 팀업으로 협업시 팀원들이 편함
    요 메세지는 대충적지 말고 주요 변경사항에 대한 정보를 작성함

    커밋 누가 찍는지 입력해 줘야함
    잔디?
    개발용 gmail???

    git config --global user.email "이메일" 전역 설정
커밋을 찍기 위해서 는 반드시 스테이징 에어리어에 있는 친구만 레포지토리로 요렇게 이동이 가능함
!
그 이동이 커밋!
작업 공간
working directory
에서 스테이징 에어리어로 추가해줘서 add

1. working dirctory (untracked-처음 관리가 되는 파일, modified-이미 관리가 되고 있는 파일)
(git add sample.txt)(파일명.경로 git 영역 내부에 있는 폴더 경로)

2. staging area (New file, modified)
git commit -m 'commit 메시지'

3. repository(Nothing to commit, working tree clean)


git은 로컬 저장소 내 모든 파일의 '변경사항'을 감시하고 있다.
(git 영역 선포한 폴더 내부 모든 변경 감시)

git commit 실습
git add .
현재 파일에 있는거 전부 스테이징 에리어로 보내셈
다시 워킹으로 빼는건? git rm --cached 파일 명 스테이지에서 내리겠다. unstage

로컬local
현재 사용자가 직접 접속하고 있는 기기 또는 시스템 개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경

git config --global -l
깃 글로벌 설정 정보 보기
로그를 한줄로 보고싶다?!
git log --oneline

git init 주의사항
* git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것
* 즉, 이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것
* git 저장소 안에 git 저장소가 있을 경우 가장 바깥쪽의 git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문

서브모듈
서브모듈은 보통 프로젝트의 단위가 클때 너무 많은걸 할때 조각조각 나뉘어서 관리할때 사용하는 방식임
힉힉

여러개 모여서 큰 프로젝트가 되거나
혹은 특별한 보안상의 이슈로 특정 사람들만 봐야한다 이런경우 특정 사람만 초대해서 보게 함!

그래서 지금 같은 찌끄레기 상태에서는 사용하지 않음
master존재하면 git init하지말거라...

혹시 한다면...선생님을 부르렴...

스테이징 에이리어에 올렸으면 커밋 찍고 수정하고 그냥 저상태로 수정해서 끌어내리지 마라 한번에 하다보면 이상하게 꼬일 수 있음
---
# 20240112
gitignore를 하면 블랙리스트라 아무리 add해도 안 올라감
자리 이동때마다 git config --global user.email "메일주소"
git config --global user.name "유저네임"

git log를 했는데 갑자기 명령어가 입력이 안된다?!!?!?키보드 q를 누르면 나갈수있다

부모 깃이 아니라 내가 방금 생성한 깃을 삭제해줘야함
저러면 일단 깃 애드부터 잘 안됨
(어제꺼 복습)

어제까지 한 건 로컬 레포지토리
내가 저장한 저장정보를 원격저장소에 보내는걸 할것
깃헙이 원격저장소 깃랩 이런거

## 원격저장소

코드와 버전 관리 이력을 온라인 상의특정 위치에 저장하여 여러개발자가 협업하고 코드를 공유할 수 있는 저장공간 

깃헙 같은 것
퍼블릭이 기본이라 보통 누구ㅏㄴ 볼수있음
분산임!
누구나 같이 개발할수있는 환경!

옥토캣..문어였음...
고양이 문어

add 하고 commit하면 전부 local repository에 저장이 되어버림!

이걸 원격 저장소에 올릴려면?

1. 원격 저장소의 주소가 필요
    * 이때 필요한 명령어가 git remote: 원격저장소 관련 명령어
    git remote add origin<=별칭(원격저장소의 별칭) remote_repo_url 별치을 다르게 해서 url2, url3이렇게 등록할수 있음 별칭1 별칭2

오리진에 올릴수도 있고 별칭1에 등록된 레포에도 올릴수있음
등록하는건 올리는 사람 마음
1. 리모트 레포 생성
2. 로컬에 리모트 레포 등록
    * git remote add 별칭 remote repo url
3. 로컬에서 푸쉬한다.
    * git push 별칭 브랜치명
    * 로컬에서 리모트로 올릴때는 push
    * 리모트에서 로컬로 가지고 올때는 pull
    
.git이라고 붙어도 안붙어도 동작함 주소만 있으면 ok!

저장소 목록 확인
* git remote -v

git push -u origin master
* -u: upstream 원격 저장소에 commit 목록을 업로드
깃푸쉬만 해도 자동 업로드 가능하게 미리 등록 같은 느낌
흑흑

깃아 푸쉬해줘 오리진이라는 이름의 원격저장소에 마스터라는 이름의 브랜치를!

리모트와 로컬은 자동 동기화가 아니니까 해줘야하는데 동기화 기준은 remote가 된다!

항상 push 하기 전에 작업하기 전에는 remote와 버전을 동기화 하는 것이 좋음
gitpull을 해서 리모트의 최신과 맞추고 다시 작업하고 push~

- 아직 협업은 상정 안하고 혼자 작업 기준

리모트 보다 로컬이 오래된거라면 반드시 리모트 내용을 pull 받아서 최신화 해 주어야함

원격저장소에는 commit이 올라가는 것 
커밋 이력이 없다면 push 할 수 없음
add commit한적 없어도 할 수 없음

**버젼이 올라가느 것이므로 무조건 commit이 존재해야함!**


### pull clone의 차이

* git pull origin master
원격저장소의 변경 사항만을 받아옴 (업데이트)
    리모트 레포와 로컬 레포가 한 번이라도 존재해야 pull이 성립이 됨 업데이트만 받아올수있음
    local이 없는데 레포를 받아오면 뭘 업데이트 할 지 모르므로 무조건 local 레포가 존재했을때 pull이 가능함(local이 존재한다는건 내부에 .git이라는 폴더가 존재함을 의미)
* git clone remote_repo_url
    원격 저장소의 전체를 복제 (다운로드)
    로컬 환경에 리모트의 내용을 복제해서 가져와야할때!
    (clone으로 받은 프로젝트는 이미 git init되어 있음)
    clone 최초한번 local없을때 한번! 해주고 이후에는 pull 해주면 됨!존재하니까!
    clone은 없을때~ .git 폴더 같이 복제됨


* 차이 pull 로컬 git 영역 있을때
        clone 로컬 git 영역 없을때
git bash에서 붙여넣기 shift+insert

기준이 리모트
리모트와 기준을 맞추고 버젼 만들고 push해서 올려야함 만약 아니다? 그럼 이제 충돌나니까 꼭 할때 수동으로 항상 리모트와 버젼을 수동으로 일치 시켜줘야함

아침에오면 pull하는 습관 같은...
작업전에 git pull 후에 작업 add commit push


### gitignore

git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일
==>버전관리안하는 파일이나 폴더

프로젝트에 따라 공유하지않아야하는 것들도 존재하기 때문

gitignore는 파일이름이 .gitignore라는 파일로 파일명 앞에 .gitigrnore라고 붙고 확장자는 없음


이건 프로젝트 시작에서 제일 먼저 해줘야함
.으로 시작하는 폴더는 숨김의 의미

정말 중요하거나 정말 필요없는 파일을 주로 .gitignore에 저장 보안상 중요도가 높은 경우

버젼 관리중에 .gitignore에 등록이 된다면???

git ignore에 등록되어있지만 여전히 관리 대상이라는 의미

한번이라도 커밋이 찍힌 파일은 깃 이그노어에 등록되어도 제외되지 않음 그래서 초반 등록이 중요함

이미 관리되는건 등록해봤자 무쓸모~
만약 버전 관리중이라면 한 번 빼야함


git rm --cached a.txt 관리 대상에서 a.txt를 제외 시키는 명령어

git config --global core.autocrlf true
이걸 치면 없어짐

어떤 거를 제외할지 매번 고민할 필요 없음

gitignore를 한번에 설정할수있도록 지원이 있음

어떤 운영체제 프레임워크 프로그래밍 언어를 쓰는지 개발환경에 따라 gitignore목록을 만들어주는 사이트가 있음
https://www.toptal.com/developers/gitignore/

==
gitignore.io


## github은 어디에 활용?

개인 포트폴리오

* github활용하기 
    * TIL을 통해 내가 학습한 것을 기록(Today I Learned)==> 내가 성장한 과정을 기록
* 개인, 팀 프로젝트 코드를 공유
--- 
* TIL
매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것

단순히 배운것만을 필기하는 것이 아닌 스스로 더 나아가 어떤 학습을 했는지를 기록하는 것

블로그 적인 느낌으로 쓰는게 가장 좋음

신입개발자에게 요구되는 가장 중요한 덕목==>문서화

문서화의 중요성!
문서화 연습의 중요성
https://d2.naver.com/news/3435170
개발자의 수준 분류

글쓰기 연습을 위해 TIL을 써보도록....흑흑

TIL만들기??




README.md 파일이란?
* 프로젝트에 대한 설명, 사용방법, 문서화된 정보등을 포함하는 역할
* Markdown 형식으로 작성되며, 프로젝트의 사용자, 개발자, 혹은 기여자들에게 프로젝트에 대한 전반적인 이해와 활용 방법을 제공하는데 사용
* 주로 프로젝트의 소개, 설치 및 설정 방법, 사용 예시, 라이선스 정보, 기여방법 등을 포함
* 반드시 저장소 최상단에 위치해야 원격 저장소에서 올바르게 출력됨

    * 리드미와 .git폴더가 동일한 폴더에 있어야함
    그래야 한번에 보이니까! 항상 같은 곳에~~(.git폴더와 동일한 위치를 의미)


git remote rm 원격_저장소_이름 별칭
 현재 로컬 저장소에 등록된 원격 저장소 주소 삭제
