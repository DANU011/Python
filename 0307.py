#
''''''
#0307

# 여러 줄로 이루어진 문자열은 삼중 따옴표

##문자열 연산
# 문자열 합치기
s1 = "Hello"
s2 = "world"
s3 = s1 + s2
print(s3)  # 출력: HelloWorld

# 문자열 반복
s4 = "Ha"
s5 = s4 * 3
print(s5)  # 출력: HaHaHa

# 문자열 길이 구하기
s6 = "Python is awesome"
print(len(s6))  # 출력: 17

##문자열 인덱싱

# 문자열 인덱싱 예제 1
s = "Hello, World!"
print(s[0])   # 'H'
print(s[1])   # 'e'
print(s[-1])  # '!' java배열과 유사, 오른쪽부터 시작 -1

#사용자로부터 문자열을 입력 받고, 문자열에서 첫 번째와 마지막 문자를 출력하기

'''string = input("문자열을 입력하세요: ")

first = string[0]
last = string[-1]

print("첫 번째 문자는 %s입니다." % first)
print("마지막 문자는 %s입니다." % last)'''

#문자열에서 홀수 번째 문자 추출하기
string = "abcdefghij"

result = ""
for i in range(len(string)): # len(string) 10 /range(len(string)) 0~9
    if i % 2 == 0: #시작이 0임을 주의!
        result += string[i]

print(result)  # 출력값: "acegi"

##문자열 인덱싱
#문자열 hello world에서 world 부분 문자열을 추출
string = "hello world"
substring = string[6:] #6부터 1씩증가
print(substring)  # "world"

#문자열 hello world에서 hello 부분 문자열을 추출
string = "hello world"
substring = string[:5] #시작부터 4번까지
print(substring)  # "hello"

#문자열 hello world에서 hlowrd 부분 문자열을 추출
string = "hello world"
substring = string[::2] #처음부터 끝까지 2씩 증가
print(substring)  # "hlowrd"

#문자열을 뒤집는 예제
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"

##문자열 주의사항
# 문자열과 숫자를 함께 사용할 때
s = "Hello"
n = 3
#print(s + n)  # TypeError: can only concatenate str (not "int") to str

# 타입을 일치시킨 후 사용해야 함
print(s + str(n))  # "Hello3"

# 문자열 인덱스 범위를 벗어난 경우
s = "Hello"
#print(s[5])  # IndexError: string index out of range

# 인덱스가 올바른 범위 내에 있는지 확인해야 함
if len(s) > 5:
    print(s[5])  # ""
else:
    print("Index out of range")

# 문자열 슬라이스 범위를 벗어난 경우
s = "Hello"
print(s[1:10])  # "ello"

'''문자열을 수정할 때 주의
문자열은 불변(immutable)한 객체입니다.
따라서 한 번 생성된 문자열은 수정할 수 없습니다.
만약 문자열을 수정해야 한다면, 새로운 문자열을 생성해야 합니다.
'''
# 문자열 수정
s = "Hello"
#s[0] = "h"  # TypeError: 'str' object does not support item assignment

# 문자열은 불변(immutable)한 객체이므로, 새로운 문자열을 생성해야 함
s = "hello" + s[1:]
print(s)  # "hello"

##문자열 함수와 메서드
#문자열 함수
s = "Hello, world!"
print(len(s))  # 13

#문자열 메서드
s = "Hello, world!"
s_upper = s.upper()
print(s)  # "Hello, world!"
print(s_upper)  # "HELLO, WORLD!"

##문자열 구성 파악 함수 bool 값으로 나옴.
'''
isalnum(): 문자열이 알파벳과 숫자로만 이루어졌는지 여부를 반환합니다.
isalpha(): 문자열이 알파벳으로만 이루어졌는지 여부를 반환합니다.
isdecimal(): 문자열이 10진수 숫자로만 이루어졌는지 여부를 반환합니다.
isdigit(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isidentifier(): 문자열이 파이썬 식별자로 사용 가능한지 여부를 반환합니다.
islower(): 문자열이 소문자로만 이루어졌는지 여부를 반환합니다.
isnumeric(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isprintable(): 문자열이 출력 가능한지 여부를 반환합니다.
isspace(): 문자열이 공백 문자로만 이루어졌는지 여부를 반환합니다.
istitle(): 문자열이 제목 케이스로 이루어졌는지 여부를 반환합니다.
isupper(): 문자열이 대문자로만 이루어졌는지 여부를 반환합니다.
'''
# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True >메서드
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True

