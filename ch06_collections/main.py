"""
python 대표 collection 종류
1. list (리스트) : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple (튜플) : 추가 / 수정 / 삭제가 불가능 / 순서 있음
3. set (세트) : 중복된 값의 저장이 불가능 / 순서 없음
4. dict (딕셔너리) : 키 + 값 으로 관리
"""
list_example = [30, 40, "김이", [100, "김삼"]]
print(list_example)
tuple_example = (10, 20, 30, "김사")
print(tuple_example)
set_example = {100, 200, 300, 400, "김오"}
print(set_example)
dict_example = {
    "이름": "김일",
    "나이": 20,
    "학교": "코리아아이티"
}
print(dict_example)
"""
1. list : 여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능. Java 기준 하나의 배열에 동일한 자료형만 들어갈 수 있는 것과 달리 강점을 가집니다.
"""
# list 의 선언 및 초기화
# li1 = [1,2,3,"김사"]
"""
    1.1 list 의 index / slice
        list 는 str 과 동일한 방식의 index / slicing 을 지원
        1) 인덱스 / 마이너스 인덱스
"""
# print(li1[0])
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])
# print(li1[-4])
"""
        2) slicing
            str 의 slicing 과 같이 "시작인덱스:종료인덱스:증감값" 으로 이루어져 있음.
"""
# li2 = [100, 3.14, "hello"]  # list 선언 및 초기화 방법 # 1
# li3 = list((4,5,6,7,8,9,0)) # list 선언 및 초기화 방법 # 2
# print(li3[0:4:2])   # 알아서 잘 해석해보도록
"""
        3) list 의 element 추가와 삭제
            list 에 새로운 요소를 추가할 때는 아까 한 것처럼 .append() 를 사용할 수 있습니다. 그리고 .insert() 도 존재합니다.
            .append() - 항상 마지막 인덱스에 element 를 추가
            .insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가
"""
# scores = [30, 40, 50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0, 90)
# print(scores)
"""
        .pop() 의 경우 NoArgs 라면 맨마지막 element 가 삭제됨.
        .pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 element 를 삭제함.
"""
# print(scores.pop())     # 결과값 : 100 맨마지막 인덱스의 element 를 삭제하고 걔를 return
# print(scores)
# print(scores.pop(0))    # 결과값 : 90
# print(scores)
"""
        교재에는 없는데 수업하는 삭제 메서드 : .remove(값) - list 내에 해당 값을 찾아내서 삭제함(인덱스가 아닙니다)
"""
# print(scores.remove(50))       # 결과값 : None
# scores.remove(300)             # 추후 예외처리를 하게 될 수도 있겠네요.
# scores.pop(10)
# print(scores)

li4 = [1,2,3,4,5,6,7,8,9,10]
print(li4)
for i in range(len(li4)):
    li4[i] *= 2
print(li4)

for li_num in li4:
    li_num = li_num * 2
    print(li_num)
# 귀찮다는 것을 알았습니다. 사실상 list 내에서의 element 들에 대해 연산을 일괄적으로 적응하는 method 가 따로 있습니다. 그리고 우리는 그것을 JS 에서 해보기도 했습니다.

modified_li4 = list(map(lambda num: num * 2, li4))
# 이상의 경우가 극단적으로 list 의 내부 각각의 element 들에 동일한 함수를 적용한 결과를 적용하는 map() 함수입니다. 그런데 저희는 JS 에서 배열의 method 로 사용했었습니다. 이상의 코드가 좀 문제가 있다면 map() 함수의 결과값이 map 객체에 해당하기 때문에 list() 함수를 통한 형변환을 해줘야한다는 점입니다.
print(modified_li4)
"""
    2. tuple(튜플) : 저장된 값을 변경할 수 없는 list 라고 생각하시면 됩니다. 순서는 없기 때문에 index 넘버의 사용과 slicing 은 사용 가능하지만 추가 / 수정 / 삭제 불가능.
"""
tu1 = (1,2,3)           # 튜플 생성 방법 # 1
tu2 = tuple((4,5,6))    # 튜플 생성 방법 # 2
tu3 = 7,8,9             # 튜플 생성 방법 # 3
print(type(tu3))

a, b, c = 7, 8, 9       # 복수의 변수 선언 및 초기화 방법 -> 변수 개수와 데이터 개수가 같으면 알아서 '순서대로' 대입됩니다.

# tu4 = 0  # <- 얘는 인트임
# print(type(tu4))

tu5 = "hello. ", "good morning. ", "my name is ", "kim-il ", "i am ", "20 ", "years old."
for word in tu5:    # 사실상 tuple 수업이 아니라 str method 관련이죠.
    print(word.title(), end="") # 결과값 : Hello. Good Morning. My Name Is Kim-Il I Am 20 Years Old.

