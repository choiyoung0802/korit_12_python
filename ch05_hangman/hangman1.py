import random
# numbers = [1,2,3,4,5]
# chosen_number = random.choice(numbers)
# random 이라는 객체같은 것에 choice 라는 메서드가 있고 내부에 list 자료형을 넣으면 하나를 뽑아서 변수에 저장하나보네
# print(chosen_number)

word_list = ["apple", "banana", "camel"]
# todo - 1 : word_list 에서 하나의 단어를 임의로 선택하도록 random 모듈을 사용하고, 해당 단어를 chosen_word 변수에 담으시오.

# todo - 2 : 사용자에게 알파벳 하나를 추측해서 입력하라고 요청하고, 이를 guess 변수에 담으시오. 대문자로 시작하는 경우를 방지하기 위해 .lower()

# todo - 3 : guess 에서 입력한 문자 하나가 chosen_word 의 str 문자열 중에 하나의 문자와 일치하는지를 확인할 수 있도록 반복-조건문을 작성하고 맞으면 졍답 / 틀리면 오답이라고 출력
"""
예를 들어 단어가 apple 이고 p 라고 입력했다면
오답
정답
정답
오답
오답
"""
chosen_word = random.choice(word_list)
guess = input("단어를 추측해서 입력하세요 >>> ").lower()
for answer in chosen_word:
    if answer == guess:
        print("정답")
    else:
        print("오답")