##문자열 대소문자 변환 함수
'''
upper(): 문자열의 모든 알파벳을 대문자로 변환한 새로운 문자열을 반환합니다.
lower(): 문자열의 모든 알파벳을 소문자로 변환한 새로운 문자열을 반환합니다.
capitalize(): 문자열의 첫 문자를 대문자로,
나머지 문자를 소문자로 변환한 새로운 문자열을 반환합니다.
title(): 문자열에서 단어의 첫 문자를 대문자로,
나머지 문자를 소문자로 변환한 새로운 문자열을 반환합니다.
swapcase(): 문자열에서 대문자는 소문자로,
소문자는 대문자로 변환한 새로운 문자열을 반환합니다.
'''
# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"

##문자열 찾기 함수
'''
find(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다.
찾지 못한 경우에는 -1을 반환합니다.
rfind(sub): 문자열에서 지정된 문자열(sub)을 '뒤에서부터' 찾아서 그 위치를 반환합니다.
찾지 못한 경우에는 -1을 반환합니다.
index(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다.
찾지 못한 경우에는 ValueError '예외'가 발생합니다.
rindex(sub): 문자열에서 지정된 문자열(sub)을 뒤에서부터 찾아서 그 위치를 반환합니다.
찾지 못한 경우에는 ValueError '예외'가 발생합니다.
count(sub): 문자열에서 지정된 문자열(sub)이 '몇 번' 등장하는지 카운트하여 반환합니다.
'''

# 문자열 찾기 함수 예시
s = "hello, world!"

print(s.find("o"))  # 4 처음 찾아진거 반환
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2
print(s.find("ello")) # 1
print(s.find("elo")) #-1 찾지못함.

##문자열 공백 삭제, 변경 함수
'''
strip([chars]): 문자열의 '양쪽' 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. chars 인자를 생략하면 공백을 제거합니다.
lstrip([chars]): 문자열의 '왼쪽' 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. chars 인자를 생략하면 공백을 제거합니다.
rstrip([chars]): 문자열의 '오른쪽' 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. chars 인자를 생략하면 공백을 제거합니다.
replace(old, new[, count]): 문자열에서 old를 new로 바꾼 새로운 문자열을 반환합니다.
count 인자를 사용하면 치환할 최대 횟수를 지정할 수 있습니다.
'''
# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!" 양쪽 공백삭제
print(s.lstrip())  # "hello,   world!  " 왼쪽 공백삭제
print(s.rstrip())  # "  hello,   world!" 오른쪽 공백 삭제
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "

##문자열 분리, 결합 함수
'''
split( )
문자열을 지정된 구분자(sep)로 나누어 '리스트'로 반환합니다.
sep 인자를 생략하면 공백을 구분자로 사용합니다.
maxsplit 인자를 사용하여 나눌 횟수를 지정할 수 있습니다.
'''
string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

#maxsplit 어떻게?
#문자열.split(sep='구분자', maxsplit=분할횟수)
string = "apple,banana,grape"
string_list = string.split(sep=",",maxsplit=1)  # 쉼표를 구분자로 사용
print('maxsplit :',string_list)  # ['apple', 'banana', 'grape']
'''
splitlines( )
문자열을 개행 문자 또는 캐리지 리턴 문자 등을 기준으로 분리하여 리스트로 반환합니다.
join( )
문자열을 반복 가능한 객체의 요소들을 구분자로 연결하여 반환합니다.
'''
# 문자열 분리, 결합 함수 예시
s = "apple,banana,grape"

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"] \n,\r로 쪼개짐
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

