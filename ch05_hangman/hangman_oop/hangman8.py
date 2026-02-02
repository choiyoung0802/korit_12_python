# play_hangman 이라는 함수를 call1() 유형으로 정의하고, 호출하시오.
def play_hangman():
    import random
    from hangman_arts import logo, stages
    from hangman_word_list import word_list
    print(logo)
    chosen_word = random.choice(word_list)
    print(f"테스트 단어 : {chosen_word}")
    display = []
    for _ in range(len(chosen_word)):
        display.append("_")
    lives = 6
    end_of_game = False
    while not end_of_game:
        print(stages[lives])
        guess = input("입력하세요 >>> ")
        for _ in range(len(chosen_word)):
            if guess == chosen_word[_]:
                display[_] = guess
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} 단어는 없음. 남은 기회:{lives}")
            if lives == 0:
                end_of_game = True
                print(stages[lives])
                print("컷")
                print(f"정답은 {chosen_word} 입니다.")
        print(" ".join(display))
        if "_" not in display:
            end_of_game = True
            print("정답입니다.")
    print("게임 종료")

play_hangman()