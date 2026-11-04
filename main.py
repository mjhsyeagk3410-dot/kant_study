# 가위 바위 보 게임 미니 프로젝트 

import random # 난수가 발생되는 모듈 임포트 

huma_score = 0
compu_score = 0

while True:
    print("=" * 30) #게임시작 문구 윗 장식
    print("가위 / 바위 / 보 게임") #게임시작할때
    print("=" * 30) #게임시작 문구 아랫 장식 

    print("1. 가위 / 2. 바위 / 3. 보")

    huma = int(input("번호를 선택하세요.: "))
 
    compu = random.randint(1, 3)
    rps_text = ["", "가위", "바위", "보"]
    
    huma_text = rps_text[huma]
    compu_text = rps_text[compu]

    if huma == compu:
     print("=> 무승부") 
    elif (huma == 1 and compu == 3) or (huma == 2 and compu == 1) or (huma == 3 and compu == 2):
        print("=> 승리")
        huma_score += 1
    else:
        print("=> 패배")
        compu_score += 1

    print("[게임 결과]")
    print(f"나: {huma_text} vs 컴퓨터: {compu_text}")
    print(f"현재 스코어 나 {huma_score} : {compu_score} 컴퓨터")

    game_continue = input("다시 도전 (yes/no): ")
    if game_continue== "no":
        break

    else:
        continue 