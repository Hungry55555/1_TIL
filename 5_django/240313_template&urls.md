장고 템플릿 시스템
데이터 표현을 제어하면서 표현과 관련된 ㅜㅂ분을 담당

html 콘텐츠를 변수 값에 따라 바꾸기

장고 ㅔㅁ플릿 랭기지

템플릿에서 조건,반복,변수 등의 프로그래밍적 기능을 제공하는 시스템
{{}}
중괄호가 두개!

1. Variable
렌더 함수의 세번째 인자로 딕셔너리 값이 존재해야함
키 값으로 접근을 해야함
컨텍스트에 들어가는 타입은 반드시 딕셔너리에 해당해야함
2. 필터
표시할 변수를 수정할 때 사용 (변수+|+필터)

3. 태그
화면에 표시 안되고 그냥 기능을 하는게 
시작과 종료 태그가 있는게 있음
없는태그들이 있는데  이렇게 조건 같은건 존재함

DTL에서의 주석
hello


기본 템플릿 구조의 한계
모든 템플릿에 부트스트랩을 쓰려면?
모든 템플릿에 부트스트랩 cdn을 써야하나?!
부모 템플릿 만들어주고 얘를 상속한다면?!
부모에 cdn 코드가 들어있다면 굳이 cdn 작성안해도 이미 다 cdn 작성되어있도록 하는 것


템플릿 상속
1. 페이지의 공통요소를 포함
2. 하위 템플릿이 재정의 할 수 있는 공간 정의

html form 요청과 응답

데이터를 보내고 가져오기
안녕이라는 페이지 받아보기?
요청 받아서 응답?
어떤 태그 쓸것?
html의 form 태그 쓸것
실습에서 등장을...언제?

아이디 패스워드
로그인창이 폼태그

submit 이 로그인이 제출되면 폼이 요청을 보내는 아주 중요한 역할을 하는 태그

검색도 폼
사용자로부터 ㅏㄹ당된 데이터를 서버로 전송
체크박스도 사용자가 클릭한 데이터