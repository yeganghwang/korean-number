from .kor_utils import *

def kor2num(kor_str):
    kor_str = kor_str.replace(' ', '')
    total = 0
    section = 0
    num = 0
    i = 0
    length = len(kor_str)
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
