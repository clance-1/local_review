import secrets
import string

# 서로 헷갈리기 쉬운 문자들(O, 0, o, l, I, 1, S, 5, Z, 2, B, 8, G, 6, |)은 가독성을 위해 비밀번호에서 제외한다.
AMBIGUOUS_CHARACTERS = set("O0olI1S5Z2B8G6|")
PASSWORD_CHARACTERS = ''.join(
    ch for ch in (string.ascii_letters + string.digits + string.punctuation)
    if ch not in AMBIGUOUS_CHARACTERS
)

# 주어진 길이의 랜덤한 비밀번호를 생성하는 함수
def generate_password(length):
    """주어진 길이의 무작위 비밀번호를 생성합니다.

    Args:
        length (int): 생성할 비밀번호 길이. 0 이상의 정수여야 합니다.

    Returns:
        str: 지정한 길이의 랜덤 비밀번호. length가 0인 경우 빈 문자열('')을 반환합니다.

    Raises:
        TypeError: length가 int가 아닌 경우.
        ValueError: length가 음수인 경우.
    """
    if not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")

    return ''.join(secrets.choice(PASSWORD_CHARACTERS) for _ in range(length))