##문자열 정렬, 채우기 함수
'''
center(width[, fillchar]): 문자열을 지정된 너비(width) 가운데 정렬하여 새로운 문자열을 반환합니다.
fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다.
기본값은 공백입니다.
ljust(width[, fillchar]): 문자열을 지정된 너비(width)에 맞추어 왼쪽으로 정렬하여 새로운 문자열을 반환합니다.
fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다.
기본값은 공백입니다.
rjust(width[, fillchar]): 문자열을 지정된 너비(width)에 맞추어 오른쪽으로 정렬하여 새로운 문자열을 반환합니다.
fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다.
기본값은 공백입니다.
zfill(width): 문자열의 왼쪽에 0을 채워서 지정된 너비(width)에 맞추어 새로운 문자열을 반환합니다.
'''
# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   " 원래있던거+새로추가할거 합쳐서 10
print(s.center(11, "-"))  # "---hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"

##연습문제 - 사용자가 입력한 문자열에 대해 다음 물음에 답하라
#s = input("문자열을 입력하세요: ") #applebanana
#문자열의 문자수를 출력하라
print('문자수 : ',len(s))
#문자열을 10번 반복한 문자열을 출력하라
sten=s*10
print('열번반복 : ',sten)
#문자열의 첫 번째 문자를 출력하라
print('첫 번째 문자 : ',s[0])
#문자열에서 처음 3문자를 출력하라
print('처음3문자 : ',s[:3])
#===문자열에서 마지막 3문자를 출력하라
print('마지막3문자 : ',s[-3:]) #string[시작 인덱스:끝 인덱스:문자사이간격]
#문자열의 문자를 거꾸로 출력하라
rev_s=s[::-1]
print('거꾸로 : ',rev_s)
#===문자열에 17번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
if len(s)>17:
    print(s[16]) #index 0부터 시작
else:
    print('문자가 없습니다') #문자열 주의사항 인덱스 범위 참고 ppt 11p
#===문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
print(s[1:-1]) #index 범위를 사용해서 제거하면됨
print('첫번째마지막 제거 : ',)
#문자를 모두 대문자로 변경하여 출력하라
print('모두 대문자 : ',s.upper())
#문자를 모두 소문자로 변경하여 출력하라
print('모두 소문자 : ',s.lower())
#문자열에서 'a'를 'e'로 대체하여 출력하라
print('a를 e로 : ',s.replace('a','e'))

'''
문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는
'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
Your word: Buffalo
Buffa
lo
'''
#find로 찾아서 s.find('a')
#s = input("Your word: ")
sf = s.find('a') # a 처음나오는 위치 
if sf != -1:
    print(s[:sf+1])
    print(s[sf+1:])
else:
    print('a가 없습니다. : ',s) # a 존재 x

#a가 여러개 split?
print(s.replace('a','a\n'))

'''
숫자를 문자열로 변화하는 방법은 str(num)을 이용한다.
str(12) > '12'가 된다. 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다.
int('12') > 12가 된다. 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라.
예를 들어 234 > 2+3+4=9가 된다
[Hint]
sum = 0
for s in '234':
sum += int(s)
'''
# 반복문 1-1000을 문자로 반환해서 쪼개기 > 숫자로 반환해서 더하기

sum = 0 #f1
for num in range(1,1001): #1000까지 1001포함 x #f1
    dsum=0 #f2
    for d in str(num): #f2
        dsum += int(d) #f2
    sum+=dsum #f1
print(sum)

##Collection Data Types
'''
리스트 (list)
리스트는 파이썬에서 가장 많이 사용하는 자료구조입니다.
리스트는 대괄호 [ ] 내에 쉼표(,)로 구분된 요소들을 담을 수 있습니다.
리스트는 수정 가능하며, 순서도 유지됩니다.
'''
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']

