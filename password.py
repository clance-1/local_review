# 주어진 길이의 랜덤한 비밀번호를 생성하는 함수
def generate_password(length):
    import random
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))
