import random

def play_again():
    answer = input("다시 하시겠습니까? (y/n): ")
    return answer.lower() == 'y'

def record_result(result, records):
    if result == 'win':
        records['win'] += 1
    elif result == 'lose':
        records['lose'] += 1
    else:
        records['draw'] += 1

def print_records(records):
    print(f"승: {records['win']} 패: {records['lose']} 무승부: {records['draw']}")

def RSP_game():
    RSP = ['가위', '바위', '보']
    records = {'win': 0, 'lose': 0, 'draw': 0}
    
    while True:
        print("게임을 시작합니다.")
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if player_choice not in RSP:
            print("유효한 입력이 아닙니다.")
            continue
        
        computer_choice = random.choice(RSP)
        print(f"사용자: {player_choice}, 컴퓨터: {computer_choice}")
        
        if player_choice == computer_choice:
            print("무승부입니다!")
            record_result('draw', records)
        elif (player_choice == '가위' and computer_choice == '보') or \
             (player_choice == '바위' and computer_choice == '가위') or \
             (player_choice == '보' and computer_choice == '바위'):
            print("사용자 승리!")
            record_result('win', records)
        else:
            print("컴퓨터 승리!")
            record_result('lose', records)
        
        print_records(records)
        
        if not play_again():
            print("게임을 종료합니다.")
            break

# 게임 실행
RSP_game()
