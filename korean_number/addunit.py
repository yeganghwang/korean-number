from .kor_utils import *

def addunit(num):
    parts = split_by_4(num)
    result = []
    for i, part in enumerate(parts):
        if int(part) == 0:
            continue
        unit_str = KOR_UNIT_MAP2[i]
        result.insert(0, str(int(part)) + unit_str)
    return ' '.join(result)
