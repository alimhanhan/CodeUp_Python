# 두 정수 입력
a, b = input().split()
a = int(a)  # 변수 a에 저장되어 있는 값을 정수로 변환
b = int(b)  # 변수 b에 저장되어 있는 값을 정수로 변환

# 3항 연산자를 사용하여 큰 값을 선택
c = (a if (a >= b) else b)

# 결과를 출력
print(c)