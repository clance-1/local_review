# 주어진 길이의 랜덤한 비밀번호를 생성하는 함수
def generate_password(length):
    if not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")
    import secrets
    # 혼동되는 문자들을 제외(O, 0, o, l, I, 1, S, 5, Z, 2, B, 8, G, 6, |)
    exclude = {'O', '0', 'o', 'l', 'I', '1', 'S', '5', 'Z', '2', 'B', '8', 'G', '6', '|'}
    characters = ''.join(chr(i) for i in range(32, 127) if chr(i) not in exclude)
    if not characters:
        raise ValueError("no available characters to generate password")
    return ''.join(secrets.choice(characters) for _ in range(length))