print()
print(tu5)
"""
이상의 예시를 남겨두는 이유는 우리가 배우는 collection 의 개념과 내부 element 의 자료형이 서로 다르다는 점 때문입니다. tuple 자체는 추가 / 수정 / 삭제가 불가능했잖아요. 그런데 내부 element 자체는 str 이니까 데이터의 가공이 가능하겠네요.

    3. set 세트
        : 수학의 집합 개념, Java 와 동일합니다.
"""
set1 = {1,2,3}          # 세트 생성 방법 # 1
set2 = set({4,5,6})     # 세트 생성 방법 # 2

# 비어있는 list / tuple / set 생성 방법
li = []
tu = ()
se = {}
print(type(li))     # 결과값 : <class 'list'>
print(type(tu))     # 결과값 : <class 'tuple'>
print(type(se))     # 결과값 : <class 'dict'> .. 딕셔너리가 튀어나옴. 그래서
se1 = set({})    # 이렇게 만들어야함.
print(type(se1))
"""
list / tuple 은 index 가 존재한다고 했습니다. 그래서 이렇게 인덱스가 존재하는 애들을 sequence 로 분류하고, set / dictionary 의 경우에는 인덱스가 없기 때문에 비시퀸스라는 표현을 쓰기도 합니다.
    
    set 관련 메서드
    1. .add() - set 에 새로운 element 추가
    2. .remove() - 기존 element 삭제    -> index 가 없으니까 .pop() 이 없겠네요.
    3. .discard() - 기존 element 삭제
"""
se2 = {10,20,30}
se2.add(50)
print(se2) # 결과값 : {10, 20, 50, 30}
se2.remove(30) # 순서가 없기 때문에 '값'을 정확하게 입력해야만 합니다.
print(se2) # 결과값 : {10, 20, 50}

# remove() vs. discard()
# se2.remove(70) # 얘는 오류 발생
# print(se2)
se2.discard(70) # 얘는 오류가 발생하지 않습니다.
print(se2)
"""
.remove() 의 경우 argument 로 set 내에 있는 값을 정확하게 입력하지 않으면 KeyError 예외가 발생합니다. 반면에 discard() 의 경우에는 set 내에 없는 값을 입력했을 경우 해당 값이 애초에 존재하지 않기 때문에 변함 없는 상태로 메서드가 종료됩니다.
"""
# 인덱스 넘버는 없지만 향상된 for 문으로 내부 element 를 출력할 수는 있습니다.
for num in se2:
    print(num)  # 순서는 담보 못함
"""
    4. dict(딕셔너리) - Java 에서의 Map / JS 에서의 Object / JSON 과 비슷한 형식입니다.
"""
dict1 = {
    "이름": "김일",
    "나이": 20,
    "주소": ["서울특별시", "마포구", "목동"],
}
"""
전에 수업한 것처럼 155번 라인까지 key-value pair 이 있는데, 나중에 학교라는 key 를 추가하려고 할 때, 155번 라인에 콤마 치고 엔터 치고 "학교": "코리아아이티" 같은 식으로 추가하기 번거로우니까 나중에 확장성을 위해서 미리 콤마쳐두는 편입니다. 그러면 그냥 156번 라인에 추가 property 를 넣으면 되니까요.

정말정말정말 중요하게 제가 반복반복적으로 말하는 부분 dictionary 에서 반복문 돌리면 key 가 나옵니다.
"""
for key in dict1:
    print(key)

# 그렇다면 value 를 확인하기 위해서는
for key in dict1:
    print(dict1[key])

# key 들만 추출하는 메서드
print(dict1.keys())
print(type(dict1.keys())) # 결과값 : <class 'dict_keys'>
print(list(dict1.keys())) # 결과값 : ['이름', '나이', '주소']   리스트로 형변환함.

# value 들만 추출하는 메서드
print(dict1.values())
print(type(dict1.values())) # 결과값 : <class 'dict_values'>

# key 들 혹은 value 들만 뽑아서 list 를 만들고 싶다면 list() 형변환 함수를 사용하셔야 합니다.
"""
그래서 collections 수업을 할 때 매우 중요한 점은 list 를 배웠을 때 list 만 고려할 것이 아니라 set / tuple / dictionary 로 자료형을 변경하는 것이 가능한가입니다.

    1) dictionary 에서 property 추가 / 삭제
"""
dict1["직업"] = "웹 퍼블리셔"  # 기존에 없는 key 를 입력하고 = value 하시면 됩니다.
print(dict1)
dict1["직업"] = "웹 개발자"   # key 하나당 value 는 동일하기 때문에 재대입이 이루어집니다.
print(dict1)

print(dict1.pop("직업")) # key 를 알아야지 삭제 가능합니다 / .pop() 의 return 특정이 중요하죠. 그러면 최종 value 가 뽑혀져 나올테니까 # 결과값 : 웹 개발자

