import random


def guess_number ():
    random_number = random.randint(1, 100)
    print(random_number)
    count = 0
    while True:
        number = int(input("1에서 100 사이의 숫자를 입력하세요: "))
        if number > 100 or number == 0:
            print("유효한 숫자를 입력하세요.")
        elif number > random_number:
            print("DOWN")
            count += 1
        elif number < random_number:
            print("UP")
            count += 1
        else:
            print("정답입니다!")
            count += 1
            break


    print(f"시도한 횟수: {count}번")

guess_number()

while True:
    user_input = input("게임을 다시 하시겠습니까? y/n")
    if user_input == 'y':
        guess_number()
    elif user_input == 'n':
        print("게임을 종료합니다.")
        break
    else:
        print("y 또는 n로 대답해 주십시오.")