import secrets
import string

# AMBIGUOUS_CHARACTERS: 비밀번호 생성 시 제외할 문자들의 집합
#
# 서로 헷갈리기 쉬운 문자들(O, 0, o, l, I, 1, S, 5, Z, 2, B, 8, G, 6, |)은
# 가독성을 위해 비밀번호에서 제외합니다.
#
# 이 집합에는 시각적으로 혼동되기 쉬운 문자들이 포함되어 있습니다:
#   - 대문자 O와 숫자 0
#   - 소문자 l과 숫자 1
#   - 대문자 I와 숫자 1
#   - 기타 혼동 가능한 문자: S/5, Z/2, B/8, G/6, |
#
# 이러한 문자들을 제외하면 비밀번호의 가독성이 향상되고 입력 오류가 줄어듭니다.
AMBIGUOUS_CHARACTERS = set("O0olI1S5Z2B8G6|")

# CHARACTERS: 비밀번호 생성에 사용되는 최종 문자 집합
#
# 영문 대소문자, 숫자, 특수문자를 포함하되 AMBIGUOUS_CHARACTERS에 포함된
# 문자는 제외합니다. 이 문자열은 generate_password() 함수에서 무작위
# 비밀번호를 생성할 때 사용됩니다.
#
# 구성: string.ascii_letters + string.digits + string.punctuation에서
#       혼동되는 문자를 제거한 결과입니다.
CHARACTERS = ''.join(
    ch for ch in (string.ascii_letters + string.digits + string.punctuation)
    if ch not in AMBIGUOUS_CHARACTERS
)

# 주어진 길이의 랜덤한 비밀번호를 생성하는 함수
def generate_password(length):
    """주어진 길이의 무작위 비밀번호를 생성합니다.

    Args:
        length (int): 생성할 비밀번호 길이. 0 이상의 정수여야 합니다.

    Returns:
        str: 지정한 길이의 랜덤 비밀번호.

    Raises:
        TypeError: length가 int가 아닌 경우.
        ValueError: length가 음수인 경우.
    """
    if not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")

    return ''.join(secrets.choice(CHARACTERS) for _ in range(length))
