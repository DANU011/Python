# 주석, 변수
a=10 # 이것은 한 줄 주석입니다
b=20 # 변수명=값
c=a+b

'''
이것은
여러 줄
주석입니다.
'''

"""
이것은
다른
여러 줄
주석입니다.
"""


print("hello world!",a,b)

print()

# 변수 사용 예제

x = 10  # 변수 x에 정수 10을 저장
y = 20  # 변수 y에 정수 20을 저장
z = x + y  # 변수 z에 x와 y의 합을 저장
print(z)  # 변수 z의 값을 출력

print()

#예약어를 확인하는 방법

import keyword

print(keyword.kwlist)

print()

#정수형 데이터

# 양의 정수
x = 100
print(x)    # 출력: 100

# 음의 정수
y = -200
print(y)    # 출력: -200

# 0
z = 0
print(z)    # 출력: 0

print()

#진수

# 10진수
x = 42
print(x)    # 출력: 42

# 2진수
y = 0b101010
print(y)    # 출력: 42

# 8진수
z = 0o52
print(z)    # 출력: 42

# 16진수
w = 0x2a
print(w)    # 출력: 42

print()

#실수 변환
print(float(10))
print(float("3.14"))

print()

#복소수

# 복소수 생성
z1 = 2 + 3j
z2 = complex(4, -2)

# 복소수 연산
z3 = z1 + z2
z4 = z1 * z2
z5 = z1 / z2
z6 = z1 ** 2

# 결과 출력
print(z3)   # (6+1j)
print(z4)   # (14+8j)
print(z5)   # (-0.4+0.7j)
print(z6)   # (-5+12j)

print()

#복소수형 데이터를 다룰 때, 실수부와 허수부를 각각 얻는 방법
z = 3 + 4j
print(z.real)  # 출력: 3.0
print(z.imag)  # 출력: 4.0

print()

#문자열

string = "Hello, World!"
print(string[0]) # "H" 출력
print(string[7]) # "W" 출력

greeting = "Hello"
name = "John"
message = greeting + ", " + name + "!" #더하기 연산자로 붙일수 있음.
print(message) # "Hello, John!" 출력

#문자열 반복
word = "spam"
repeated = word * 3
print(repeated) # "spamspamspam" 출력

#문자열 전용함수
string = "Hello, World!"
position = string.find("World")
print(position) # 7 출력

print()

#Boolean
a = True
b = False

print(a and b)   # 출력: False
print(a or b)    # 출력: True
print(not a)     # 출력: False

a = 3
b = 5

print(a < b)    # 출력: True
print(a > b)    # 출력: False

print()

'''타입 에러 - 변수에 저장되는
데이터의 타입이 일치하지 않아 발생하는 오류'''
# num = 10
# text = "apple"
# print(num + text)

#타입 에러 해결 - num을 문자열로 변환
num = 10
text = "apple"
print(str(num) + text)

print()

#타입 변환
num = 10
float_num = float(num)
str_num = str(num)
bool_num = bool(num)

print(type(num))         # <class 'int'>
print(type(float_num))   # <class 'float'>
print(type(str_num))     # <class 'str'>
print(type(bool_num))    # <class 'bool'>

print()

#리스트, 튜플, 딕셔너리

#리스트(List)
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange" #1번 인덱스 변경
print(fruits)

print()

#튜플(Tuple) - 요소의 추가, 수정, 삭제 등이 불가능

fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[1])

print()

#딕셔너리(Dictionary)
''' 중괄호({})를 사용, key와 value로 이루어진 쌍(pair),
key와 value는 콜론(:)으로 구분, 각 쌍은 쉼표(,)로 구분,
인덱스 대신 key를 사용하여 value에 접근가능'''

fruits = {"apple": 3, "banana": 2, "cherry": 5}
print(fruits)
print(fruits["banana"]) #키값 출력
fruits["orange"] = 4 #추가
print(fruits)

print()

# 산술연산자 사용 예제
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print(c)  # 13 출력
print(d)  # 7 출력
print(e)  # 30 출력
print(f)  # 3.3333333333333335 출력
print(g)  # 1 출력

print()

#산술 연산자 우선순위

result = 2 + 3 * 4 - 6 / 2 ** 2
print(result)  # 출력 결과: 12.5

result = (2 + 3) * 4 - 6 / 2 ** 2
print(result)  # 출력 결과: 18.5

