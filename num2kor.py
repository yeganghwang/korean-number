from kor_utils import *

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
