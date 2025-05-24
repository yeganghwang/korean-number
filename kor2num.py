def kor2num(kor_str):
    kor_num_map = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    kor_unit_map1 = ['', '십', '백', '천']
    kor_unit_map2 = ['', '만', '억', '조', '경', '해']

    kor_str = kor_str.replace(' ', '')
    total = 0
    section = 0
    num = 0
    i = 0
    length = len(kor_str)
    while i < length:
        char = kor_str[i]
        if char in kor_num_map:
            num = kor_num_map.index(char)
            i += 1
        elif char in kor_unit_map1:
            unit = 10 ** kor_unit_map1.index(char)
            if num == 0:
                num = 1
            section += num * unit
            num = 0
            i += 1
        elif char in kor_unit_map2:
            unit = 10 ** (4 * kor_unit_map2.index(char))
            if num == 0 and section == 0:
                section = 1
            section_total = section + num
            total += section_total * unit
            section = 0
            num = 0
            i += 1
        else:
            i += 1
    total += section + num
    return str(total)

def num2kor(num):
    kor_num_map = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    kor_unit_map1 = ['', '십', '백', '천']
    kor_unit_map2 = ['', '만', '억', '조', '경', '해']

    if num == 0:
        return kor_num_map[0]

    result = []
    num_str = str(num)[::-1]  # 뒤집어서 4자리씩 처리
    num_len = len(num_str)
    for i in range(0, num_len, 4):
        part = num_str[i:i+4][::-1]
        part_int = int(part)
        if part_int == 0:
            continue

        part_result = []
        for j, digit in enumerate(part[::-1]):
            n = int(digit)
            if n != 0:
                s = ''
                if not (n == 1 and j > 0):
                    s += kor_num_map[n]
                s += kor_unit_map1[j]
                part_result.insert(0, s)
        unit_idx = i // 4
        unit_str = kor_unit_map2[unit_idx]

        # 만 단위 특수 규칙 처리
        if unit_str == '만':
            # 10000~19999는 '만', 그 외에는 '일만', '이만' 등
            abs_part = int(num_str[::-1][max(0, num_len-4-unit_idx*4):num_len-unit_idx*4] or '0')
            if 10000 <= num % 100000 < 20000:
                # 10000~19999: '만'만 출력
                result.insert(0, unit_str)
                continue
            elif part_int == 1 and num_len <= 8:  # 100000000 미만에서 1만은 '만'
                result.insert(0, unit_str)
                continue
        # 억, 조, ... 단위는 항상 '일억', '일조' 등
        if part_int == 1 and unit_str and unit_str != '만':
            result.insert(0, '일' + unit_str)
        else:
            result.insert(0, ''.join(part_result) + unit_str)

    return ' '.join([r for r in result if r])

def test_kor_num():
    test_cases = [
        (0, '영'),
        (1, '일'),
        (9, '구'),
        (10, '십'),
        (11, '십일'),
        (20, '이십'),
        (21, '이십일'),
        (100, '백'),
        (101, '백일'),
        (110, '백십'),
        (111, '백십일'),
        (1000, '천'),
        (3500, '삼천오백'),
        (9999, '구천구백구십구'),
        (81651, '팔만 천육백오십일'), 
        (1062, '천육십이'),
        (1841, '천팔백사십일'),
        (2000, '이천'),
        (7154, '칠천백오십사'),
        (1001, '천일'),
        (1010, '천십'),
        (1100, '천백'),
        (1111, '천백십일'),
        (10000, '만'),
        (10001, '만 일'),
        (12345, '만 이천삼백사십오'),
        (100000, '십만'),
        (500000, '오십만'),
        (1000000, '백만'),
        (10000000, '천만'),
        (100000000, '일억'),
        (123456789, '일억 이천삼백사십오만 육천칠백팔십구'),
        (1000000000, '십억'),
        (1000000001, '십억 일'),
        (100200300, '일억 이십만 삼백'),
        (1000000000000, '일조'),
        (10000000000000000, '일경'),
        (100000000000000000000, '일해'),
        (1234567890123456789, '백이십삼경 사천오백육십칠조 팔천구백일억 이천삼백사십오만 육천칠백팔십구'),
    ]
    for num, kor in test_cases:
        assert num2kor(num).replace(' ', '') == kor.replace(' ', ''), f"num2kor({num}) => {num2kor(num)}, expected {kor}"
        assert kor2num(kor) == str(num), f"kor2num({kor}) => {kor2num(kor)}, expected {num}"
    print('All tests passed!')

if __name__ == "__main__":
    test_kor_num()