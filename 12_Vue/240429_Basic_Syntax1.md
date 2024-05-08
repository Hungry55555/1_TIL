s# Template Syntax
## 개요
* Template Syntax: DOM을 기본 구성 요소 인스턴스의 데이터에 **선언적으로 바인딩(Vue Instance와 DOM을 연결)** 할 수 있는 HTML 기반 **템플릿 구문(확장된 문법 제공)** 을 사용
### Template Syntax 종류
1. Text Interpolation
```html
<p>Message: {{ msg }}</p>
```
* 데이터 바인딩의 가장 기본적인 형태
* 이중 중괄호 구문 (콧수염 구문)을 사용
* 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
* msg속성이 변경될 때마다 업데이트 됨

2. Raw HTML
```html
<div v-html="rawHtml"></div>
```
```js
const rawHtml = ref('<span style="color:red:>This should be red.</span>')
```
* 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

3. Attribute Bindings
```html
<div v-bind:id="dynamicId"></div>
```
```js
const dynamicId = ref('my-id')
```
```html
<div id="my-id"></div>
```
* 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
* HTML의 id 속성 값을 vue의 dynamicId속성과 동기화 되도록 함
* 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨
4. JavaScript Expressions
## Directive
# Dynamically data binding
## v-bind
## Attribue Bindings
## Class and Style Bindings
# Event Handling
## v-on
# Form Input Bindings
## v-model
## v-model 활용
