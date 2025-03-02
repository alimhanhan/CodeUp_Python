a, b, c = map(int, input().split())  # 정수 3개 입력받아 정수형 변환
sum_value = a + b + c  # 합 계산
avg_value = sum_value / 3  # 평균 계산

print(sum_value, f"{avg_value:.2f}")  # 합과 평균(소수 둘째 자리까지) 출력