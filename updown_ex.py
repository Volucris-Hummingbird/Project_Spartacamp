import random

def updown_game():
    best_score = float('inf')  # 플레이어의 최고 시도 횟수를 기록
    play_again = True  # 게임을 반복하기 위한 변수

    while play_again:
        print("새로운 게임을 시작합니다.")
        target_number = random.randint(1, 100)
        attempts = 0
        
        while True:
            try:
                guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
                if guess < 1 or guess > 100:
                    print("입력한 숫자가 범위를 벗어났50습니다. 1부터 100 사이의 숫자를 입력하세요.")
                    continue
                
                attempts += 1

                if guess < target_number:
                    print("업!")
                elif guess > target_number:
                    print("다운!")
                else:
                    print(f"정답입니다! {attempts}번 시도했습니다.")
                    if attempts < best_score:
                        best_score = attempts
                    break
            except ValueError:
                print("올바른 숫자를 입력하세요.")
        
        play_again_input = input("게임을 다시 하시겠습니까? (yes/no): ")
        play_again = play_again_input.lower() == 'yes'
    
    print(f"최고 기록: {best_score}번")

# 게임 실행
updown_game()
