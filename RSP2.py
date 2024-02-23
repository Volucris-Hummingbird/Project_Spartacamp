import random

RSP = ['가위', '바위', '보']

def RSP_game():
    play_time = float('inf')
    play_again = True
    
    while play_again:
        print("게임을 시작합니다.")
        computer_choice = random.choice(RSP)
        # 게임의 수
        playno = 0
        
        # 승패 세기
        win = 0
        lose = 0
        draw = 0
        
        while True:
            try: 
                answer = input("가위, 바위, 보 중 하나를 입력하세요 : ")
                if answer not in RSP :
                    print ("가위, 바위, 보 중 하나만 입력해주세요.")
                    continue
            
                playno += 1
            
                if (answer == '가위' and computer_choice == '보') or (answer == '바위' and computer_choice == '가위') or (answer == '보' and computer_choice == '주먹'):
                    print ("win")
                    win += 1
                elif (answer == computer_choice):
                    print("draw")
                    draw += 1
                else:
                    print("lose")
                    lose += 1
                
                # 다시 도전 여부 확인
                play_again = input("다시 도전하시겠습니까? (yes/no) : ").lower()
                if play_again != 'yes':
                    print("게임을 종료합니다.")
                    break
            
            except ValueError:
                print("가위, 바위, 보 중 하나만 입력해주세요.")
                continue
    
    # 게임 종료 후 승, 패, 무승부 출력
    print(f"최고 기록: {playno}번")
    print(f"승 : {win}, 패 : {lose}, 무승부 : {draw}")

# 게임 실행
RSP_game()
