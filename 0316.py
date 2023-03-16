'''bin, oct, hex  int
bin(x), oct(x), hex(x)
10진 정수 x에 대한 2진수, 8진수, 16진수 문자열 반환
int(str, base=10)
문자열 str을 10진수로 변환'''

bin(12)   #'0b1100'
int('123') #123
int('1010', 2) #10


'''
enumerate
enumerate(iterable,start=0)
주로 순서가 있는 자료형(리스트, 튜플 등)의 각 요소에 대해 인덱스와 값을 동시에 반환하는데 사용됩니다.
bin, oct, hex  int
bin(x), oct(x), hex(x)
10진 정수 x에 대한 2진수, 8진수, 16진수 문자열 반환
int(str, base=10)
문자열 str을 10진수로 변환
'''
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)
    
'''    
eval 보안?
eval(expr,[globals[,locals]])
문자열로 표시된 파이썬 코드를 실행하고 결과를 반환
'''
result = eval('2 + 3 * 4')
print(result)  # 출력 결과: 14

'''
filter
filter(func,seq)
시퀀스의 각 요소에 대해 함수를 적용하여 결과가 True인 것만 모아서 리스트로 반환하는 함수

리스트에서 짝수만 추출하는 예시
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력 결과: [2, 4, 6, 8, 10]

'''
map
map(함수, 시퀀스)
시퀀스의 각 원소에 대해 지정된 함수를 적용하여, 새로운 리스트를 반환
'''
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # 출력결과: [1, 4, 9, 16, 25]


'''
ord
ord(ch)
ch에 대한 ASCII 코드 반환
ord('A') > 65
'''

'''
repr <-> eval 
repr(obj)
obj를 문자열로 변환
repr(b'0011') > "b'0011'"
'''
my_list = [1, 2, 3]
list_str = repr(my_list)
print(list_str)  # 출력 결과: '[1, 2, 3]'


'''
round
round(x, n=0)
실수 x를 소수점 아래 n자리로 반올림하여 반환
'''
num1 = 3.141592653589793238
num2 = 2.71828182845904523536

result1 = round(num1)    # 반올림하여 정수로 변환
result2 = round(num2, 3) # 소수점 셋째자리까지 반올림

print(result1) # 출력 결과: 3
print(result2) # 출력 결과: 2.718

'''
zip
zip(seq, *seqs)
seq 요소와 *seqs 요소의 튜플 쌍으로 이루어진 리스트 iterable 반환
'''
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 32, 28]

for name, age in zip(names, ages):
    print(name, age)

'''
enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를
모두 찾아 출력하는 프로그램을 작성하라. 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.

두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(),
'3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는
프로그램을 작성하라.

