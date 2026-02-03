"""
클래스 정의 형식 :

class 클래스명(파스칼케이스):
    본문(attribute / method)

객체 생성 형식 :
객체명 = 클래스명()    # 생성자 호출은 맞는데 new 가 없습니다.
"""
# 클래스 정의 예시
class WaffleMachine:
    pass            # 이거 클래스나 메서드에 쓰면 엔터쳤을 때 오류 안 남

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle) # 결과값 : <__main__.WaffleMachine object at 0x0000025073151940>
"""
클래스의 구성
1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닙니다(Java 때 제가 방이 가져야 할 구성요소는 뭐였냐고 질문했었습니다). 객체를 생성하기 위해서는 객체가 가져야 할 '값'과 '기능'을 지녀야 합니다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성은 두 가지로 나뉩니다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수(Java 에서는 얘를 static 변수라고 불렀습니다).
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
    
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 인스턴스 메서드
        3) 정적 메서드
    
    Java 에서는 this 썼었는데(아직 정의 중인 클래스에 대한 객체가 생성될 수 없으니 임의로 this 키워드를 썼었습니다), python 에서는 self 씁니다.
    
    self 키워드 : 인스턴스 변수에서 각각의 객체를 의미하기 위해서 self 키워드를 붙여줍니다. 인스턴스 메서드에서의 첫 번째 매개변수로 '항상' self 를 추가해야합니다(그래서 자동 생성됩니다).
"""
# 클래스 정의
class Person:
    # 메서드 정의(함수가 클래스 내에 있으니까 / 들여쓰기 주의해야 합니다)
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"연락처 : {self.tel}")
        print(f"주소 : {self.address}")

    def show_info2(self):
        return f"제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}이고, {self.address}에 살고 있습니다."

# 객체 생성
person1 = Person()
# Person 클래스의 인스턴스에서 인스턴스 메서드 호출 -> 왜? 첫 번째 매개변수가 self 였으니까
person1.set_info(age=20, tel="010-1234-5678", address="부산광역시 부산진구", name="김일")
# 이상의 코드에서 keyword argument 를 썼습니다. 어떤 속성에 어떤 값을 넣는지 아니까 굳이 Java 의 builder 패턴이 필요 없겠네요.
person1.show_info()
print(person1.show_info2())