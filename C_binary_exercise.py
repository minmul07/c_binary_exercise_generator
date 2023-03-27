import random

# 비트 수 설정.
difficulty = 6  # 3 ~ 7까지의 숫자
#difficulty = random.randint(3, 7)

# 모드 설정.
mode = 2
# 1: 정답 즉시 출력
# 2: AND/OR/XOR 별로 퀴즈

num1 = random.getrandbits(difficulty)
num2 = random.getrandbits(difficulty)

if num2 > num1:
    num1, num2 = num2, num1
num2 = num2 << (difficulty - num1.bit_length())

num1_str = format(num1, "b").zfill(difficulty).rjust(7, "0")
num2_str = format(num2, "b").zfill(difficulty).rjust(7, "0")
num_and = num1 & num2
num_or = num1 | num2
num_xor = num1 ^ num2

print(f"num1: {num1_str}")
print(f"num2: {num2_str}")

if mode == 1: #즉시 출력
    print(f"{num1_str} & {num2_str}:   {format(num_and).zfill(difficulty).rjust(7, '0')}   AND")
    print(f"{num1_str} | {num2_str}:   {format(num_or).zfill(difficulty).rjust(7, '0')}   OR")
    print(f"{num1_str} ^ {num2_str}:   {format(num_xor).zfill(difficulty).rjust(7, '0')}   XOR")
    
else: #퀴즈
    userInput = input(f"{num1_str} & {num2_str}: (7자리로 입력) ")
    if userInput == format(num_and, "b").zfill(difficulty).rjust(7, "0"):
        print("정답입니다! \n")
    else:
        print("틀렸습니다!")
        print(f"정답 - {num1_str} & {num2_str}: {format(num_and, 'b').zfill(difficulty).rjust(7, '0')}\n")

    userInput = input(f"{num1_str} | {num2_str}: (7자리로 입력) ")
    if userInput == format(num_or, "b").zfill(difficulty).rjust(7, "0"):
        print("정답입니다! \n")
    else:
        print("틀렸습니다!")
        print(f"정답 - {num1_str} | {num2_str}: {format(num_or, 'b').zfill(difficulty).rjust(7, '0')}\n")

    userInput = input(f"{num1_str} ^ {num2_str}: (7자리로 입력) ")
    if userInput == format(num_xor, "b").zfill(difficulty).rjust(7, "0"):
        print("정답입니다! \n")
    else:
        print("틀렸습니다!")
        print(f"정답 - {num1_str} ^ {num2_str}: {format(num_xor, 'b').zfill(difficulty).rjust(7, '0')}\n")
        
#https://github.com/minmul07/c_binary_exercise_generator