다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때
{'led':'on', 'motor':'off', 'switch':off'} 반환.
Hint: dict([['a','b'], ['c', 'd']]) -> {'a': 'b', 'c': 'd'}
'''
#1
'''str=input('문자입력 :')

flag=0

for i,st in enumerate(str):
    if st =='a':
        print(i)
        flag=1
        
if flag==0:
    print('a가 없습니다')'''

#2
'''def sum(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return n*m
def div(n,m):
    return n/m
table = { '1':sum '2':sub '3':mul '4':div }

func = table['1']
print(func(2,3))'''

#3 eval split &, =

#li=[a[0].split('=')+a[1].split('=')+a[1].split('=')]
#li = dict(li)
#print(str)

'''
str = 'led=on&motor=off&switch=off'

a=str.split('&')

temp = []

for item in a:
    temp.append(item.split('='))
    
print(temp)
'''

def str_parse(str):
    a=str.split('&')

    temp = []

    for item in a:
        temp.append(item.split('='))
    
    return dict(temp)

print(str_parse('led=on&motor=off&switch=off'))

#========================================================
'''
클래스 정의

class 클래스이름:
    # 클래스 멤버 변수
    클래스변수 = 값
    
    # 생성자 메서드
    def __init__(self, 매개변수):
        # 인스턴스 멤버 변수
        self.인스턴스변수 = 매개변수
        
    # 인스턴스 메서드
    def 메서드이름(self, 매개변수):
        # 메서드 내용
'''
'''
생성자
class 클래스이름:
    # 클래스 멤버 변수
    클래스변수 = 값
    
    # 생성자 메서드
    def __init__(self, 매개변수):
        # 인스턴스 멤버 변수
        self.인스턴스변수 = 매개변수
        
    # 인스턴스 메서드
    def 메서드이름(self, 매개변수):
        # 메서드 내용
'''
#self
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12

# 인스턴스(Instance)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(5, 6)

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30

# 인스턴스 변수(Instance Variable)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 변수를 이용하여 객체 생성
rectangle1 = Rectangle(3, 4)
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4

# 인스턴스 변수 값 변경
rectangle1.width = 5
print(rectangle1.width) # 출력 결과: 5

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 20

#클래스 변수(Class Variable)

class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

# 클래스 변수 값을 출력
print(Rectangle.count) # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
print(Rectangle.count) # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
print(Rectangle.count) # 출력 결과: 2 생성될 때 마다 영향을 끼침. 모든객체가 공유

#인스턴스 메서드(Instance Method)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle1.perimeter()) # 출력 결과: 14

#자전거 클래스(Bicycle class)

class Bicycle:
    # 생성자 메서드
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    # 인스턴스 메서드
    def speed_up(self, increment):
        self.speed += increment

    def apply_brake(self, decrement):
        self.speed -= decrement

# Bicycle 클래스를 이용하여 객체 생성
my_bike = Bicycle(6, 0)
print(my_bike.speed) # 출력 결과: 0

# 인스턴스 메서드 호출
my_bike.speed_up(3)
print(my_bike.speed) # 출력 결과: 3

my_bike.apply_brake(1)
print(my_bike.speed) # 출력 결과: 2

'''
클래스 메서드
인스턴스 메서드와의 차이점은 첫 번째 인자가 self 대신 cls임과 동시에,
클래스 변수에 대한 접근 및 수정이 가능하다.
클래스 메서드는 @classmethod 데코레이터를 이용하여 정의
'''
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2

#계산기 클래스(Calculator class)

class Calculator:
    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2

# Calculator 클래스를 이용하여 객체 생성
my_calculator = Calculator()
print(my_calculator.calculate(2, 3)) # 출력 결과: 5


# 클래스 메서드 호출
Calculator.set_operator('*')
print(my_calculator.calculate(2, 3)) # 출력 결과: 6

'''
Deposit 클래스를 생성하라. 이 클래스는 세 개의 인스턴스 변수 initial과 interest,
n을 갖는다. initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
인스턴스 메소드 profit()은 n년 후 원리금을 반환한다.
n년 후 원리금은 initial * (1 + interest)n이다.
Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는
프로그램을 작성하라. 단 원리금은 정수로 표시되어야 한다.
'''
'''
class Deposit:
    def _init_(self, initial, interst, n):
        self.initial=initial
        self.interst=interst
        self.n=n
        
    def profit(self):
        return int(self.initial * (1 + self.interest)**self.n)
    
x=Deposit(1000000,0.035,7)
print(x.profit())
'''

'''
캡슐화
인스턴스 변수 이름 앞에 밑줄 두 개(__)를 붙여서 비공개 인스턴스 변수로 만들어
캡슐화를 구현
'''
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age 인스턴스 변수를 비공개로 설정

p = Person("Alice", 25)
print(p.name)   # Alice
print(p.__age)  # 비공개 인스턴스 변수에 접근 시 에러 발생
'''

'''
getter/setter 메서드
직접적으로 인스턴스 변수에 접근할 수 없는 경우, 메서드를 통해 간접적으로 접근하는 방법
'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

p = Person("John", 30)
print(p.get_name())  # "John" 출력
p.set_name("Alice")
print(p.get_name())  # "Alice" 출력

#상속(Inheritance)
#클래스 상속의 예시
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")
        print("나이는", self.age, "살입니다.")
class Teacher(People):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def show_info(self):
        super().introduce()
        print("제 전공은", self.subject, "입니다.")
teacher = Teacher("홍길동", 30, "수학")
teacher.show_info()

# super()는 상속 관계에서 부모 클래스의 메서드나 인스턴스 변수를 호출할 때 사용

'''
예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고 부모 클래스의
age, name 인스턴스 변수를 이용할 수 있는가? 이용할 수 없다면 그 이유는?
이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?
'''
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
    
    # 수정한 부분
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

'''
t = Techer(35,'kim','highschool')
t.introMe()
t.set_name('lee')
t.introMe
t.showSchool()'''

'''
다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
getID() 메소드는 employeeID를 반환하는 메소드이다.
Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이,
ID를 출력하라.
'''
'''
class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID=employeeID
        
        def getID(self):
            return self.employeeID
        
        
emp = Employee("동양", 65, 2019)
print(f'ID:{emp.getID()}')
'''
#다중 상속
class Parent1:
    def method1(self):
        print("Parent1's method1")

class Parent2:
    def method2(self):
        print("Parent2's method2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Parent1's method1
c.method2()  # Parent2's method2

#메서드 오버라이딩(Method Overriding)
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

# 메서드 오버라이딩을 이용한 다형성 구현
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() # 각 객체에 따라 다른 동작을 수행

#사칙연산을 구현하는 예시
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

class AdvancedCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

c = Calculator()
print(c.add(2, 3))        # 5
print(c.subtract(5, 1))   # 4
print(c.multiply(4, 6))   # 24
print(c.divide(10, 2))    # 5.0

ac = AdvancedCalculator()
print(ac.divide(10, 0))   # Cannot divide by zero
print(ac.divide(10, 2))   # 5.0

#게임 캐릭터를 구현하는 예시
class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
    
    def attack(self):
        print(f"{self.name} attacks with a normal attack.")

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength
    
    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")
    
    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")

class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic
    
    def attack(self):
        print(f"{self.name} casts a magic missile.")
    
    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")


c = Character("Bob", 10, 100)
c.attack()  # Bob attacks with a normal attack.

w = Warrior("Conan", 20, 200, 15)
w.attack()  # Conan attacks with a mighty swing.
w.smash()   # Conan smashes the ground with a powerful blow.

m = Mage("Merlin", 15, 150, 30)
m.attack()  # Merlin casts a magic missile.
m.teleport()  # Merlin teleports to a nearby location.

# 클래스 분리
class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break

game = Game("Alice",120,15, "Goblin", 60, 8)
game.fight()


# 분리
# Player 클래스
class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")


# Monster 클래스
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

# Game 클래스
class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    def create_player(self, name, hp, attack):######
        self.player = Player(name, hp, attack)

    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)######

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break

game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()

# 추상 클래스(abstract class)란, 인스턴스를 생성할 수 없는 클래스
# 특정한 인터페이스를 구현해야 하는 클래스들이 반드시 일정한 형태의 메서드를 구현하도록 강제할 수 있다.
'''
추상 클래스를 정의하는 예시
abc 모듈을 import합니다.
ABC 클래스를 상속받아 추상 클래스를 생성합니다.
추상 메서드를 정의합니다. 추상 메서드는 구현 코드가 없이 메서드 이름과 매개변수만을 가진 메서드를 말합니다.
@abstractmethod 데코레이터를 이용해 메서드를 추상 메서드로 정의합니다.
이를 통해 하위 클래스가 해당 메서드를 구현하지 않으면 오류가 발생합니다.
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_num_wheels(self):
        pass

class Car(Vehicle):
    def get_num_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_num_wheels(self):
        return 2
    
#추상 클래스를 사용하여 여러 클래스가 일정한 형태의 메서드를 구현하도록 강제하는 예제
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car started.")
        
    def stop(self):
        print("Car stopped.")


class Bike(Vehicle):
    def start(self):
        print("Bike started.")
        
    def stop(self):
        print("Bike stopped.")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()

#다형성(polymorphism)
    
class 동물:
    def 소리내기(self):
        pass

class 개(동물):
    def 소리내기(self):
        print("멍멍!")

class 고양이(동물):
    def 소리내기(self):
        print("야옹!")

def 동물들_소리내기(동물_리스트):
    for 동물_인스턴스 in 동물_리스트:
        동물_인스턴스.소리내기()

개_인스턴스 = 개()
고양이_인스턴스 = 고양이()

동물들 = [개_인스턴스, 고양이_인스턴스]
동물들_소리내기(동물들)

#메서드 오버라이딩 (Method Overriding): 다형성을 만드는 하나의 방법
class 동물:
    def 소리내기(self):
        print("동물이 소리를 냅니다.")

class 개(동물):
    def 소리내기(self):  # 메서드 오버라이딩
        print("멍멍!")

개_인스턴스 = 개()
개_인스턴스.소리내기()  # 결과: 멍멍!


'''
문제: 학생 정보를 관리하는 프로그램을 만드세요.
학생(Student) 클래스
인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적(avg_score)
메서드: get_info() - 학생의 정보를 문자열로 반환

학생들을 관리하는 클래스(StudentManager)
인스턴스 변수: 학생들(student_list)
메서드:
add_student(student): 학생을 리스트에 추가하는 메서드
remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
find_student(student_id): 학번을 이용해 학생을 찾는 메서드
show_all_students(): 모든 학생의 정보를 출력하는 메서드
'''
class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name=name
        self.student_id=student_id
        self.year=year
        self.major=major
        self.avg_score=avg_score
    
    def get_info(self):
        return f"이름:{self.name}, 학번{self.student_id}, 학년{self.year}, 전공{self.major}, 평균성적{self.avg_score}"

class StudentManager:
    def __init__(self,student_list):
        self.student_list = []
    
    def add_student(self,student):
        self.student_list.append(student)
        
    def show_all_students(self):
        for student in self.sutdent_list:
            print(student.get_info())
            
    def remove_student(self,student_id): # list 돌면서 입력값과 같은 id가 있으면 삭제
        for student in self.student_list:
            if student.student_id == student_id:
                self.sutdent_list.remove(student)
                return
        print(f'{student_id}학번을 가진 학생이 없습니다.')
    
'''    def find_student(self,student_id): # list 돌면서 입력값과 같은 id가 있으면 삭제
        for student in self.student_list:
            if student.student_id == student_id:
                print(f'{student_id}는 )
                return
        print(f'{student_id}학번을 가진 학생이 없습니다.')
'''    
'''student_manager = StudentManager()

sutdent1 = student('김아무개','20230001',2, '컴퓨터공학','90.5')
sutdent2 = student('김무개','20230002',5, '퓨터공학','80.5')
sutdent3 = student('김아개','20230003',4, '컴터공학','91.5')
sutdent4 = student('김아무','20230004',1, '컴퓨공학','70.5')

student_manager.add_student(sutdent1)
student_manager.add_student(sutdent2)
student_manager.add_student(sutdent3)
student_manager.add_student(sutdent4)

student_manager.show_all_students()

student_manager.remove_student('20230002')'''




#=============================================================================
#모듈 불러오기
'''
dir() 함수
모듈이나 클래스에 포함된 변수, 메소드, 클래스 등의 속성들을 확인할 수 있습니다.
random 모듈에 대한 dir() 사용 예시'''
import random

# random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
print(dir(random))

# random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
print(help(random.choice))

# from import 방식
from math import sqrt, pi

print(sqrt(4))  # 출력 결과: 2.0
print(pi)  # 출력 결과: 3.141592653589793

# * 방식   
from math import *

print(sqrt(9))  # 출력 결과: 3.0
print(pi)  # 출력 결과: 3.141592653589793
print(sin(pi/2))  # 출력 결과: 1.0

#import as 모듈에 별칭(alias)
import math as m

print(m.sqrt(4))  # 2.0
print(m.pi)  # 3.141592653589793

#sys.path 현재 파이썬 인터프리터가 모듈을 검색할 경로들을 담고 있는 리스트
# 현재의 디렉토리와 시스템 경로 변수 출력하기
import os, sys
print(os.getcwd()) #현재 디렉토리 표시
print(sys.path) #환경변수에 지정된 디렉토리

# OS
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 새로운 디렉토리 생성
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"새로운 디렉토리 '{new_dir}'가 생성되었습니다.")

# 생성한 디렉토리 내에 파일 생성
new_file = "new_file.txt"
with open(os.path.join(new_dir, new_file), "w") as f:
    f.write("새로운 파일 내용")
print(f"'{new_file}' 파일이 '{new_dir}' 디렉토리 내에 생성되었습니다.")

# 지정된 디렉토리의 파일 및 디렉토리 목록 확인
list_dir = os.listdir(new_dir)
print(f"'{new_dir}' 디렉토리 내의 파일 및 디렉토리 목록: {list_dir}")

# 파일인지 디렉토리인지 확인
for item in list_dir:
    item_path = os.path.join(new_dir, item)
    if os.path.isfile(item_path):
        print(f"'{item_path}'는 파일입니다.")
    elif os.path.isdir(item_path):
        print(f"'{item_path}'는 디렉토리입니다.")

# 파일 삭제
os.remove(os.path.join(new_dir, new_file))
print(f"'{new_file}' 파일이 삭제되었습니다.")

# 디렉토리 삭제
os.rmdir(new_dir)
print(f"'{new_dir}' 디렉토리가 삭제되었습니다.")


#sys
'''
import sys

# sys.argv 예시
print("명령행 인자(argument) 리스트:", sys.argv)

# sys.getsizeof() 예시
a = [1, 2, 3]
print("a의 크기:", sys.getsizeof(a))

# sys.stdin, sys.stdout, sys.stderr 예시
sys.stdout.write("표준 출력 테스트\n")
sys.stderr.write("표준 오류 출력 테스트\n")
input_data = sys.stdin.readline().strip()
print("입력값:", input_data)

# sys.version, sys.platform 예시
print("현재 파이썬 버전:", sys.version)
print("현재 시스템 플랫폼:", sys.platform)

# sys.path 예시
print("모듈 검색 경로:", sys.path)'''

# math
import math

# 반올림 함수
print(math.ceil(3.2))    # 결과: 4
print(math.ceil(-3.2))   # 결과: -3

print(math.floor(3.2))   # 결과: 3
print(math.floor(-3.2))  # 결과: -4

print(round(3.2))        # 결과: 3
print(round(-3.2))       # 결과: -3
print(round(3.5))        # 결과: 4
print(round(-3.5))       # 결과: -4

print(math.trunc(3.7))    # 결과: 3
print(math.trunc(-3.7))   # 결과: -3

# 절댓값 함수
print(abs(3.2))          # 결과: 3.2
print(abs(-3.2))         # 결과: 3.2

print(math.fabs(3.2))     # 결과: 3.2
print(math.fabs(-3.2))    # 결과: 3.2

# datetime

import datetime

# 현재 날짜
today = datetime.date.today()

# 100일 후의 날짜
hundred_days_later = today + datetime.timedelta(days=100)

# 1000일 후의 날짜
thousand_days_later = today + datetime.timedelta(days=1000)

# 결과 출력
print("100일 후:", hundred_days_later)
print("1000일 후:", thousand_days_later)

# calendar
import calendar

# 2023년 3월의 달력을 출력합니다.
print("2023년 3월의 달력:")
print(calendar.month(2023, 3))

# 2023년 3월 15일의 요일을 확인합니다. (월요일: 0, 화요일: 1, ..., 일요일: 6)
year = 2023
month = 3
day = 15
weekday = calendar.weekday(year, month, day)
print("2023년 3월 15일은 요일 인덱스 {}에 해당하는 요일입니다.".format(weekday))

# 요일 인덱스를 사용하여 요일 이름을 가져옵니다.
weekday_name = calendar.day_name[weekday]
print("2023년 3월 15일은 {}입니다.".format(weekday_name))

# numpy

import numpy as np

# 1차원 배열 생성
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# 2차원 배열 생성
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b)
# [[1 2]
#  [3 4]
#  [5 6]]

