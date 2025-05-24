# 공통 상수
KOR_NUM_MAP = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
KOR_UNIT_MAP1 = ['', '십', '백', '천']
KOR_UNIT_MAP2 = ['', '만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극', '항하사', '아승기', '나유타', '불가사의', '무량대수']

# 공통 유틸: 4자리씩 분할
def split_by_4(num):
    num_str = str(num)[::-1]
    return [num_str[i:i+4][::-1] for i in range(0, len(num_str), 4)]

# 한글 → 숫자
def kor2num(kor_str):
    kor_str = kor_str.replace(' ', '')
    total = 0
    section = 0
    num = 0
    i = 0
    length = len(kor_str)
    # 큰 단위부터 내려가면서 매칭
    unit_candidates = sorted(KOR_UNIT_MAP2, key=lambda x: -len(x))
    while i < length:
        char = kor_str[i]
        if char in KOR_NUM_MAP:
            num = KOR_NUM_MAP.index(char)
            i += 1
        elif char in KOR_UNIT_MAP1:
            unit = 10 ** KOR_UNIT_MAP1.index(char)
            if num == 0:
                num = 1
            section += num * unit
            num = 0
            i += 1
        else:
            matched = False
            for unit_str in unit_candidates:
                if unit_str and kor_str.startswith(unit_str, i):
                    unit = 10 ** (4 * KOR_UNIT_MAP2.index(unit_str))
                    if num == 0 and section == 0:
                        section = 1
                    section_total = section + num
                    total += section_total * unit
                    section = 0
                    num = 0
                    i += len(unit_str)
                    matched = True
                    break
            if not matched:
                i += 1
    total += section + num
    return total

# 숫자 → 한글(일반)
def num2kor(num):
    if num == 0:
        return KOR_NUM_MAP[0]
    result = []
    parts = split_by_4(num)
    for i, part in enumerate(parts):
        part_int = int(part)
        if part_int == 0:
            continue
        part_result = []
        for j, digit in enumerate(part[::-1]):
            n = int(digit)
            if n != 0:
                s = ''
                if not (n == 1 and j > 0):
                    s += KOR_NUM_MAP[n]
                s += KOR_UNIT_MAP1[j]
                part_result.insert(0, s)
        unit_str = KOR_UNIT_MAP2[i]
        if part_int == 1 and unit_str and unit_str != '만':
            result.insert(0, '일' + unit_str)
        else:
            result.insert(0, ''.join(part_result) + unit_str)
    return ' '.join([r for r in result if r])

# 숫자 → 한글(금융)
def num2finkor(num):
    if num == 0:
        return KOR_NUM_MAP[0]
    result = []
    parts = split_by_4(num)
    for i, part in enumerate(parts):
        part_int = int(part)
        if part_int == 0:
            continue
        part_result = []
        for j, digit in enumerate(part[::-1]):
            n = int(digit)
            if n != 0:
                s = KOR_NUM_MAP[n] + KOR_UNIT_MAP1[j]
                part_result.insert(0, s)
        unit_str = KOR_UNIT_MAP2[i]
        if part_result:
            result.insert(0, ''.join(part_result) + unit_str)
    return ''.join(result)

# 숫자 → 4자리 단위별 한글+숫자
def addunit(num):
    parts = split_by_4(num)
    result = []
    for i, part in enumerate(parts):
        if int(part) == 0:
            continue
        unit_str = KOR_UNIT_MAP2[i]
        result.insert(0, str(int(part)) + unit_str)
    return ' '.join(result)
