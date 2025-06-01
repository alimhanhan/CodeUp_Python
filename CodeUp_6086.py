# 입력 받기
w, h, b = map(int, input().split())

# 총 비트 수 계산
total_bits = w * h * b

# 비트를 바이트로 → 바이트를 킬로바이트로 → 킬로바이트를 메가바이트로
# 8비트 = 1바이트, 1024바이트 = 1KB, 1024KB = 1MB
total_MB = total_bits / 8 / 1024 / 1024

# 소수점 둘째 자리까지 반올림
print(f"{total_MB:.2f} MB")