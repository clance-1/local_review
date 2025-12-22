# 주어진 길이의 랜덤한 비밀번호를 생성하는 함수
def generate_password(length):
    if not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")
    import secrets
    import string
    characters = ''.join(
        ch for ch in (string.ascii_letters + string.digits + string.punctuation)
    )

    return ''.join(secrets.choice(characters) for _ in range(length))
