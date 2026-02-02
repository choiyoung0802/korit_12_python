"""
1. if 문
    - if 문은 조건이 참일 때만 해당 블록의 코드 실행
2. if-else 문
    - if 문은 조건이 True 일 때 / False 일 때는 else 부분 실행
3. if-elif-else 문
"""
# age = int(input("나이를 입력하세요 >>> "))
# if age >= 20:
#     print("성인입니다.")
# elif age < 20 and age > 13:
#     print("청소년입니다.")
# else:
#     print("어린이입니다.")
"""
if 조건문의 전체 형식 :

if 조건식1:
    실행문1
(elif 조건식2:)
    (실행문2)
(elif 조건식3:)
    (실행문3)
(else:)
    (실행문4)

Nested - if 문도 쓸 수 있습니다.
"""
age = 21
has_ticket = True
ticket_count = 10   # boolean 자료형 처음 변수 선언해봤습니다.
print(type(has_ticket)) # 결과값 : <class 'bool'>
if age >= 19:
    if has_ticket:
        print("영화관 입장이 가능합니다.")
    else:
        print("티켓을 구매하세요.")
else:
    print("미성년자는 출입할 수 없습니다.")
"""
비교 연산자
    1) == : 같다
    2) != : 같지않다.
    3) > : 초과
    4) < : 미만
    5) >= : 이상
    6) <= : 이하
논리 연산자
    1) and : &&와 같음
    2) or : ||와 같음
    3) not : !와 같음. 근데 python 에 not= 이런건 없고 != 는 있어서 혼란스러울 때가 있습니다.
내부에 leap_year 디렉토리 생성 -> main
"""
