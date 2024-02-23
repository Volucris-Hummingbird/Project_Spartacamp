#입력받기       판단하기
#비교하기       판단하기
#반복하기       재시작여부

import random
n = 1
b = random.randint(1,100)
c =  ""
x = 0
while c != "n" and c != "N":
    try:
        a = int(input("숫자를 입력하세요>>"))
        if a < 100 and a > 0:
            if a > b:
                print("down")
                n+=1
            elif a < b:
                print("up")
                n+=1
            else:
                print("정답입니다")
                print(f"정답까지 시행 횟수 :  {n}회")
                if x == 0:
                    x = n
                else:
                    if x > n:
                        x = n
                c = input("새로 시작하시겠습니까? (Y/N)>>")
                while c not in  ["n", "N", "y", "Y"]:
                    print("(Y/N)으로 입력해주세요")
                    c = input("새로 시작하시겠습니까? (Y/N)>>")
                if c == "y" or c == "Y":
                    print(f"이전 플레이어 최고 기록 : {x}회")
                    b = random.randint(1,100)
                    n = 1
                else:
                    print("수고하셨습니다. 다음에 또 오세요")
                    break
        else:
            print("1에서 100사이의 정수를 입력해주세요")
    except:
        print("1에서 100사이의 정수를 입력하세요")


        #if c == "y" or "Y":        왜 잘못됐는지 설명!!
        #while c != "n" and c != "N":       while c != "n" or c != "N":     과 비교!!! a와 b 합집합의 부정 => 