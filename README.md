# korean_number

한국어 숫자 ↔ 숫자 변환 및 금융 표기 지원 Python 유틸리티


## 설치 방법

아래 명령어로 설치할 수 있습니다:

```bash
pip install korean-number
```

주요 함수를 import 하여 사용합니다.
```python
from korean_number import kor2num, num2kor
```
---

## 주요 함수

### 1. kor2num(kor_str)
- **설명:**  한글로 표기된 숫자를 아라비아 숫자로 변환합니다. 입력값의 공백과 상관없이 변환합니다.
- **예시:**
  ```python
  kor2num('일억 이천삼백사십오만 육천칠백팔십구')  # 123456789
  kor2num('천백십일')  # 1111
  kor2num('영')  # 0
  ```

---

### 2. num2kor(num)
- **설명:**  숫자를 일반적인 한글 숫자 표기로 변환합니다. 만, 억, 조 등의 단위로 공백이 발생합니다.
- **예시:**
  ```python
  num2kor(123456789)  # '일억 이천삼백사십오만 육천칠백팔십구'
  num2kor(1111)       # '천백십일'
  num2kor(100000000)  # '일억'
  num2kor(0)          # '영'
  ```

---

### 3. num2finkor(num)
- **설명:**  숫자를 금융 표기법에 맞는 한글 숫자 표기로 변환합니다. (모든 자리의 1도 '일'로 표기, 예: '일천일백일십일')
- **예시:**
  ```python
  num2finkor(123456789)  # '일억이천삼백사십오만육천칠백팔십구'
  num2finkor(1111111111) # '일십억일천일백일십일만일천일백일십일'
  num2finkor(1111)       # '일천일백일십일'
  num2finkor(100000000)  # '일억'
  num2finkor(0)          # '영'
  ```

---

### 4. addunit(num)
- **설명:**  숫자를 4자리 단위(만, 억, 조 등)로 끊어서 각 단위별로 한글 단위와 함께 표기합니다.
- **예시:**
  ```python
  addunit(1234567890123456789)  # '123경 4567조 8901억 2345만 6789'
  addunit(10001)                # '1만 1'
  addunit(100000000)            # '1억'
  ```

---

## 예시 코드

```python
print(num2kor(123456789))      # '일억 이천삼백사십오만 육천칠백팔십구'
print(num2finkor(1111))        # '일천일백일십일'
print(kor2num('천백십일'))     # '1111'
print(addunit(12345678))       # '1234만 5678'
```

---


## 사용법 (import 예시)

설치 후 아래와 같이 import하여 사용할 수 있습니다:

```python
from korean_number import num2kor, num2finkor, kor2num, addunit

print(num2kor(123456789))      # '일억 이천삼백사십오만 육천칠백팔십구'
print(num2finkor(1111))        # '일천일백일십일'
print(kor2num('천백십일'))     # 1111
print(addunit(12345678))       # '1234만 5678'
```

---

## 라이선스

MIT License
