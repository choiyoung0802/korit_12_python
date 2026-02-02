import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")
display = []
for _ in range(len(chosen_word)):
    display.append("_")

# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6 으로 초기화하세요.

# todo - 2 : while 문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 조건을 작성하시오.
lives = 6
end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input("입력하세요 >>> ")
    for _ in range(len(chosen_word)):
        if guess == chosen_word[_]:
            display[_] = guess
        # else:
        #     lives -= 1
        #     print(stages[lives])
        #     print(f'기회가 {lives} 번 남았습니다.')
        #     if lives == 0:
        #         end_of_game = True
        # 라고 작성하면 문자 하나 당 일치 여부를 확인하기 때문에 예상했던 것과 다르게 맞추더라도 나머지 문자에 대해서 lives-=1이 누적적으로 적용됩니다. 그런데 각 element에 대한 반복 때문에 누적적으로 값이 빠진다면, 반복문 바깥에 따로 작성해주면 되겠네요.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} 단어는 없음. 남은 기회:{lives}")
        if lives == 0:
            end_of_game = True
            print("컷")
            print(stages[lives])
            print(f"정답은 {chosen_word} 입니다.")
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("정답입니다.")
print("게임 종료")


