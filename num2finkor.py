from kor_utils import *

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
