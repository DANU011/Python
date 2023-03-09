# 딕셔너리
# 연습 문제
'''
다음 딕셔너리에 대해 물음에 답하라.

사용자가 월을 입력하면 해당 월에 일수를 출력하라
알파벳 순서로 모든 월을 출력하라
일수가 31인 월을 모두 출력하라
월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
'''
days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

'''mon = input("월을 입력하세요. : ")
print(days[mon.title()])

day_li = list(days.values())
print(sorted(day_li))

for x in days:
    print(x)
    
for x in days:
    if days[x]==31:
        print(x)

# 이름 일 키 벨류 바꾸기 > 일수 기준 정렬 > 다시 원래대로 키 벨류 교환해주기
days_it = days.items()
days_it = [ (day, month) for (month, day) in days_it ]
days_it.sort() # 일수가 같을 때 달도 정렬됨.
#print(days_it)
days_it = [ (month, day) for (day, month) in days_it ]
print(days_it)

mon = input("월을 세자리로 입력하세요. : ")

for x in days:
    if x[0:3]==mon.title(): #title()
        print(days[x])'''
        
'''다음 딕셔너리에 대해 물음에 답하라. d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

전화번호가 8로 끝나는 사용자 이름을 출력하라
이메일이 없는 사용자 이름을 출력하라
사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
'''
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

'''for i in d:
    if i['phone'][7]=='8':
        print('p:',i['name'])
        
for i in d:
    if i['email']=='':
        print('e:',i['name'])
#====================================        
n = input("name : ")

flag=1

for i in d:
    if i['name']==n.title():
        print(i['phone'],i['email'])
        flag=0
        
if flag==1:
    print('이름이 없습니다')'''

## Set
# update

my_list = [5, 6, 7]
my_set = {1, 2, 3}
my_set.update(my_list)   #{1, 2, 3, 5, 6, 7}
# 리스트를 셋에 업데이트

#set 예제
#1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램
'''import random

pick = set() # 빈 set 만들어주기
while len(pick)<6:
    pick.add(random.randint(1,45))
    
print('추천번호는 : ', sorted(pick)) #정렬'''

'''연습문제
학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
'''
'''grades = {"Alice": [85, 90, 95],"Bob": [75, 80, 85],"Charlie": [95, 95, 95]}

for name, grade_list in grades.items():
    print(name, sum(grade_list)/len(grade_list))'''
    
'''숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고,
남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
'''
'''num = [1, 2, 2, 3, 3, 3, 4, 4, 5]
num_s=set(num) # list > set
print(sum(num_s))'''

'''주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.'''
text = "Hello, world!"
#결과값 {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

f_text = {}

for char in text:
    if char not in f_text:
        f_text[char] = 1 
    else :
        f_text[char] = f_text[char]+1 #있으면 추가
        
print(f_text)

# 알파벳만 선택하도록 필터링

'''
두 개의 리스트가 주어졌을 때,
두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.
리스트A: 임의의 길이와 요소를 가진 리스트
리스트B: 임의의 길이와 요소를 가진 리스트
'''
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

# 공통된 요소인 2와 4를 모두 포함한 리스트를 반환한다.
# 결과값
# [2, 4]

list1_s = set(list1)
list2_s = set(list2)
print(list(list1_s.intersection(list2_s)))


#=============================================================================================
# 함수
'''def num_sum(n):
    tot = 0
    for i in range(1,n+1):
        tot += i
    return tot

print(num_sum(50))

def cir_area(r):
    pass 3.14*r**2

def cir_cirm(r):
    pass 3.14*r*2

print(round(cir_area(3.5),1)) #round ,1 첫째짜리까지 반올림
print(round(cirm_area(3.5),1))

def dan(n):
    cd = []
    for i in range(1,n+1):
        if n%i==0:
            cd.append(i)
    return cd

print(dan(32))'''

#함수 인자 전달 방
x = 'global' #전역 서로 다름

def my_function():
    global x #>전역변수화
    x = 'local' #지역 서로 다름

my_function()
print(x)

#람다 함수
# 기존 함수 정의 방법
def add(a, b):
    return a + b

# 람다 함수 정의 방법
lambda_add = lambda a, b: a + b

# 함수 호출
result1 = add(3, 4)             # 7
result2 = lambda_add(3, 4)      # 7

#연습문제
'''두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
1.예: 2, 4 > ****
           ****
2.하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
예: 123 > 1+2+3 = 6

3.두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환

4.문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성

5.재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램

'''
#1
'''def box(n,m):
    for pass'''
#2
#3
#4
#5


#함수 내 변수 참조 순서
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)








    