import numpy as np

# 배열 더하기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)  # [5 7 9]

# 배열 곱하기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)  # [4 10 18]

# 행렬 곱셈
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(c)
# [[19 22]
#  [43 50]]

import numpy as np

# 배열 인덱싱
a = np.array([1, 2, 3, 4, 5])
print(a[0])  # 1
print(a[-1])  # 5

# 2차원 배열 인덱싱
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b[0, 1])  # 2

# 배열 슬라이싱
a = np.array([1, 2, 3, 4, 5])
print(a[1:4])  # [2 3 4]

# 2차원 배열 슬라이싱
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b[1:3, :]) 
# [[3 4]
#  [5 6]]

# 배열 크기 변경
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.reshape(a, (2, 3))
print(b)
# [[1 2 3]
#  [4 5 6]]

# 배열 전치
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.transpose(a)
print(b)
# [[1 3 5]
#  [2 4 6]]

# pandas
'''
pandas는 파이썬에서 데이터 분석과 조작을 위한 라이브러리입니다. 
데이터 불러오기 및 저장: pandas는 CSV, 엑셀, SQL, JSON, HTML 등 다양한 데이터 형식을 지원하여 데이터를 불러오고 저장할 수 있습니다.
데이터 정제: pandas를 사용하면 결측치 처리, 중복 제거, 데이터 타입 변환 등 데이터 정제 작업을 수행할 수 있습니다.
데이터 조작: 데이터를 필터링, 정렬, 그룹화, 피벗, 병합, 조인 등 다양한 방법으로 조작할 수 있습니다.
데이터 분석: pandas는 기술통계, 시계열 분석, 빈도 계산 등 데이터 분석 작업을 수행하는 데 유용한 함수를 제공합니다.

Series: 1차원 데이터 구조로, 인덱스와 값으로 구성됩니다.
DataFrame: 2차원 데이터 구조로, 행과 열로 구성됩니다.
Index: Series나 DataFrame의 인덱스를 나타내는 객체입니다.
GroupBy: 데이터를 그룹으로 나누어서 통계 정보를 계산합니다.
merge(): 두 개 이상의 DataFrame을 병합합니다.
concat(): 여러 개의 DataFrame을 연결합니다.
read_csv(): CSV 파일을 읽어 DataFrame으로 반환합니다.
to_csv(): DataFrame을 CSV 파일로 저장합니다.
'''
import pandas as pd

# 시리즈(Series) 예시
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

# 데이터프레임(DataFrame) 예시
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'year': [2017, 2017, 2018, 2019],
        'score': [100, 95, 80, 90]}
df = pd.DataFrame(data)
print(df)

# 데이터프레임에서 열 선택 예시
print(df['name'])
print(df.year)

# 조건을 이용한 데이터 선택 예시
print(df[df.year > 2017])

# 데이터프레임에 열 추가 예시
df['grade'] = ['A', 'A-', 'B+', 'B']
print(df)

# 데이터프레임에서 행 선택 예시
print(df.loc[0])
print(df.loc[[0, 2]])

# 데이터프레임에서 행과 열 선택 예시
print(df.loc[0, 'name'])
print(df.loc[[0, 2], ['name', 'score']])

#matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label='sin')
plt.plot(x, y_cos, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()