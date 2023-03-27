# try-except 문
#ValueError 처리 예시
'''try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")'''

#FileNotFoundError 처리 예시
'''try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist. Please check the file path.")'''

#여러 예외 처리
'''여러 예외를 한 개의 except 블록에서 동시에 처리하려면, 예외 클래스들을 괄호로 묶고
쉼표로 구분하여 지정''' 
'''
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")'''
'''
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
'''

#에러 메시지 표시
'''
try:
    # 예외가 발생할 수 있는 코드를 실행합니다.
except ExceptionType as error(변수):
    # 예외가 발생했을 때 실행할 코드를 작성합니다.
    print(f"An error occurred: {error}")
'''
'''
try:
    result = 5 / 0
except ZeroDivisionError as error:
    print(f"An error occurred: {error}")
'''

#as 키워드
'''
as 키워드는 주로 두 가지 상황에서 사용
모듈 임포트:
as 키워드는 모듈을 임포트할 때, 해당 모듈의 이름을 다른 이름으로 사용하고자 할 때 사용.
예외 처리:
as 키워드는 try-except 문에서 발생한 예외 객체를 특정 변수에 할당할 때 사용.
이렇게 함으로써 발생한 예외 객체를 참조하고,
예외에 대한 추가 정보를 확인하거나 출력할 수 있다.
'''

#except Exception as e
'''
Exception
파이썬에서 모든 예외 클래스의 기본 클래스.
이 클래스를 사용하면 어떤 종류의 예외든 처리할 수 있다.
'''
'''
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")
'''

#try-except-else 문
'''
try:
    # 예외가 발생할 수 있는 코드
except [예외 타입]:
    # 예외가 발생했을 때 실행할 코드
else:
    # 예외가 발생하지 않았을 때 실행할 코드

else 절: 
else 절은 try 블록에서 예외가 발생하지 않았을 때 실행되는 영역.
try 블록이 성공적으로 실행되면 else 절이 실행되고,
예외가 발생하면 해당하는 except 블록이 실행.
예외 처리 외에 추가적인 작업이 필요한 경우 else 절을 사용할 수 있다.
'''

'''
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
    file.close()
'''

#try-except-finally 문
'''
finally 절:
 주로 프로그램이 예외 상황에서도 반드시 수행해야 하는 작업을 처리하는 데 사용.
 이 작업은 자원 정리, 파일 닫기, 데이터베이스 연결 종료, 네트워크 연결 종료 등이 있다.
 finally 절은 예외 발생 여부와 상관없이 실행되므로,
 자원의 누수를 방지할 수 있다.

'''
'''
try:
    # 예외가 발생할 수 있는 코드
except ExceptionType1:
    # 예외 타입 1이 발생한 경우 실행할 코드
except ExceptionType2:
    # 예외 타입 2가 발생한 경우 실행할 코드
# ... 필요한 만큼의 except 블록을 추가
finally:
    # 예외 발생 여부와 상관없이 항상 실행할 코드
'''
'''
try:
    file = open("example.txt", "r") #한글, 인코딩 필요
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
'''

'''
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 이
주어질 때 try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.
사용자로부터 문자열을 입력 받는다.
문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다.
문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.

위 문제를 try-except를 이용하지 않고 프로그램할 수 있는가? 차이점은 무엇인가?
'''

data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
'''
while True:
    try:
        user_input=input("enter a day of a week")
        value = date[user_input]
        print(value)
    except KeyError:
        print("empty")
        break
'''
'''
while True:
    try:
        user_input=input("enter a day of a week")
        value = data.get(user_input, None)
        if value is not None:
            print(value)
        else:
            print("empty")
        break
'''

#파일 열기
'''
open() 함수를 사용하여 파일 객체를 만든다.
파일을 열 때는 파일 이름과 모드를 지정해야 한다.
r: 읽기 모드. 파일을 읽기 위해서 사용. 파일이 존재하지 않으면 오류가 발생.
w: 쓰기 모드. 파일을 쓰기 위해서 사용. 파일이 이미 존재하면 덮어쓰고,
존재하지 않으면 새로운 파일을 생성.
a: 추가 모드. 파일의 끝에 내용을 추가하기 위해서 사용.
파일이 이미 존재하면 파일 끝에 내용을 추가하고, 존재하지 않으면 새로운 파일을 생성.
x: 배타적 생성 모드. 새로운 파일을 생성하기 위해서 사용. 파일이 이미 존재하면 오류가 발생.
b: 이진 모드. 파일을 바이너리 모드로 연다.
t: 텍스트 모드. 파일을 텍스트 모드로 연다. 이것이 기본값.
+: 읽기와 쓰기 모두를 지원하는 모드. r+, w+, a+와 같은 형태로 사용.
'''
'''
#파일 읽기
file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)

#읽은 위치 처음으로
file.seek(0)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print(line)

#읽은 위치 처음으로
file.seek(0)

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
lines = file.readlines()
print(lines)

#file.close()  # 파일을 닫습니다.
'''
'''
#파일 쓰기
file = open("example2.txt", "w")

# 파일에 문자열을 씁니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")

# 파일에 문자열의 리스트를 씁니다.
lines = ["We will use it to demonstrate file writing in Python.\n",
         "We can write multiple lines at once.\n"]
file.writelines(lines)

file.close()  # 파일을 닫습니다.

#파일 닫기
file = open("example.txt", "r")
content = file.read()
file.close()
'''
'''
Python에서 파일을 열고 사용한 후에는 반드시 파일을 닫아한다.
파일을 닫지 않으면 파일이 계속해서 열린 상태로 남아 있어서,
다른 프로그램이나 사용자가 해당 파일을 사용하지 못하게 된다.
'''

