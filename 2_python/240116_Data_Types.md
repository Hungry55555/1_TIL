# 지난시간 복습
* Data Type: 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성으로 대표적으로 5종류가 있음
* int(정수 자료형), float(실수 자료형), str(문자열) : 지난시간에 함
* 오늘 시퀀스 타입에 이어서 함
---
# Sequence Types
* 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
(str, list, tuple, range)

* Sequence Types 특징
    1. 순서 (Sequence) : 값들이 순서대로 저장 (정렬 X)
    2. 인덱싱 (Indexing) : 각 값에 고유한 인덱스 (번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음
    3. 슬라이싱 (Slicing) : 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
    4. 길이 (Length) : len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
    5. 반복 (Iteration) : 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
    

## list (리스트)
* 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형
    * 문자열과 다른 특성 : 변경이 가능하다.

* 리스트 표현
    * 0개 이상의 객체를 포함하며 데이터 목록을 저장
    * 대괄호([])로 표기
        * 어제 배운 str문자열[] 형태에서 대괄호는 리스트가 아니라 인덱스 나타내는 것
    * 데이터는 어떤 자료형도 저장할 수 있음
    * 일반적으로 배열은 array라고 부르지만, 파이썬은 이걸 리스트로 부름
```python
my_list_1 = []

my_list_2 = [1, 'a', 3, 'b', 5]

my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```
* 리스트의 시퀀스 특징
    * 인덱스가 어려우면 값 사이사이를 자른다고 생각하면 편하다!
    * [::세번째 값] 세번째 값 지정하면 step을 지정해주는 것으로, 세번째 값이 2라면 2칸 씩 자른 값을 출력하겠다는 의미, -1은 역순으로 범위 값을 뒤집은 결과가 나오게 된다.
```python
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5
```
* 중첩된 리스트 접근
    * 출력 값 예상해보기
 ```python
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(my_list)) # 5  
print(my_list[4][-1])  # !!!
print(my_list[-1][1][0])  # w
 ```
리스트의 경우 하나의 항목이 1이라는 길이 값을 가지기 때문에 5개 원소를 가지고 있다면, 내부 원소가 아무리 길거나 커도 길이는 5

* 리스트는 가변 (변경 가능)
```python
my_list = [1, 2, 3]
my_list[0] = 100

print(my_list)  # [100, 2, 3]
```

## tuple (튜플)
* 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형

* 튜플 표현
    * 0개 이상의 객체를 포함하며 데이터 목록을 저장
    * 소괄호(())로 표기
    * 데이터는 어떤 자료형도 저장할 수 있음
```python
my_tuple_1 = ()

my_tuple_2 = (1,)

my_tuple_3 = (1, 'a', 3, 'b', 5)
```
여기서 (1,) 뒤에 있는 컴마는???
    * 만약 이 ,가 없다면 (1)이 되는데 이것은 정수 1이 되어버린다. 만약 이게 "1이라는 요소 한 개를 가진 튜플이다"라고 하고싶다면 정수뒤에 ,를 찍어 줘야한다.

* 튜플의 시퀀스 특징
```python
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[0:5:2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5
```

* 튜플은 불변 (변경 불가)
```python
my_tuple = (1, 'a', 3, 'b', 5)

# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'
```
* 튜플은 어디에 쓰일까?
    * 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등 **개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용됨**
``` python
x, y = (10, 20)

print(x)  # 10
print(y)  # 20

# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
```

튜플과 리스트의 차이는? 변형이 불가하냐 가능하냐

## range
* 연속된 **정수 시퀀스**를 생성하는 **변경 불가능**한 자료형

* range 표현
    * range(n)
        * 0부터 n-1까지의 숫자를 가진 시퀀스를 생성 (슬라싱과 좀 비슷함)
    * range(n,m)
        * n부터 m-1까지의 숫자 시퀀스

    * 왜 n-1 일까? 컴퓨터는 시작이 0 이기 때문

```python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
```
* 보통 반복문과 함께 활용됨 앞에 list(range())형식으로 list를 붙여 형을 변환하여 데이터를 확인할 수 있음

```python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능

print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
# Non-sequence Types
## dict (딕셔너리)
* **key-value 쌍**으로 이루어진 **순서**와 **중복이 없는** **변경 가능한** 자료형

* 딕셔너리 표현
    * key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range ...)
        * 키값은 애초에 변경 불가능한 값만 들어가서 변경 불가
    * value는 모든 자료형 사용 가능
    * 중괄호({})로 표기
    * 순서가 없어서 요소마다 인덱스가 없어서 인덱스로 접근이 불가능함
```python
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}
```

* 딕셔너리 사용
    * 딕션 접근은 키를 통해서 값에 접근을 함, 키가 나오는게 아니라 이 키의 값(value)이 나옴
    * 딕셔너리 사용시 키는 중복이 되지 않기 때문에 중복을 만들어서 넣으면 뒤에 입력한 값으로 출력이 된다.
```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple'])  # 12
print(my_dict['list'])  # [1, 2, 3]