'''
튜플 (tuple)
튜플은 리스트와 비슷하지만, 수정이 불가능한 자료구조입니다. (형변환을 이용하여 수정)
튜플은 소괄호 ( ) 내에 쉼표(,)로 구분된 요소들을 담을 수 있습니다.
'''
numbers = (1, 2, 3, 4, 5)
names = ('Alice', 'Bob', 'Charlie')
'''
딕셔너리(Dictionary)
딕셔너리는 키(key)와 값(value)의 쌍으로 구성된 자료형입니다.
딕셔너리는 순서가 없습니다.
딕셔너리는 {}를 사용하여 생성할 수 있습니다.
'''
'''>>> d = {'name': 'John', 'age': 30}
>>> type(d)
<class 'dict'>
>>> d = dict(name='John', age=30)
>>> type(d)
<class 'dict'>'''

'''
셋 (set)
셋은 순서가 없는 유일한 요소(element)들의 집합입니다.
셋은 중복된 값을 허용하지 않습니다.
셋은 {}을 사용하여 생성할 수 있습니다. 또는 set() 함수를 사용하여 생성할 수 있습니다.
'''
'''>>> s = {1, 2, 3}
>>> type(s)
<class 'set'>
>>> s = set([1, 2, 3])
>>> type(s)
<class 'set'>'''

#리스트
'''
리스트는 파이썬에서 가장 기본적이고 많이 사용되는 자료형 중 하나로,
여러 개의 값을 하나의 변수에 저장하고 관리할 수 있습니다. 
대괄호 [ ] 로 감싸져 있으며, 쉼표(,) 로 구분된 값들이 나열되어 있습니다.
리스트는 문자열과 유사하지만, 문자열과 달리 값의 변경이 가능합니다. 
리스트 안에는 어떤 자료형도 포함시킬 수 있습니다.
'''
# 정수와 실수가 포함된 리스트
mixed_list = [1, 2.5, 3, 4.2, 5]

# 문자열과 불리언 값이 포함된 리스트
string_bool_list = ['hello', True, 'world', False]

# 리스트와 튜플이 포함된 리스트
list_tuple_list = [[1, 2, 3], (4, 5, 6), [7, 8, 9]]

# 리스트와 딕셔너리가 포함된 리스트
list_dict_list = [[1, 2, 3], {'a': 4, 'b': 5, 'c': 6}, [7, 8, 9]]

# 리스트와 집합이 포함된 리스트
list_set_list = [[1, 2, 3], {4, 5, 6}, [7, 8, 9]]

#리스트 컴프리헨션(List Comprehension)
'''
파이썬에서 리스트를 간단하게 생성하는 방법 중 하나입니다.
기본적인 문법 구조
[표현식 for 항목 in 반복가능객체 if 조건문] * 반복가능객체 : 리스트 튜플 ...등

표현식은 각 항목에 대한 연산을 의미하고, 항목은 반복 가능한 객체에서 가져온 값이 들어갑니다.
if 조건문은 생략이 가능하며, 조건문이 참인 경우에만 값을 추가합니다.
'''
## [표현식 for 항목 in 반복가능객체 if 조건문]
#1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

#리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

#리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]

#문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 바꾸기
words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) >= 5]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']
#re = [word.lower() for word2 in words if len(word2) >= 7]
#print(re)

#====리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist] #이중 for문처럼 생각
print(new_list)  # [1, 2, 3, 4, 5, 6]

#====주어진 이차원 리스트에서 짝수만 리스트로 생성하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]

##리스트 인덱싱
'''
리스트 안에 있는 특정 요소에 접근하는 방법입니다. 리스트 인덱싱은 대괄호 []를 사용하며,
리스트에서 접근하려는 요소의 인덱스를 대괄호 안에 넣어서 사용합니다.
인덱스는 0부터 시작하며, 리스트의 길이보다 1 작은 값을 가집니다.
만약 음수 값을 사용하면 리스트의 끝에서부터 역순으로 접근할 수 있습니다.
'''
# 리스트 인덱싱 기본 문법
#my_list[index]

# 리스트 인덱싱 예시
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # "apple" 출력
print(fruits[1])  # "banana" 출력
print(fruits[-1])  # "cherry" 출력