#with 문
'''
with 문은 파일을 열고 작업을 마치면 파일을 자동으로 닫아줍니다.
with open("example.txt", "r") as file:
    # 파일을 다루는 코드
'''
'''
with open("example.txt", "r") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print(content)
'''
'''
# 읽기 모드로 파일을 엽니다.
file = open("example.txt", "r")
content = file.read()
print("읽기 모드 예시:")
print(content)
file.close()

# 쓰기 모드로 파일을 엽니다.
file = open("example.txt", "w")
file.write("This is an example.\n")
file.write("We are writing to a file.\n")
print("쓰기 모드 예시:")
print("파일이 생성되었습니다.")
file.close()

# 추가 모드로 파일을 엽니다.
file = open("example.txt", "a")
file.write("We are appending to a file.\n")
print("추가 모드 예시:")
print("파일이 열렸고 내용이 추가되었습니다.")
file.close()
'''
'''
# 배타적 생성 모드로 파일을 엽니다.
file = open("example3.txt", "x")
file.write("This is a new file.\n")
print("배타적 생성 모드 예시:")
print("새로운 파일이 생성되었습니다.")
file.close()

# 이진 모드로 파일을 엽니다.
file = open("example.bin", "wb")
file.write(b"This is binary data.")
print("이진 모드 예시:")
print("바이너리 파일이 생성되었습니다.")
file.close()

# 읽기와 쓰기를 지원하는 모드로 파일을 엽니다.
file = open("example.txt", "r+")
content = file.read()
print("읽기와 쓰기를 지원하는 모드 예시:")
print("파일 내용:")
print(content)
file.write("\nWe are writing to the file again.")
file.close()
'''
'''
with open("example.txt", "r") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print("read() 함수 예시:")
    print(content)

    # 파일에서 한 줄을 읽습니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    line = file.readline()
    print("\nreadline() 함수 예시:")
    print(line)

    # 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    lines = file.readlines()
    print("\nreadlines() 함수 예시:")
    print(lines)
'''

#정규표현식 기본 개념
'''
정규표현식이란?
정규표현식(Regular Expression)은 문자열을 처리하는 패턴을 정의하는데 사용되는 형식 언어.
정규표현식은 문자열의 검색(search)과 치환(replace) 작업에 사용.

정규표현식의 구성 요소
정규표현식은 메타 문자(meta character)와 리터럴(literal)로 이루어져 있다.
메타 문자는 특별한 의미를 가지며, 리터럴은 문자 그대로를 의미.

정규표현식의 메타 문자
. (마침표) : 임의의 문자 한 개를 의미.
^ (캐럿) : 문자열의 시작을 의미.
$ (달러) : 문자열의 끝을 의미.
(별표) : 0개 이상의 문자를 의미.
(더하기) : 1개 이상의 문자를 의미.
? (물음표) : 0개 또는 1개의 문자를 의미.

정규표현식의 리터럴
정규표현식의 리터럴은 문자 그대로를 의미.
예를 들어, "hello"는 정규표현식에서 "hello"라는 문자 그대로를 의미.
'''

'''
#re.match() 함수

#re.match() 함수는 문자열의 시작에서 패턴을 찾아서 반환
#예를 들어, re.match(r"abc", "abcdef")는 "abc"와 매칭

# match 함수 예시

import re

# 문자열의 시작부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")
'''

'''
#re.search() 함수
#re.search() 함수는 문자열 내에서 패턴을 검색하여 반환
#예를 들어, re.search(r"abc", "defabc")는 "abc"와 매칭.

# search 함수 예시

import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
#pattern = r"[pP]ython"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")
'''

