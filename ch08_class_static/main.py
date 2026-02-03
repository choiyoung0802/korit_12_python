"""
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스 마다 서로 다른 값
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 접근 방식 - 인스턴스 접근(o) / 클래스 접근(x)
    클래스 변수 접근 방식 - 인스턴스 접근(o) / 클래스 접근(o)
"""
# 클래스 변수 예시
class Korean:
    country = "한국"                 # 클래스 변수 # 1
    def __init__(self, name, age, address):
        self.name = name            # 인스턴스 변수 # 1
        self.age = age              # 인스턴스 변수 # 2
        self.address = address      # 인스턴스 변수 # 3
# 객체 생성
korean = Korean("김일", 21, "서울특별시 마포구")
print(korean.name)      # 인스턴스 변수 참조
# 클래스 변수 참조
print(korean.country)   # 객체명.클래스변수명 으로 접근 가능
print(Korean.country)   # 클래스명.클래스변수명 으로 접근 가능

"""
객체명.클래스변수명을 통해서 클래스 변수에 접근이 가능하긴 한데, 클래스 내부 코드를 보기 전까지는 country 라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없습니다.

이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는
클래스명.클래스변수명을 통해서 참조하는 것이 권장됩니다.

2. 클래스 메서드
"""
class Korean2:
    country = "대한민국"        # 클래스 변수의 선언 및 초기화
    # 클래스 메서드의 정의 방법
    @classmethod                # @ decorator 를 달면 됩니다.
    def trip(cls, travelling_site):
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")
# 클래스 메서드 호출
Korean2.trip("대한민국")
Korean2.trip("미국")
# 객체 생성
person2 = Korean2()
person2.trip("일본")      # 객체명.클래스메서드() 호출도 가능하긴 합니다. 근데 마찬가지로 권장되지 않습니다.

"""
3. 정적 메서드(static method)
    정적 메서드 또한 self 를 쓰지 않음. 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미. self.속성명을 사용하여 인스턴스 변수의 값을 참조하는데 정적 메서드는 아예 첫번째 매개변수가 고정되어 있지 않습니다.
    - 인스턴스 변수를 참조하지 못한다는 점에서 클래스 메서드와의 공통점에 해당.
    
    인스턴스를 생성하지 않아도 사용할 수 있음 - 클래스 메서드와의 공통점 # 2
    
    특징 :
        1) 인스턴스 / 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 # 1
        4) 반드시 작성해야 하는 매개변수(self / cls)가 없음 -> 클래스 메서드와의 차이점 # 2

이상을 토대로 정적 메서드는 self/cls 를 둘 다 사용하지 않기 때문에 인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적합합니다.

즉, Java 에서의 정적 메서드 = 파이썬의 클래스 메서드 + 정적 메서드
"""
class Korean3:
    country = "한국"

    @staticmethod
    def slogan():
        print("Imagine Your Korea ! 🥱")

    @staticmethod
    def slogan2(str_example):
        print(f"Imagine Your Korea ! 😒 {str_example}")

# static method 의 호출
Korean3.slogan()
Korean3.slogan2("근데 너무 춥다.")

"""
기본 예제
가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의하겠습니다.
"""

class Bag:
    count = 0

    def __init__(self): # 여기 내부나 인스턴스메서드 내부에서 self 쓰면 속성이 선언되겠네요.
        Bag.count += 1  # cls.count 가 아니라 Bag.count 라는데에 주목해야합니다.
        # 즉, 생성자는 인스턴스 메서드이기 때문에 인스턴스 메서드 내에서 클래스 변수를 참조할 때는 cls.클래스변수명 이 아니라 클래스명.클래스변수명 으로 참조해야 한다는 점이 중요합니다.
        print("가방 객체가 생성되었습니다.")

    # 클래스 메서드의 정의
    @classmethod
    def sell(cls):
        print("가방이 팔렸습니다.")
        cls.count -= 1          # 얘는 클래스 메서드니까 Bag.count 가 아니라 cls.count 입니다.

    @classmethod
    def remain_bag(cls):
        return cls.count

# 객체 생성
bag1 = Bag()
print(f"현재 가방 재고 : {Bag.count}")    # 인스턴스메서드(생성자) 를 통해서 클래스 변수의 값을 바꿨습니다. 이 값은 모든 Bah 클래스의 인스턴스들이 공유한다는 점에서 정적 변수 개념과 동일합니다.
bag2 = Bag()
bag3 = Bag()
print(f"현재 가방 재고 : {Bag.count}")
bag1.sell()     # 객체명.클래스메서드() 호출했습니다. - 실제로 bag1 객체가 소멸된건 아닙니다.
print(f"현재 가방 재고 : {Bag.count}")
"""
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
"""
print()
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
        print(f"{name}이(가) 태어났습니다.")

    @classmethod
    def get_population(cls):
        return cls.count

    def __del__(self):
        print(f"RIP {self.name}")

man = Person("김일")
woman = Person("김이")
print(f"전체 인구수 : {Person.get_population()}")
del man