'''리스트 내부에 리스트가 있는 경우 다중 리스트 인덱싱을 사용하여 리스트의 리스트 내부에
있는 요소에도 접근할 수 있습니다.'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])  # [1, 2, 3] 출력
print(matrix[1])  # [4, 5, 6] 출력
print(matrix[2])  # [7, 8, 9] 출력
print(matrix[0][1])  # 2 출력
print(matrix[1][2])  # 6 출력

##리스트 슬라이싱
'''
리스트 슬라이싱은 리스트에서 원하는 부분만을 추출하는 방법입니다.
다음은 리스트 슬라이싱의 문법입니다.
리스트[start:end:step]
여기서 start는 추출을 시작할 위치, end는 추출을 끝낼 위치(해당 인덱스의 값은 포함하지 않음),
step은 추출할 요소의 간격입니다.
'''
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])   # [2, 3, 4]
print(my_list[:3])    # [1, 2, 3]
print(my_list[2:])    # [3, 4, 5]
print(my_list[::2])   # [1, 3, 5]

#음수 인덱스를 사용하여 리스트의 끝에서부터 추출할 수도 있습니다.
my_list = [1, 2, 3, 4, 5]
print(my_list[-3:])   # [3, 4, 5]
print(my_list[:-2])   # [1, 2, 3]

##리스트 합치기
#+ 연산자를 이용하는 방법
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

#extend() 메서드를 이용하는 방법
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list3 = list1
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

##리스트 요소 수정
#인덱싱을 이용하여 요소 수정하기
my_list = [1, 2, 3, 4]
my_list[2] = 5
print(my_list) # 출력 결과: [1, 2, 5, 4]

#슬라이싱을 이용하여 요소 수정하기
my_list = [1, 2, 3, 4]
my_list[1:3] = [5, 6]
print(my_list) # 출력 결과: [1, 5, 6, 4]

##리스트 요소 추가
#append() 메서드-리스트의 끝에 새로운 요소를 추가
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list) # 출력 결과: [1, 2, 3, 4, 5]

# insert() 메서드-원하는 위치에 새로운 요소를 추가
my_list = [1, 2, 3, 4]
my_list.insert(2, 5)
print(my_list) # 출력 결과: [1, 2, 5, 3, 4]

##리스트 요소 제거

# remove() 메서드
my_list = [1, 2, 3, 4]
my_list.remove(3)
print(my_list) # 출력 결과: [1, 2, 4]
#슬라이싱
my_list = [1, 2, 3, 4, 5]
my_list[1:4] = []
print(my_list) # 출력 결과: [1, 5]

#del 키워드-특정 인덱스에 있는 요소를 제거할
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list) # 출력 결과: [1, 2, 4]

# pop() 메서드
my_list = [1, 2, 3, 4]
my_list.pop()
print(my_list) # 출력 결과: [1, 2, 3]

my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(2)
print(my_list) # 출력 결과: [1, 2, 4, 5]
print(removed_item) # 출력 결과: 3

#clear() 메서드는 리스트의 모든 요소를 제거
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list) # 출력 결과: []

##내장 함수를 이용해서 리스트 다루기
#sum 함수를 이용한 합 구하기
nums = [1, 2, 3, 4, 5]
#total = sum(nums)
#print(total)  # 15

#max 함수와 min 함수를 이용한 최대값과 최소값 구하기
nums = [1, 2, 3, 4, 5]
max_num = max(nums)
min_num = min(nums)
print(max_num)  # 5
print(min_num)  # 1

#sorted 함수를 이용한 정렬하기=오름
nums = [3, 5, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4, 5]

#reversed 함수를 이용한 역순 정렬하기-내림
nums = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(nums))
print(reversed_nums)  # [5, 4, 3, 2, 1]

##sort()와 sorted()
#sort(): 리스트를 정렬합니다. 원본 리스트가 변경됩니다. 메서드
a = [3, 2, 1]
a.sort()
print(a)  # 출력: [1, 2, 3]

'''sorted(): 리스트를 정렬합니다. 정렬된 새로운 리스트를 반환합니다.
원본 리스트는 변경되지 '않'습니다. 리스트 외에도 정렬 가능.'''
a = [3, 2, 1]
b = sorted(a)
print(a)  # 출력: [3, 2, 1]
print(b)  # 출력: [1, 2, 3]

##reverse()와 reversed()
#reverse(): 리스트를 역순으로 뒤집습니다. 원본 리스트가 변경됩니다.
a = [1, 2, 3]
a.reverse()
print(a)  # 출력: [3, 2, 1]

'''reversed(): 리스트를 역순으로 뒤집습니다. 뒤집힌 리스트를 반환합니다.
원본 리스트는 변경되지 않습니다.
이터레이터(iterator)를 반환 > 리스트로 반환되지 않음.
'''
a = [1, 2, 3]
b = reversed(a)
print(a)  # 출력: [1, 2, 3]
print(list(b))  # 출력: [3, 2, 1] > 형변환 필요

#reverse()와 reversed()
'''
reverse()는 리스트 자체를 뒤집는 메소드입니다. 따라서 reverse()를 호출한 리스트 자체가
변경되며, 반환값은 None입니다. > 리스트용 메서드
reversed()는 이터러블 객체를 역순으로 순회할 수 있는 이터레이터(iterator)를 반환하는
> 리스트로 반환되지 않음.
함수입니다. 따라서 reversed()를 호출한 리스트 자체는 변경되지 않습니다.