#문자열 추출
'''
문자열 추출이란?
문자열 추출은 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하고 추출하는 과정.

re.findall() 함수
re.findall() 함수는 문자열 내에서 패턴과 매칭된 모든 부분을 리스트로 반환.
예를 들어, re.findall("a", "abcdaaa")는 ['a', 'a', 'a', 'a']와 같은 리스트를 반환.
'''
'''
import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']
'''

'''
#문자열 치환
#re.sub() 함수
#re.sub() 함수는 문자열 내에서 패턴과 매칭된 부분을 다른 문자열로 치환.
'''
'''
re.sub(pattern, repl, string, count=0, flags=0)
pattern: 정규표현식 패턴
repl: 치환할 문자열 또는 치환 함수
string: 대상 문자열
count: 치환할 최대 개수 (생략 가능)
flags: 정규표현식 옵션 (생략 가능
'''
'''
import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴을 다른 문자열로 대체하기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

result1 = re.sub(pattern, "10", string1)
result2 = re.sub(pattern, "0", string2)
result3 = re.sub(pattern, "***", string3)

print(result1)  # I have 10 apples and 10 oranges
print(result2)  # The temperature is -0.0 degrees Celsius
print(result3)  # The password is ***
'''

#그룹핑
#매칭된 패턴에서 특정 부분만 추출하고자 할 때
#매칭된 패턴에서 특정 부분을 치환하고자 할 때
'''
import re

phone_number = "031-1234-5678"
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678
print(result.group())
'''

#그룹핑 치환 예시
#날짜 표기법이 YYYY-MM-DD 형태로 되어 있을 때 이를 MM/DD/YYYY 형태로 바꾸고 싶다면
import re

date = "2022-03-18"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2/\3/\1", date)

print(result)  # "03/18/2022"

#이름 순서 바꾸기

import re

string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)" #\s : 공백 문자와 매칭
result = re.sub(pattern, r"\2 \1", string)
print(result)  # "Yuna Kim"

#정규표현식 패턴 옵션
'''
패턴 옵션
re.IGNORECASE 또는 re.I 옵션
re.IGNORECASE 옵션은 대소문자를 무시.
예를 들어, re.findall(r"a", "AbCdAaA", re.IGNORECASE)는 ['A', 'a', 'A', 'a', 'A']와 같은
리스트를 반환.
re.MULTILINE 또는 re.M 옵션 re.MULTILINE 옵션은 다중행 모드를 사용.
예를 들어, "abc\ndef\nghi"라는 문자열에서 r"^g"를 검색할 때, re.MULTILINE 옵션이 적용되면
"g"와 매칭.
'''

#re.MULTILINE
string = """Python is an interpreted language
It is dynamically typed
And it is easy to learn"""


import re

pattern = '^Python'
result = re.findall(pattern, string, re.MULTILINE)
print(result)  # ['Python', 'typed']

#이메일 주소 추출
import re

def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails


string = "John's email is tt83@naver.com. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']

'''
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

\b : 단어 경계
[A-Za-z0-9._%+-]+ : 이메일 주소의 로컬 파트(local part)로 사용될 수 있는 문자들
@ : 이메일 주소의 구분자
[A-Za-z0-9.-]+ : 이메일 주소의 도메인 파트(domain part)로 사용될 수 있는 문자들
\. : 도메인 파트와 TLD(top-level domain)를 구분하는 점(.)
[A-Z|a-z]{2,} : | > or TLD로 사용될 수 있는 대문자 또는 소문자 문자들, 최소 2자리 이상
'''

#\b
'''
\b는 단어(word) 경계를 나타내는 메타문자. 
단어 경계란 단어와 단어가 아닌 문자(character) 사이의 경계를 의미. 
예를 들어, 단어 book의 경계는 공백이나 문장부호 등의 문자가 있을 수 있다.
\b는 이러한 단어 경계를 나타내므로, 정규표현식에서 단어 검색을 할 때 매우 유용.
문자열 book이 단어가 아닌 일부 단어의 일부분으로 포함되어 있더라도 매칭되지 않는다.
'''
string = "I love books. My favorite book is 'The Great Gatsby'."

import re

pattern = r'\bbook\b'
result = re.findall(pattern, string)
print(result)  # ['book']

#정규표현식을 사용한 데이터 유효성 검증
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False

#전화번호 유효성 검증하는 예제
import re

def is_valid_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3,4}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_number1 = '010-1234-5678'
phone_number2 = '02-123-4567'
phone_number3 = '123-4567'

print(is_valid_phone_number(phone_number1))  # True
print(is_valid_phone_number(phone_number2))  # True
print(is_valid_phone_number(phone_number3))  # False

#로그 데이터에서 IP 주소를 추출하는 예시
import re

log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)








