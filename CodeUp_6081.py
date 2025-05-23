hex_input = input()  # 입력 예: B
n = int(hex_input, 16)  # 16진수를 10진수 정수로 변환

for i in range(1, 16):  # 1부터 15(F는 16진수로 15)
    print('%X*%X=%X' % (n, i, n * i))