#비교연산자

# 비교연산자 사용 예제
a = 10
b = 20
c = 10
print(a == b)  # False 출력
print(a != b)  # True 출력
print(a <= c)  # True 출력
print(b > c)  # True 출력

print()

#할당연산자
'''덧셈 후 할당(+=), 뺄셈 후 할당(-=),
곱셈 후 할당(*=), 나눗셈 후 할당(/=), 나머지 후 할당(%=)'''

# 할당연산자 사용 예제
a = 10
b = 20
a += b  # a = a + b 와 동일
print(a)  # 30 출력
a -= b  # a = a - b 와 동일
print(a)  # 10 출력
a *= b  # a = a * b 와 동일
print(a)  # 200 출력
a /= b  # a = a / b 와 동일
print(a)  # 10.0 출력
a %= b  # a = a % b 와 동일
print(a)  # 10.0 출력

print()

#논리연산자

# 논리연산자 사용 예제
a = True
b = False
c = True
print(a and b)  # False 출력
print(a or b)  # True 출력
print(not a)  # False 출력
print(not b)  # True 출력
print(a and c)  # True 출력
print(b or c)  # True 출력

print()

#멤버쉽 연산자
'''멤버쉽 연산자는 주어진 데이터가
시퀀스형 자료 (문자열, 리스트, 튜플, 세트)에
포함되어 있는지 여부를 확인하는 연산자'''

# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력
print("k" not in b)  # True 출력

print()

#식별 연산자 - is와 is not

# 식별 연산자 사용 예제
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # False 출력/ 다른 메모리의 주소값을 가지고 있음.
print(a is not b)  # True 출력
print(a is c)  # True 출력/ c에 a할당
print(b is not c)  # True 출력

#산술식과 비교식
# 산술식 활용 예제
x = 10
y = 5
a = x + y  # 덧셈 연산자를 이용하여 x와 y의 합을 계산
b = x - y  # 뺄셈 연산자를 이용하여 x와 y의 차를 계산
c = x * y  # 곱셈 연산자를 이용하여 x와 y의 곱을 계산
d = x / y  # 나눗셈 연산자를 이용하여 x와 y의 나눗셈을 계산
e = x % y  # 나머지 연산자를 이용하여 x와 y의 나머지를 계산
f = x // y  # 몫 연산자를 이용하여 x와 y의 몫을 계산
g = x ** y  # 지수 연산자를 이용하여 x의 y승을 계산

print(a, b, c, d, e, f, g)  # 15, 5, 50, 2.0, 0, 2, 100000 출력

# 비교식 활용 예제
x = 10
y = 5
a = x == y  # 등호를 이용하여 x와 y가 같은지 여부를 비교
b = x != y  # 불등호를 이용하여 x와 y가 다른지 여부를 비교
c = x > y  # 부등호를 이용하여 x가 y보다 큰지 여부를 비교
d = x >= y  # 부등호와 등호를 이용하여 x가 y보다 크거나 같은지 여부를 비교
e = x < y  # 부등호를 이용하여 x가 y보다 작은지 여부를 비교
f = x <= y  # 부등호와 등호를 이용하여 x가 y보다 작거나 같은지 여부를 비교

print(a, b, c, d, e, f)  # False, True, True, True, False, False 출력

#산술식과 비교식을 이용한 활용법
# 산술식 및 비교식 응용 예제
x = 10
y = 5
a = x + y
b = x - y
c = x * y
d = x / y

if a > c and b < d:  # a가 c보다 크고, b가 d보다 작은 경우
    print("a > c and b < d")  # 출력 안 됨
elif a < c or b > d:  # a가 c보다 작거나, b가 d보다 큰 경우
    print("a < c or b > d")  # "a < c or b > d" 출력
else:
    print("neither")  # 출력 안 됨

print()
# print()
# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30

# 산술식 출력 예제
print(10 + 5)  # 15 출력
print(10 - 5)  # 5 출력
print(10 * 5)  # 50 출력
print(10 / 5)  # 2.0 출력
print(10 % 5)  # 0 출력
print(10 // 5)  # 2 출력
print(10 ** 5)  # 100000 출력

# 리스트 출력 예제
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)  # ['apple', 'banana', 'cherry', 'kiwi', 'mango'] 출력

# 리스트 값 출력 예제
print(fruits[0])  # 'apple' 출력
print(fruits[1])  # 'banana' 출력
print(fruits[2])  # 'cherry' 출력

