from kor_constants import *

def split_by_4(num):
    num_str = str(num)[::-1]
    return [num_str[i:i+4][::-1] for i in range(0, len(num_str), 4)]
