"""
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스)
    본문
"""
# 부모 클래스 정의
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name}이(가) {food}(을)를 먹습니다.")

    def drink(self, drink_name):
        print(f"{self.name}이(가) {drink_name}을(를) 먹습니다.")

person1 = Person("김영")
person1.eat("감자")

# 서브 클래스 정의
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f"{self.name}은(는) {self.school}에서 공부를 합니다.")

    def drink(self, drink_name):
        print(f"{self.school}에서", end=" ")
        super().drink(drink_name)

# 서브 클래스의 객체 생성
potter = Student(name="해리포터", school="호그와트")
potter.study()
potter.eat("라면")    # 부모의 메서드를 정의하는 일 없이 그대로 쓸 수 있음
potter.drink("투샷아이스아메리카노")      # overriding 된 메서드를 호출
"""
1. 서브 클래스의 __init__()
    Java 와 마찬가지로 서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼 클래스의 생성자를 먼저 호출' 하는 코드를 작성하셔야 합니다.
    
    super() 는 잘 생각해보시면 슈퍼 클래스의 생성자라고 해석할 수 있을 겁니다. potter = Student() 에서 보면 알 수 있듯이 그러면 슈퍼 클래스의 객체가 .__init__(name) 이라는 메서드를 호출했다고 해설할 수 있겠네요.
    즉, 이상의 코드에서 Student 생성자의 호출이 완벽하게 마무리 되려면 super().__init__(name) 에 의해서 슈퍼 클래스인 Person 의 생성자가 먼저 호출이 완료되고 -> Person 크랠스의 인스턴스가 생성됩니다.
    이후에 슈퍼 클래스의 인스턴스 변수인 name 이 서브 클래스로 전달되고, 그 다음 서브 클래스에서 school 인스턴스 변수를 선언 및 초기화하여 서브 클래스의 인스턴스가 생성완료됩니다.
    
    : 생성자를 호출했다면 -> 객체가 생성되었다고 볼 수 있는데 -> 그렇다면 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가 있는거 아니냐 -> 맞긴한데 그러면 별개의 인스턴스라고 봐야 하냐면 그게 또 좀 애매합니다.
    
    Java 에서는 super() -> 얘는 생성자 / super.메서드명() 으로 super 자체가 객체인 경우가 있었지만 python 에서는 super() 로 일원화되어있습니다.

2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스(부모 생성자 호출 했으니까요)
    Student 클래스의 객체는 Student 의 인스턴스이면서 Person 의 인스턴스.
    
    Java 를 기준으로 instanceof 연산자 역할을 하는 것이 JS 에서는 typeof 연산자가 있었는데, python 에서는 isinstance() 함수가 있습니다. -> 다 소문자입니다.

형식 :
isinstance(객체명, 클래스명) -> boolean
"""
print(isinstance(potter, Student))  # 결과값 : True
print(isinstance(potter, Person))   # 결과값 : True
print(isinstance(person1, Student)) # 결과값 : False
print(isinstance(person1, Person))  # 결과값 : True

print(issubclass(Student, Person))  # 결과값 : True 객체 안 만들고 클래스 간의 위계만 확인하고 싶으면 쓸 수 있겠습니다.

"""
3. 다음 지시 사항을 읽고 Hybrid 클래스를 구현하시오.

지시 사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.
    
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
"""
class Car:
    max_oil = 50    # 클래스 변수
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return      # 기름을 0이거나 음수값으로 입력하면 메서드 그대로 종료
        self.oil += oil
        if self.oil > Car.max_oil:  # 클래스 변수의 한계갑 초과라면
            self.oil = Car.max_oil
        print(f"기름을 {self.oil} 주유 했습니다.")

    def car_info(self):
        print(f"현재 주유 상태 : {self.oil}")

class Hybrid(Car):
    max_charge = 30
    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount
        print("하이브리드 차량이 생산되었습니다.")

    def charge(self, amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > Hybrid.max_charge:
            self.amount = Hybrid.max_charge
        print(f"전기를 {self.amount} 충전 했습니다.")

    def hybrid_info(self):
        super().car_info()  # 현재 주유 상태가 불러와지겠네요. -> 어차피 부모 객체가 생성됐기 때문에 super() 키워드를 통해 메서드를 호출할 수 있을겁니다. 그래서 저 같으면 hybrid_info() 라는 별개의 메서드라기 보다는 car_info() 메서드로 만든 다음에 재정의했을 것 같습니다.
        print(f"현재 충전 상태 : {self.amount}")

car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

"""
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. -> call3()
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 -> call3()
        (넓이 = 너비 * 높이)
3. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.

 
circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____
너비가 10, 높이가 8인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
"""
print()
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"{self.name}")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f"반지름이 {self.radius}인 {self.name}이 생성되었습니다.")

    def area(self):
        return 3.14 * self.radius ** 2

    def draw(self):
        print(f"이름이 {self.name}인 원의 넓이는 {self.area()} 입니다.")

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f"너비가 {self.width}, 높이가 {self.height}인 {self.name}이 생성되었습니다.")

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f"이름이 {self.name}인 직사각형의 넓이는 {self.area()} 입니다.")

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')