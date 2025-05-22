# 예시입력 : '일억 이천삼백사십오만 육천칠백팔십구'
# 예시출력 : '123456789'

def kor2number(kor_str):
    
    total = 0
    num = 0
    tmp = 0
    
    kor_num_map = {
        '영': 0,
        '일': 1,
        '이': 2,
        '삼': 3,
        '사': 4,
        '오': 5,
        '육': 6,
        '륙': 6,
        '칠': 7,
        '팔': 8,
        '구': 9
    }
    
    kor_unit_map = {
        '십': 10,
        '백': 100,
        '천': 1000,
        '만': 10000,
        '억': 100000000,
        '조': 1000000000000,
        '경': 10000000000000000,
        '해': 100000000000000000000
    }
    
    kor_str = kor_str.replace(' ', '')

    i = 0
    section_total = 0
    while i < len(kor_str):
        char = kor_str[i]
        if char in kor_num_map:
            num = kor_num_map[char]
            i += 1
        elif char in kor_unit_map:
            unit = kor_unit_map[char]
            if unit >= 10000:
                if num == 0 and tmp == 0:
                    section_total = 1
                else:
                    section_total = tmp + num
                total += section_total * unit
                tmp = 0
                num = 0
                section_total = 0
            else:
                if num == 0:
                    num = 1
                tmp += num * unit
                num = 0
            i += 1
        else:
            i += 1

    total += tmp + num
    return str(total)