# 딕셔너리 출력 예제
person = {"name": "John", "age": 25, "city": "New York"}
print(person)  # {'name': 'John', 'age': 25, 'city': 'New York'} 출력

# 딕셔너리 값 출력 예제
print(person["name"])  # 'John' 출력
print(person["age"])  # 25 출력
print(person["city"])  # 'New York' 출력

#문자열 포매팅

# % 연산자를 이용한 포매팅

# %s는 문자열, %d는 정수, %f는 실수
name = "John"
age = 30
height = 175.5154

print("My name is %s, I'm %d years old, and my height is %.1f."
      % (name, age, height)) #넣어줄 순서/ %.1f 소숫점 한자리까지
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 출력 형식 지정 예제
num = 10
pi = 3.14159265

print("num = %d" % num)  # 출력 결과: "num = 10"
print("pi = %f" % pi)  # 출력 결과: "pi = 3.141593"
print("pi = %.2f" % pi)  # 출력 결과: "pi = 3.14"
print("pi = %10.2f" % pi)  # 출력 결과: "pi =       3.14"/%10열칸이 잡힘

# 문자열
name = "John"
print("Hello, %s!" % name)

# 정수
num = 42
print("The answer is %d." % num)

# 실수
pi = 3.14159
print("Pi is approximately %.2f." % pi)

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is %s %s and I am %d years old." % (first_name, last_name, age))

# 진수 변환
decimal_num = 42
binary_num = bin(decimal_num)
print("The decimal number %d is equal to the binary number %s." % (decimal_num, binary_num))

'''
%d: 정수 출력
%f: 실수 출력
%F: 실수 출력 (대문자)
%g: 실수를 지수 형태로 출력
%G: 실수를 지수 형태로 출력 (대문자)
%s: 문자열 출력
%a: 출력할 값을 문자열로 표현 (리스트, 딕셔너리 등)
'''
print()

#format() 메소드를 이용한 문자열 포매팅

#문자열 안에 중괄호 {}를 사용하여 변수의 값을 출력
# format() 메소드를 이용한 포매팅

name = "John"
age = 30
height = 175.5