list1 = [10,20,30,40,50,60,70,80,90,100]
print(f"3 번째 요소로부터 7 번째 요소 = {list1[2:7]}")
print(f"3 번째 요소로부터 7 번째 요소중 2 번째 요소 = {list1[2:7][1]}")


"""
사용자로부터 1에서 12사이의 월을 입력 받아 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.
(윤년은 고려x)

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일 까지입니다.
# 1 : dictionary 를 이용하는 방법
# 2 : list 를 이용하는데, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 을 이용하는 방법
# 3 : list 를 이용하는데, [28, 30, 31] 을 이용하는 방법
"""

# month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))
# dict0 = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31,
# }
# print("↓ dict 사용")
# print(f"{month}월은 {dict0[month]}일 까지입니다.")
# list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print("↓ list 사용")
# print(f"{month}월은 {list2[month-1]}일 까지입니다.")
# list3 = [28, 30, 31]
# if month == 2:
#     last_date = list3[0]
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     last_date = list3[1]
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     last_date = list3[2]
# else:
#     print("잘못입력함")
#     last_date = "x"
# print(f"{month}월은 {last_date}일 까지입니다.")
"""
이상의 코드 라인에서 중요한 것은 in 개념입니다.
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체(iterable)이 올 수 있다는 점입니다.
그래서 
elif month_int in [ 1, 3, 5, 7, 8, 10, 12 ]:
    last_date = last_date_list2[2]
의 해석 부분이 중요한데, in 다음에 임의의 list를 초기화하여 month_int가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토했다고 해석할 수 있겠습니다.

( 1, 3, 5, 7, 8, 10, 12 ) 이렇게 초기화하더라도 전혀 문제가 없겠네요. tuple로 집어넣은 사례가 되겠습니다.

응용 예제
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.

짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장하세요.
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20, 25, 30]입니다.
입력 받은 숫자들 중 짝수는 [10, 20, 30]입니다.
"""
# bin_set = set({})
# for i in range(3):
#     travel = input("희망하는 수학여행지를 입력하세요 >>> ")
#     bin_set.add(travel)
# print(f"조사된 수학여행지는 {bin_set} 입니다.")
# print(f"조사된 수학여행지는 {list(bin_set)} 입니다.")
#
# bin_li = []
# even_li = []
# numbers = int(input("몇 개의 숫자를 입력할까요? >>> "))
# for i in range(numbers):
#     list_number = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     bin_li.append(list_number)
#     if list_number % 2 == 0:
#         even_li.append(list_number)
# print(f"입력 받은 숫자는 {bin_li}입니다.")
# print(f"입력 받은 숫자들 중 짝수는 {even_li}입니다.")

"""
딕셔너리 기반의 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름의 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름의 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름의 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.


숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)          # call2() 유형
print(add_numbers2(last_num))   # call4() 유형

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]

예를 들어 hello = ['안', '녕', '하', '세', '요']라는 list가 있다고 가정했을 때,
add_numbers3(10, hello)를 호출하면
[1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
라는 결과값을 만드는 함수를 정의한다면 어떻게 할 수 있을지 고민해보세요.
"""

# dict_list = {}
# nums = int(input("몇명 입력할래? >>> "))
# for i in range(nums):
#     name = input(f"{i+1}번째 사람의 이름을 입력하세요 >>> ")
#     phone_number = input(f"{i+1}번째 사람의 연락처를 입력하세요 >>> ")
#     dict_list[name] = phone_number
# print(f"입력 받은 연락처는 {dict_list}입니다.")

# last_num = int(input("숫자 몇 까지 입력하시겠습니까? >>> "))
# def add_numbers1(n):
#     numbers1 = []
#     for i in range(1, n + 1):
#         numbers1.append(i)
#     print(numbers1)
#
# def add_numbers2(n):
#     numbers2 = []
#     for i in range(1, n + 1):
#         numbers2.append(i)
#     return numbers2
#
# add_numbers1(last_num)
# print(add_numbers2(last_num))
#
# hello = ["안", "녕", "하", "세", "여"]
# def add_numbers3(n, a):
#     for i in range(n):
#         a.insert(i, i+1)
#     print(a)
#
# add_numbers3(10, hello)
#
# # 아오
# def add_numbers4(n, temp_list):
#     numbers4 = []
#     for i in range(n):
#         numbers4.append(i+1)
#     for letter in temp_list:
#         numbers4.append(letter)
#     print(numbers4)

"""
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개변수 : list인 numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
"""
print()
def count_even_odd(n):
    even = 0
    odd = 0
    for i in range(len(n)):
        if n[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"짝수의 개수 : {even}개")
    print(f"홀수의 개수 : {odd}개")

count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])