# 값 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3]}
```
## Set (세트, 집합 자료형)
* 순서와 중복이 없는 변경 가능한 자료형
    * non-sequence기 때문에 순서가 없음

* 세트 표현
    * 수학에서의 집합과 동일한 연산 처리 가능
    * 중괄호({})로 표기
    * 빈세트 만들 때 {}이렇게 못만들고 set()이렇게 만들어야함
        * 왜냐하면 dict가 {}이걸 이미 먹어버려서 빈 값의 set를 만들려면 set()로 사용해야한다.
```python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

* 세트 표현
    * 수학에서의 집합과 동일한 연산 처리 가능
    * 중괄호({})로 표기
```python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

* 세트의 집합 연산
```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```
|합집합| \| |
|---|---|
|차집합|-|
|교집합|&|

집합연산이 필요한 경우 사용됨 그거 아니면 간단하게 중복을 제거하고 싶을때 그거 아니면 별로...
순서가 없기 때문에 중복제거를 위해 사용하면 순서가 다 없어져 버림

# Other Types
## None
* 파이썬에서 '값이 없음'을 표현하는 자료형
* 값이자 타입
어떠한 변수가 있고 None이라는 값을 할당 할 수 있음
값이 없음을 표현하는 값
* None 표현
```python
variable = None

print(variable)  # None
```

## Boolean
* 참 (True)와 거짓 (False) 값을 가진 변수 자료형
* 불리언 표현
    * 비교 / 논리 연산의 평가 결과로 사용됨
    * 주로 조건 / 반복문과 함께 사용
```python
bool_1 = True
bool_2 = False

print(bool_1)  # True
print(bool_2)  # False
print(3 > 1)  # True
print('3' != 3)  # True
```
시퀀스와 넌 시퀀스의 공통점?
* 여러개의 값을 저장하는 친구들
이런애들을 묶어서 collection이라함

# Collection
* 여러 개의 항목 또는 요소를 담는 자료 구조 (str, list, tuple, set, dict)

* 컬렉션 정리

|컬렉션|변경 가능 여부|순서|  |
|:---:|:---:|:---:|:---:|
|str|X|O|시퀀스|
|list|O|O|시퀀스|
|tuple|X|O|시퀀스|
|set|O|X|비시퀀스|
|dict|O|X|비시퀀스|

* 불변과 가변의 차이

```python
# 불변

my_str = 'hello'
# TypeError: 'str' object does not support item assignment
my_str[0] = 'z'
```
```python
# 가변

my_list = [1, 2, 3]
my_list[0] = 100
# [100, 2, 3]
print(my_list)
```
파이썬 튜터를 사용하는 것을 제안!


# Type Conversion
## 암시적 형변환 (Implicit Type conversion)
* 파이썬이 자동으로 형변환을 하는 것

* 암시적 형변환 예시
    * Boolean과 Numeric Type에서만 가능
        * 인트와 플롯의 만남=> 플롯
        * 트루와 폴스 1과 0으로 대체되기 때문에 트루와 인트의 합을 계산가능 트루와 폴스의 합 계산 가능
```python
print(3 + 5.0)  # 8.0

