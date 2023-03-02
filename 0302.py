#
''' '''

# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
num = int(input("숫자를 입력하세요: "))
#input 기본적을 문자 숫자로 바꿔 줘야함.

if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")


#=========================================
num = int(input("숫자를 입력하세요: "))

if num > 0:
    print("양수입니다")
elif num < 0:
    print("음수입니다")
else:
    print("0입니다")
    
    
#========================================
    # 사용자로부터 성적을 입력받아, 학점 부여하기
score = int(input("성적을 입력하세요: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")


#========================================
num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)


#========================================
score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)


#========================================
string = input("문자열을 입력하세요: ")
length = len(string) if string else 0 #비어있으면 거짓
print("문자열의 길이는", length, "입니다.")
#len 문자열의 갯수 count


#========================================
k = int(input("국어 성적을 입력하세요: "))
e = int(input("영어 성적을 입력하세요: "))
m = int(input("수학 성적을 입력하세요: "))

avg = kscore*0.4+escore*0.4+mscore*0.2
print(score)

grade="A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
#========================================
num1 = float(input("첫 번째 수를 입력하세요: "))
num2 = float(input("두 번째 수를 입력하세요: "))

if num1 > num2:
    print("큰 수는", num1, "입니다.")
else:
    if num1 == num2:
        print("두 수는 같습니다.")
    else:
        print("큰 수는", num2, "입니다.")


#========================================
score = 75

if score >= 90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    if score >= 85:
        grade = "B+"
    else:
        grade = "B"
elif score >= 70:
    if score >= 75:
        grade = "C+"
    else:
        grade = "C"
elif score >= 60:
    if score >= 65:
        grade = "D+"
    else:
        grade = "D"
else:
    grade = "F"

print("등급:", grade)


#========================================
'''사용자로부터 cm 단위의 길이를 입력 받는다.
입력 값이 음수이면 "잘못 입력하였습니다"라는
메시지를 출력하고 양수이면 길이를 인치로 변환하여
출력하는 프로그램을 작성하라. 1인치 = 2.54cm'''
cm = int(input("cm을 입력하세요. : "))
inch = cm*2.54
if cm > 0 :
    print(inch)
elif cm < 0 :
    print("잘못 입력하였습니다")


#========================================
'''사용자로부터 이수한 학점을 입력 받는다.
학점이 40학점 미만이면 "1학년입니다"를 출력하고,
40이상 80미만이면 "2학년입니다"를 출력한다.
학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.
'''
scount= int(input("이수 학점을 입력하세요 : "))

if scount < 40 :
    print ("1학년입니다.")
elif 40 <= scount & scount < 80 :
    print ("2학년입니다.")
else :
    print("졸업반입니다")


#========================================
'''사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력
받는다. 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
'''
time = int(input("시간 : "))
apm = int(input("am (1) or pm (2) ? :"))

overhour = int(input("시간 : "))
new_time =time+(overtime%24)

if new_time > 12 :
    if apm ==1 :
        apm="pm"
    else :
        apm="am"
    print("New hour: %d %s"%(new_time % 12, apm))
else :
    if apm == 1 :
        apm = "am"
    else :
        apm = "pm"
    print("New hour: %d %s"%(new_time, apm))


#========================================
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
    
# for ========================================
fruits = ["apple", "banana", "cherry"]

for fruit in fruits: # fruit 변수
    print(fruit)


#========================================
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)


#========================================
colors = ("red", "green", "blue")

for color in colors:
    print(color)

#========================================
text = "Python"

for char in text:
    print(char)

#========================================
for i in range(1, 11): # range(시작값, 끝에서 앞의 값)
    print(i)

#========================================
for i in range(0, 11, 2): # range(시작값, 끝에서 앞의 값,증감값)
    print(i)

#========================================
for i in range(10, 0, -1):
    print(i)

#========================================
# 0에서 4까지의 정수 시퀀스 생성
for i in range(5):
    print(i)

# 2에서 8까지 2씩 증가하는 정수 시퀀스 생성
for i in range(2, 9, 2): #range(start, stop, step) stop-1까지 나옴
    print(i)

# 10에서 1까지 1씩 감소하는 정수 시퀀스 생성
for i in range(10, 0, -1):
    print(i)

#========================================
#구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

#========================================
#별문자로 모양 그리기
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="") #print 안에 숨겨져있음 end="\n"-줄바꿈
    print()#기본값이 println인셈.print("*")=print("*", end="\n")

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()

#========================================
'''3의 배수와 5의 배수의 합 구하기
사용자로부터 양의 정수 n을 입력받아, 1부터 n까지의 자연수 중에서
3의 배수와 5의 배수의 합을 구하고, 이를 출력하는 프로그램을
작성하세요.
사용자로부터 입력받는 정수 n은 1 이상의 양의 정수입니다.
자연수 1부터 n까지의 숫자 중에서 3의 배수 또는 5의 배수인 숫자들의
합을 구합니다. 결과값은 정수형으로 출력합니다.
'''
num=int(input("양의정수를 입력하세요 :"))
sum=0;
for i in range(1,num+1) :
    if i % 3 ==0 or i % 5 == 0 :
        sum += i
print(sum)

#========================================
'''
사용자로부터 5개의 정수형 숫자를 입력받아,
입력받은 숫자들 중에서 최댓값과 최솟값을 찾고,
이를 출력하는 프로그램을 작성하세요.
입력받은 숫자는 1 이상 100 이하의 자연수입니다.
입력받은 숫자 중 중복된 숫자가 있을 수 있습니다.
'''
# n1=int(input("양의정수를 입력하세요 :"))
# n2=int(input("양의정수를 입력하세요 :"))
# n3=int(input("양의정수를 입력하세요 :"))
# n4=int(input("양의정수를 입력하세요 :"))
# n5=int(input("양의정수를 입력하세요 :"))
# 
# min=0
# max=0
# for min range(0,4,1)