따라서, 리스트를 뒤집어서 '새로운 리스트를 생성'하고 싶다면 reversed()를 사용하고,
리스트를 '자체적으로' 뒤집고자 한다면 reverse()를 사용하면 됩니다.
'''

##이터러블 객체
'''이터러블(iterable) 객체란 반복 가능한(iterable) 객체를 의미합니다.
즉, 여러 개의 요소를 가지고 있는 컬렉션(collection) 객체 중에서 하나로,
요소를 한 번에 하나씩 차례로 처리할 수 있습니다.

이터러블 객체는 반복문을 사용하여 요소를 하나씩 처리할 수 있으며,
대표적으로 리스트, 튜플, 딕셔너리, 문자열 등이 이에 해당합니다.
'''
my_list = [1, 2, 3, 4, 5]   # 리스트
my_tuple = (1, 2, 3, 4, 5)  # 튜플
my_dict = {'a': 1, 'b': 2, 'c': 3}  # 딕셔너리
my_string = 'Hello, World!'  # 문자열

##이터러블 객체와 이터레이터
'''이터러블 객체는 이터레이터를 생성할 수 있는 객체이고,
이터레이터는 실제로 값을 반환하는 객체입니다.
이터러블 객체에서 iter() 함수를 호출하면 이터레이터 객체가 반환되며,
이터레이터에서 __next__() 메서드를 호출하면 값이 하나씩 반환됩니다.
이터러블 객체: iter() 함수로 이터레이터를 생성할 수 있는 객체 
이터레이터: __next__() 메서드로 값을 차례대로 반환하는 객체
'''
# 이터러블 객체를 만들고
my_list = [1, 2, 3, 4, 5]

# 이터러블 객체로 이터레이터 생성
my_iter = iter(my_list)

# 이터레이터를 사용하여 값을 출력
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

##연습문제
'''3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
insert()로 맨 앞에 새로운 친구 추가
insert()로 3번째 위치에 새로운 친구 추가
append()로 마지막에 친구 추가'''
name=['a','b','c']

name.insert(0,'n1')
print(name)
name.insert(2,'n3') #0부터 시작
print(name)
name.append('l')
print(name)

'''리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
두 번째 요소를 17로 수정
리스트에 4, 5, 6을 추가
첫 번째 요소 제거
리스트를 요소 순서대로 배열하기
인덱스 3에 25넣기'''
li = [1, 2, 3]
li[1]=17
print(li)
li +=[4,5,6]
print(li)
del li[0]
print(li)
li.sort()
print(li)
li.insert(3,25) #수정 아니고 추가
print(li)

'''for 루프를 이용하여 다음과 같은 리스트를 생성하라.
0~49까지의 수로 구성되는 리스트
1~50까지 수의 제곱으로 구성되는 리스트'''
li=[num for num in range(1,50)]
print(li)
lis=[num2**2 for num2 in range(1,51)] #제곱근 **n
print(lis)

li = []
for i in range(1,50):
    li.append(i)
print(li)

lis = []
for i in range(1,51):
    lis.append(i**2)
print(lis)


'''크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는
새로운 리스트를 생성하라. 예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성'''
L=[1,2,3]
M=[4,5,6]
N = [L[i]+M[i] for i in range(len(L))]
print(N)
#zip 함수를 사용하기 [x+y for x,y in zip(list1, list2)]

N2 = []
for i in range(len(L)):
    N2.append(L[i]+M[i])
print(N2)

'''사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라.
예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.'''
#li = input("5개의 숫자를 띄어서 입력하세요 : ").split()
re = '+'.join(li)
print(re)

##튜플
#튜플 생성
# 빈 튜플 생성
t1 = ()
print(t1)  # ()

# 요소가 하나인 튜플은 요소 뒤에 콤마(,)를 붙여서 생성
t2 = (1,)
print(t2)  # (1,)

# 여러 요소를 가진 튜플 생성
t3 = (1, 2, 3)
print(t3)  # (1, 2, 3)

# 리스트나 문자열을 튜플로 변환
t4 = tuple([1, 2, 3])
print(t4)  # (1, 2, 3)

t5 = tuple("hello")
print(t5)  # ('h', 'e', 'l', 'l', 'o')


# 소괄호 없이도 생성 가능
t = 1, 2, 3
print(t)  # (1, 2, 3)

##튜플 인덱싱, 슬라이싱
# 튜플 생성
my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

# 인덱싱
print(my_tuple[0])   # 'apple' 출력
print(my_tuple[-1])  # 'mango' 출력

# 슬라이싱
print(my_tuple[2:5])   # ('cherry', 'orange', 'kiwi') 출력
print(my_tuple[:4])    # ('apple', 'banana', 'cherry', 'orange') 출력
print(my_tuple[2:])    # ('cherry', 'orange', 'kiwi', 'melon', 'mango') 출력
print(my_tuple[::2])   # ('apple', 'cherry', 'kiwi', 'mango') 출력
print(my_tuple[::-1])  # ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple') 출력

#튜플 연산
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 튜플 이어붙이기
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# 튜플 반복하기
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

##튜플의 메소드
#count(value): 튜플에서 해당 값이 등장하는 횟수를 반환합니다.
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # 3

#index(value): 튜플에서 해당 값이 처음으로 등장하는 인덱스를 반환합니다.
t = (1, 2, 3, 2, 4, 2)
print(t.index(2))  # 1


##튜플 언패킹
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

#튜플 언패킹을 이용하면 두 변수의 값을 쉽게 교환할 수 있습니다.
x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1

##튜플과 리스트 상호 변환
# 튜플을 리스트로 변환
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

# 리스트를 튜플로 변환
my_list = [6, 7, 8, 9, 10]
my_tuple = tuple(my_list)
print(my_tuple)

#튜플과 리스트 간 형변환 시 주의점
'''리스트 안에 요소가 변경 가능한 객체인 경우,
튜플로 변환하더라도 요소 값이 변경될 수 있다는 점입니다.
예를 들어, 다음과 같은 리스트를 튜플로 변환하면 튜플의 요소 값이 변경될 수 있습니다.
'''
my_list = [1, 2, [3, 4]]
my_tuple = tuple(my_list)
print(my_tuple) # 출력 결과: (1, 2, [3, 4]) > 내부의 리스트는 수정 가능함

my_tuple[2][0] = 5 # > 내부 리스트 수정
print(my_tuple) # 출력 결과: (1, 2, [5, 4])

#튜플을 이용한 함수에서의 활용 예시
'''
튜플을 이용한 함수에서는 여러 값을 동시에 반환할 수 있으며,
함수의 매개변수로서 튜플을 사용하여 함수에 여러 인수를 전달할 수 있습니다.
'''
def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide # > 튜플

result = calculate(10, 2)  #  결과: (12, 8, 20, 5.0)
print(result)
'''
이러한 방식으로 함수에서 여러 값을 동시에 반환하고,
반환된 튜플 값을 변수에 할당하여 활용할 수 있습니다.
'''










































