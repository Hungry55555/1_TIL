# 이벤트
## 개요
### 일상속의 이벤트
* 컴퓨터 기보드를 눌러 텍스트를 입력하는 것
* 전화벨이 울려 전화가 왔음을 알리는 것
* 손을 흔들어 인사하는 것
* 전화기의 버튼을 눌러서 통화를 시작하는 것
* 리모컨을 사용하여 채널을 변경하는 것

### 웹에서의 이벤트
* 화면을 스크롤하는 것
* 버튼을 클릭했을 때 팝업 창이 출력되는 것
* 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
* 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
-> 웹에서의 모든 동작은 **이벤트 발생과 함께 한다.**

## event 객체
* event: 무언가 일어났다는 신호, 사건
=> 모든 DOM 요소는 이러한 event를 만들어 냄

### 'event' object
* DOM에서 이벤트가 발생했을 때 생성되는 객체
* 이벤트 종류
    - mouse, input, keyboard, touch ...
    - https://developer.mozilla.org/en-US/docs/Web/API/Event
    ==> DOM 요소는 event를 받고 받은 event를 '처리' **event handler(이벤트 처리기) 할 수 있음
## event handler
* event handler: 이벤트가 발생했을 때 실행되는 함수
=> 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것
* .addEventListener(): 대표적인 이벤트 핸들러 중 하나
=> 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
```js
EventTarget.addEventListener(type,handler)
```
EventTarget : DOM 요소
type : 수신할 이벤트
handler : 콜백 함수

"**대상(EventTarget)** 에 **특정 Event(type)** 가 발생하면, **지정한 이벤트를 받아 할 일(handler)** 을 등록한다."

### addEventListenr의 인자
* type
    - 수신할 이벤트 이름
    - 문자열로 작성 (ex. 'click')
* handler
    - 발생한 이벤트 객체를 수신하는 콜백 함수
    - 콜백 함수는 발생한 event object를 유일한 매개변수로 받음

### addEventListener 활용
* "버튼을 클릭하면 버튼 요소 출력하기"
=> 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼 정보를 출력

* 요소에 addEventListener를 부착하게 되면 내부의 this 값은 대상 요소를 가리키게 됨 (event 객체의 currentTarget 속성 값과 동일)
## 버블링

# event handler 활용
## 이벤트 기본 동작 취소