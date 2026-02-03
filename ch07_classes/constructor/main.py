"""
아까 전에 일종의 setter 같은 것을 이용하여 속성에 속성값을 대입해줬습니다. 굳이 field 선언을 하지 않았는데 method 내에서 객체의 속성을 정의할 수 있다는 점이 특이했습니다. 그런데 이렇게 메서드를 경유하게 되면 기본 생성자를 통해서 객체를 생성한 다음에 속성에 값을 대입해야 하는 과정을 거쳐야 하는 것을 알 수 있습니다.

객체 생성시 기본 생성자 호출 -> set_info() 메서드 호출해서 값 대입

그러니까, AllArgsConstructor 에 해당되는 걸 python 에서 정의할 수 있지 않을까
"""
# 클래스 정의
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")

# 객체 생성 시 (기본 생성자 호출 -> set_info() 호출 -> show_info() 호출)
satang = Candy()
satang.set_info("구형", "갈색")
satang.show_info()
"""
속성값에 대한 제한이 따로 있지 않다면(예를 들어 나이에 123098살을 입력하는 등의) 굳이 빈 객체 만들어놓고 거기에 값 대입하는 것이 비효율적으로 느껴집니다. 그래서 저희는 AllArgsConstructor 를 도입할겁니다.

Java / JS 에서의 생성자명은 클래스명과 동일하거나 constructor 를 쓰는데, python 만 또 자기 혼자서 이상한거 씁니다. __init__() 입니다. 언더스코어 두 개임.
"""
class Candy2:
    # 생성자 정의
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        print("사탕 객체가 생성되었습니다.")

    def show_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")

# 객체 생성 방식에서의 차이가 있습니다.
satang2 = Candy2(shape="정육면체", color="흰색")
satang2.show_info()
"""
소멸자
"""
class Sample:
    # 생성자 정의
    def __init__(self):
        print("인스턴스가 생성되었습니다.")

    # 소멸자 정의
    def __del__(self):
        print("인스턴스가 소멸되었습니다.")

# 객체 생성
sample = Sample()
print()
# 객체 소멸자 호출 방법
del sample      # del 객체명입니다. 소멸자는 객체 메모리를 날려야하기 때문에 객체에 종속이 아닙니다.
print("객체 소멸 이후 작성한 코드입니다. 프로그램 종료 전에 이미 객체가 삭제되었음을 확인할 수 있습니다.")
"""
지금 보니까 코드 다 돌아가면 객체가 소멸되는 것 같은데 굳이 소멸자를 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지하기 때문에 객체가 생성될 때마다 그곳에서 불려나오게 됩니다. 하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에 소멸자를 통해서 강제로 객체를 삭제해주게 되면 메모리 관리가 된다고 볼 수 있습니다.

기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB 
"""
class USB:
    def __init__(self, capacity):
        self.capacity = capacity
        print("USB 객체가 생성되었습니다.")

    def get_info(self):
        print(f"{self.capacity}GB USB")

usb = USB(64)
usb.get_info()

class Person:
    def __init__(self, name):
        self.name = name
        print(f"{name} is born.")

    def __del__(self):
        print(f"{self.name} is dead.")

man = Person("james")
woman = Person("emily")

del man
print("위 문장에서 man 객체 소멸시켰습니다.")
"""
emily is dead. 맨 마지막에 이 친구가 나오는 이유 -> 프로그램 종료할 때 원래 객체들 다 소멸시킵니다.
"""