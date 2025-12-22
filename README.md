# local_review

## `generate_password(length)`

`generate_password(length)` 함수는 지정한 길이의 안전한 임의 비밀번호를 생성합니다. 영문 대/소문자, 숫자, 특수문자를 조합하여 생성하며, 혼동을 줄이기 위해 다음 문자들을 제외합니다:

- 대문자 `O` (오)과 숫자 `0` (영)
- 소문자 `l` (엘)과 숫자 `1` (일)
- 대문자 `I` (아이)

함수는 간단히 호출하여 사용할 수 있습니다. 예시:

```python
from password import generate_password

pw = generate_password(12)
print(pw)  # 예: 'aB3$e7G!k9Rt'
```

함수 구현은 `password.py`에 있습니다. 필요하면 생성 규칙(허용 문자 세트나 제외 문자)을 변경하여 사용할 수 있습니다.

---
_참고:_ 읽기 쉽고 혼동을 줄이기 위해 위에 명시한 혼동 가능한 문자들을 기본적으로 제외합니다.
