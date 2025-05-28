h, b, c, s = map(int, input().split())

# 전체 비트 수 계산
total_bits = h * b * c * s

# 비트를 바이트 → KB → MB로 변환
total_MB = total_bits / 8 / 1024 / 1024

# 소수점 첫째 자리까지 출력
print(f"{total_MB:.1f} MB")