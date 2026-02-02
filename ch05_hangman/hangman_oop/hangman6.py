import random
import hangman_arts
import hangman_word_list
# import 다음에 파일명을 썼다는 것에 주목해야합니다. 이 파일 하나를 파이썬에서는 module(모듈) 이라고 합니다.

# 외부의 hangman_word_list 에 있는 word_list 변수를 참조해서 chosen_word 를 만들 필요가 있습니다.
print(hangman_arts.logo)
# 위에가 힌트. 그러면 chosen_word 를 불러올 수 있도록 코드를 작성하시오.
chosen_word = random.choice(hangman_word_list.word_list)
print(f"테스트 단어 : {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display.append("_")
lives = 6
end_of_game = False
while not end_of_game:
    print(hangman_arts.stages[lives])
    guess = input("입력하세요 >>> ")
    for _ in range(len(chosen_word)):
        if guess == chosen_word[_]:
            display[_] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} 단어는 없음. 남은 기회:{lives}")
        if lives == 0:
            end_of_game = True
            print(hangman_arts.stages[lives])
            print("컷")
            print(f"정답은 {chosen_word} 입니다.")
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("정답입니다.")
print("게임 종료")