print("My name is {}, I'm {} years old, and my height is {:.1f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."
#.format > .찍어서 연결/{:.1f} > :을 넣어서 형식변경 가능

print()
# 인덱스를 이용한 포매팅 예제-중복되는 변수를 더 쉽게 출력
name = "John"
age = 30
height = 175.5

print("My name is {0}, I'm {1} years old, and my height is {2:.1f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 문자열
name = "John"
print("Hello, {}!".format(name))

# 정수
num = 42
print("The answer is {}.".format(num))

# 실수
pi = 3.14159
print("Pi is approximately {:.2f}.".format(pi))

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

# 인덱스를 이용한 대입
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {1} {0} and I am {2} years old.".format(last_name, first_name, age))

print()

# f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

print()

'''서식지정자 이용
정수: {변수:d}
실수: {변수:f}
지수: {변수:e}
전체 자릿수 지정: {변수:전체 자릿수}
소수점 이하 자릿수 지정: {변수:.소수점 이하 자릿수f}
양수일 때는 +로 표시: {변수:+}
자릿수 맞추기: {변수:자릿수}
0으로 채우기: {변수:0>자릿수}
왼쪽 정렬: {변수:<자릿수}
가운데 정렬: {변수:^자릿수}
'''
# f-string에서 다양한 서식 지정자를 이용하는 예제
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age:d} years old, and my height is {height:.2f} cm.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.50 cm."

pi = 3.14159265

print(f"The value of pi is approximately {pi:.2f}.")
# 출력 결과: "The value of pi is approximately 3.14."

x = 12345

print(f"The value of x is {x:10d}.")
# 출력 결과: "The value of x is      12345."

# f-string에서 다양한 서식 지정자를 이용하는 예제

y = 12.345

print(f"The value of y is {y:10.2f}.")
# 출력 결과: "The value of y is     12.35."

z = 3

print(f"The value of z is {z:+5d}.")
# 출력 결과: "The value of z is    +3."

w = 12345

print(f"The value of w is {w:0>10d}.")
#총 10칸을 차지하는데 0으로 채우겠다.
# 출력 결과: "The value of w is 0000012345."

text = "Hello, World!"

print(f"{text:^20}")
# 출력 결과: "   Hello, World!    "

print()

#연습문제

name="tom"
age=20
#f-string
print(f"My name is {name} and I am {age} years old.")
#format()
print("My name is {} and I am {} years old.".format(name,age))
#% 연산자
print("My name is %s and I am %s years old."%(name,age))

num1=3
num2=2
num3=1
print(f"I have {num1} apples, {num2} oranges, and {num3} banana.")

num=1.23123132
print(f"The result is {num:.2f}.")
print("The result is %.2f."%num)

a=20
b=10
c=30
print(f"{b}+{a}={c}")

print()

#input
'''
사용자로부터 키보드나 다른 입력 장치를 통해 데이터를 입력받는
파이썬 내장 함수. input() 함수는 인자를 받지 않으며,
입력된 값은 항상 문자열로 반환.사용자가 입력한 값을 정수나 실수 등의
다른 데이터 타입으로 사용하려면, 적절한 형 변환 필요.
'''

# input() 함수를 이용하여 사용자로부터 입력 받기
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# input() 함수를 이용하여 사용자로부터 입력받아 계산하기
# num1 = int(input("첫 번째 정수를 입력하세요: "))#정수형 형변환
# num2 = int(input("두 번째 정수를 입력하세요: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division:.2f}")

# input(), 포매팅, 산술식을 이용하여 계산하기
# num1 = int(input("첫 번째 숫자를 입력하세요: "))
# num2 = int(input("두 번째 숫자를 입력하세요: "))

result = f"""
입력한 숫자:
첫 번째 숫자: {num1}
두 번째 숫자: {num2}

산술 연산 결과:
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} * {num2} = {num1 * num2}
{num1} / {num2} = {num1 / num2:.2f}
""" #"""~"""하나의 문자열

print(result)

# input()과 산술식만을 이용하여 가장 큰 숫자 출력하기
# num1 = int(input("첫 번째 숫자를 입력하세요: "))
# num2 = int(input("두 번째 숫자를 입력하세요: "))
# num3 = int(input("세 번째 숫자를 입력하세요: "))

max_num = num1

if max_num < num2:
    max_num = num2

if max_num < num3:
    max_num = num3

print(f"입력한 숫자 중 가장 큰 수는 {max_num}입니다.")
print()

'''
"사과 쇼핑몰"에서 사과를 구매할 때,
총 가격을 계산하는 프로그램을 작성하세요.
사용자로부터 사과의 개수와 가격,
그리고 부가세율을 입력받아,
총 가격을 계산하는 프로그램을 작성하세요.
'''
# count=int(input("갯수를 입력하세요."))
# price=int(input("가격을 입력하세요."))
# vat=float(input("부가세율을 입력하세요."))
# 
# total=f"{(count*price)+count*price*vat}"
# 
# print(f"구매신 사과의 갯수는{count}개 이고, 개당 가격은{price}원 입니다. 부가세는 {vat}%입니다. 총 가격은 {total} 입니다.")

'''초를 입력하면 분과 초로 표시하는 프로그램.
예를 들어, 200초를 입력하면 3분 20초로 표현하라'''

# sec=int(input("초를 입력하세요."))
# 
# resultM= f"{sec//60}"
# resultS= f"{sec%60}"
# 
# print(f"{sec}초는 {resultM}분{resultS}초 입니다.")

'''분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램을
만들어라. (예 : 1550분은 1일 1시간 50분)
'''

# min=int(input("분을 입력하세요."))
# 
# day=min//(60*24)
# hour=(min//60)%24
# min2=min%60
# 
# print(f"{min}분은 {day}일 {hour}시간  {min2}분 입니다.")

'''
500만원을 연이율 5%로 복리 저금했을 때
5년 후의 원리금의 합계를 출력하는 프로그램
'''
total=int(5000000*(1+0.05)**5)
print(total)

'''
1부터 n까지의 합은 n(n+1)/2로 주어진다.
1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.
'''
n=100
total=n*(n+1)/2
print(total)

'''
판매자가 딸기와 포도를 판매하고 있다.
포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아
총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라.
'''
# grp=int(input("포도의 갯수를 입력하세요."))
# stb=int(input("딸기의 갯수를 입력하세요."))
# 
# total=f"{grp*75+stb*113.5}"
# 
# print(f"포도 {grp}개와 딸기 {stb}개의 총 무게는 {total}g입니다. ")





