max_num=0
min_num=100

for i in range(5):
    num = int(input("num :"))
    
    if num > max_num:
        max_num=num
        
    if num < min_num:
        min_num=num
        
print("max_num : ", max_num)
print("min_num : ", min_num)

#========================================
'''사용자로부터 정수형 숫자를 입력받아,
입력받은 숫자들의 합이 100보다 작을 때까지 숫자를 계속 입력받고,
입력받은 숫자들의 합을 출력하는 프로그램을 작성하세요.
입력받은 숫자는 1 이상 100 이하의 자연수입니다.
'''
sum = 0
i=1
while sum<100 :
    i = int(input("num :"))
    sum += i
print(sum)

#========================================
'''피보나치 수열의 n번째 항을 출력하는 프로그램
피보나치 수열은 다음과 같이 정의됩니다:
첫 번째 항과 두 번째 항은 각각 1입니다.
세 번째 항부터는 바로 앞 두 항의 합입니다.
즉, 1, 1, 2, 3, 5, 8, 13, ... 과 같은 수열입니다.
'''

n=int(input("몇 번째 항을 출력할까요? (1 이상의 양의 정수) :"))

if n==1 or n==2 :
    ans=1
else :
    a=1
    b=1
    i=3
    while i <= n:
        ans= a+b 
        a=b
        b=ans
        i+=1
print(ans)
    #n번째 n-1번째 + n-2번째
    
#break, continue, pass========================================
#1부터 10까지의 숫자 중에서 3의 배수인 수를 찾아 출력하는 프로그램
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
    else:
        continue
    print("이 부분은 실행되지 않습니다.")
    # continue문으로 이동했기 때문에 실행되지 않음
print("반복문이 종료되었습니다.")

#========================================
#사용자로부터 0 이 입력될 때까지 입력받은 양수를 출력하는 예제

while True:
    x = int(input("숫자를 입력하세요: "))
    if x == 0:
        break
    elif x < 0:
        print("잘못된 입력입니다.")
        pass
    else:
        print("입력한 숫자는 {}입니다.".format(x))

#========================================
#0부터 9까지의 숫자를 출력하되,5일 때는 아무 일도 하지 않고 넘어가도록 pass를 사용한 예제
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)

#========================================
#입력한 문자열에서 모음(a, e, i, o, u)을 제거하는 프로그램
        #pass 사용예제
vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")

output_str = ""
for char in input_str:
    if char in vowels:
        pass
    else:
        output_str += char

print("Modified string:", output_str)

#========================================
'''
숫자 맞추기 게임 
1~100 사이의 임의의 수가 선택되고 사용자가 숫자를 입력하면
입력한 숫자와 비교하여 "Up", "Down" 또는 "Correct!"를 출력합니다. 맞출 때까지 계속 입력할 수 있습니다.
'''
import random

# 1부터 100 사이의 임의의 수를 선택합니다
secret_number = random.randint(1, 100)

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로 반복문을 종료합니다

#========================================
#리스트 fruits에서 무작위로 선택된 하나의 과일을 출력
import random

fruits = ['apple', 'banana', 'orange', 'pear']
print(random.choice(fruits))

#무작위의 도시와 날씨를 출력하는 예제
import random

# 도시와 날씨 리스트 정의
cities = ['서울', '부산', '인천', '대구', '광주', '대전']
weathers = ['맑음', '흐림', '비', '눈', '우박']

# 도시와 날씨를 무작위로 선택하여 출력
city = random.choice(cities)
weather = random.choice(weathers)
print(f'{city}의 날씨는 {weather}입니다.')

#========================================
'''두 주사위를 던졌을 때, 합이 7이 되면 이김,
그렇지 않으면 지는 간단한 주사위 게임을 만들어보세요.
반복문 사용 이길 때 까지 주사위 게임 계속.
(힌트: random 모듈의 randint() 함수를 사용하세요.)
'''
import random
while True :
#randint(1,6)
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    print (n1,n2)
# n1+n2=7 break, 아니면 계속
    sum = n1+n2
    if sum==7 :
        print("O")
        break
    else :
        print("다시 던집니다.")
#========================================
'''
다음과 같은 게임 프로그램을 작성하라.
플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서
앞면(1) 또는 뒷면(2)이 나온다. 맞추면 $9을 따고 틀리면 $10을
잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
동전을 던져서 나오는 수는 다음 문장을 이용하라.
from random import randint
coin = randint(1,2) #1 또는 2를 임의로 발생
'''
import random
#from random import randint > c=randint(1,2) 로 표기 가능

while True:
    m=50
    c=random.randint(1,2)
    bat=int(input("앞1 뒤2를 고르세요. : "))
    if c==bat:
        m += 9
        print(m)
    else:
        m -= 10
        print(m)
    if m==100 or m <0 :
        print(p, "end")
        break
        
#========================================
'''
두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
예를 들어 (16, 24)의 최대 공약수는 8이다.
두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는
프로그램을 작성하라.
>큰 수를 작은 수로 나눈 나머지를 구하라
>큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
>작은 수가 0이 될 때까지 이 과정을 반목하라.
마지막 큰 수가 최대 공약수이다.
'''
r=int(input("정수입력1 :"))
s=int(input("정수입력2 :"))
if r > s :
    max_n=r
    min_n=s
else :
    max_n=s
    min_n=r

rs=1
while rs != 0 :
    rs = max_n % min_n
    max_n = min_n
    min_n = rs
print("최대공약수 : ", max_n)

#========================================