print(True + 3)  # 4

print(True + False)  # 1
```

## 명시적 형변환 (Explicit Type conversion)
* 개발자가 직접 형변환을 하는 것으로 암시적 형변환이 아닌 경우를 모두 포함

* 명시적 형변환 예시
    * str -> integer : 형식에 맞는 숫자만 가능
    * integer -> str : 모두 가능
    * 문자열 끼리의 합은 결합이 됨
    * 3.5를 int로 하면 3으로 소숫점 버려버림!
```python
print(int('1'))  # 1

print(str(1) + '등')  # 1등

print(float('3.5'))  # 3.5

print(int(3.5))  # 3

# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))
```

* 컬렉션 간 형변환 정리

| |str|list|tuple|range|set|dict|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|str| |O|O|X|O|X|
|list|O| |O|X|O|X|
|tuple|O|O| |X|O|X|
|range|O|O|O| |O|X|
|set|O|O|O|X| |X|
|dict|O|O (key만)|O (key만)|X|O (key만)| |

# 연산자
## 산술 연산자

|기호|연산자|
|:---:|:---:|
| - |음수 부호|
| + |덧셈|
| - |뺄셈|
| * |곱셈|
| / |나눗셈|
| // |정수 나눗셈 (몫)|
| %  |나머지|
| ** |지수 (거듭제곱)|

## 복합 연산자
* 연산과 할당이 함께 이뤄짐

```python
|기호| | |
|:---:|:---:|:---:|
| += | a += b | a = a + b |
| -= | a -= b | a = a - b |
| *= | a *= b | a = a * b |
| /= | a /= b | a = a / b |
| //= | a //= b | a = a // b |
| %= | a %= b | a = a % b |
| **= | a **= b | a = a ** b |
```
* 복합 연산자 예시
```python
y = 10
y -= 4
print(y) # 6

z = 7
z *= 2
print(z) # 14

w = 15
w /= 4
print(w) # 3.75

q = 20
q //= 3
print(q) # 6
```
## 비교 연산자
| 기호 | 내용 |
|:---:|:---:|
| < | 미만 |
| <= | 이하 |
| > | 초과 |
| >= | 이상 |
| == | 같음 |
| != |같지 않음|
|is|같음|
|is not|같지 않음|

* is 비교 연산자
    * 메모리 내에서 같은 객체를 참조하는지 확인
    * ==는 동등성 (equality), is는 식별성 (identity)
    * is 와 ==의 차이 3==3.0 근데 3 is 3.0은 틀림
    ==은 값 자체를 비교하지만 is 는 주소를 비교함
    * is 연산자는 값이 아니라 그자체로 타입인 None, True, False와 같은 것과 비교할때 is를 사용함
    * 일반적 숫자 상황은 is아니고 ==쓰고 None 과 True 상황은 is를 써야함

* 비교 연산자 예시
```python
print(3 > 6)  # False
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False

# SyntaxWarning
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문
# is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용
print(2.0 is 2)  # False
```

# 논리 연산자
|기호|연산자|내용|
|:---:|:---:|:---:|
|and|논리곱 |두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가 |
|or|논리합 |두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가 |
|not|논리부정| 단일 피연산자를 부정|

* 비교 연산자 예시
```python
print(True and False) # False

print(True or False) # True

print(not True) # False

print(not 0) # True
```
* 비교 연산자와 함께 사용 가능
```python
num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False


name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True
```

## 단축평가
* 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
* 논리 연산자에서 반드시 알아야하는 구동원리 => 단축평가

* 단축평가 예시
```python
vowels = 'aeiou'

print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0
```
in은 포함이 되어있는지 안되어 있는지

* 단축평가 동작 (어디까지 평가가 되는가?)
    * and
        *

in 이 어디 목록에 들어있는지 없는지
not in 은 안 속해야함

단축평가는 진자 잘 틀리니 어떻게 작동하는지 잘 정리해둘것
