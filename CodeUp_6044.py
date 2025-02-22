# 정수 2개를 입력받아 공백을 기준으로 분리 후 int형으로 변환
a, b = map(int, input().split())

# 합, 차, 곱 계산
sum_result = a + b
diff_result = a - b
prod_result = a * b

# 몫, 나머지 계산 (정수 연산)
quotient = a // b
remainder = a % b

# 나눈 값 계산 (실수 연산)
div_result = a / b

# 결과 출력
print(sum_result)                          # 합
print(diff_result)                         # 차
print(prod_result)                         # 곱
print(quotient)                            # 몫
print(remainder)                           # 나머지
print("{:.2f}".format(div_result))          # 나눈 값 (소수점 둘째 자리까지)