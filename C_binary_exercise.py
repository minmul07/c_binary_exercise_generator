import random

#비트 수 설정.
difficulty = 4 # 3 ~ 7까지의 숫자

num1 = random.getrandbits(difficulty)
num2 = random.getrandbits(difficulty)

if num2 > num1:
    num1, num2 = num2, num1
num2 = num2 << (difficulty - num1.bit_length())

num1_str = format(num1, 'b').zfill(difficulty).rjust(7, '0')
num2_str = format(num2, 'b').zfill(difficulty).rjust(7, '0')
num_and = num1 & num2
num_or = num1 | num2
num_xor = num1 ^ num2

print(f"num1: {num1_str}")
print(f"num2: {num2_str}")
print(f"AND:  {format(num_and, 'b').zfill(difficulty).rjust(7, '0')}")
print(f"OR:   {format(num_or, 'b').zfill(difficulty).rjust(7, '0')}")
print(f"XOR:  {format(num_xor, 'b').zfill(difficulty).rjust(7, '0')}")

#