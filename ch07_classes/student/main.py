class Student:
    # 생성자 정의
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        # 성적을 저장하기 위한 빈 딕셔너리 -> 과목명을 key / 점수를 value 로 예정
        self._grades = {}

    # python 버전의 getter 에 해당하는 메서드 정의 방식
    @property
    def name(self):
        return self._name

    # python 버전의 setter 의 예시
    @name.setter
    def name(self, value):
        self._name = value

# 객체 생성
student1 = Student("김일", 2026001)
# getter 의 호출   - 주의 사항 : 객체명.속성명도 아니고 객체명.메서드명() - 소괄호 열고 닫고도 아니라는 점에 주목해야 합니다.
print(f"학생 이름 : {student1.name}")
# setter 호출 예시
student1.name = "김영"
# getter 재호출
print(f"변경된 학생 이름 : {student1.name}")
print(student1._name)   # 속성으로도 여전히 불러낼 수 있습니다.

"""
이상의 코드에서 확인 가능한 점은 Java 기준으로 python 코드를 해석할 때 의문스러운 점이 많다는 점입니다.

1. _name 이라는 속성이 있는데 객체명.name 을 통해서 "김일" / "김영" 이라는 속성값이 출력된다는 점 : 그런데 객체명._name 도 작동한다는 점

2. 객체명._name = "김영"이 아니라 객체명.name = "김영" 으로 재대입한 것처럼 보이지 setter 의 호출로 보이지 않는다는 점. 당연히 객체명.set_name("김영") 이어야 하지 않냐는 의문점 입니다.

그런데 이건 Java 기준으로 본거고, python 으로 풀었을 때는, _name / name 이 서로 다른 개념으로 보이지만 '_' 가 붙으면 파이썬 언어 내부적으로 동일한 속성으로 처리해줍니다.

객체명.속성명 뒤에 () 가 없음에도 불구하고 파이썬은 이걸 그냥 메서드처럼 처리해준다는 점입니다. 그래서 그냥 객체명.속성명이면 getter 로 처리해주고 '객체명.속성명 = 데이터' 면 알아서 setter 로 처리해줍니다.

그런데 그 '알아서' 처리하기 위한 필수적인 작업이 '@property' 와 '속성명.setter' 라는 데코레이터(decorator) 때문입니다.

원래는 이거 자동 생성되기 때문에 일일이 @ 달고 _속성명인지 / 그냥 속성명인지 따질 필요가 없는데 저희는 backend 를 파이썬으로 짜지 않기 때문에 현재 쓸모가 좀 없는 상황입니다. 현재 수준으로는 python 으로 백엔드를 작성할 때 필요할 때가 있고, 이렇게 getter / setter 를 쓴다는 것으로 알아두시면 되겠습니다.
"""