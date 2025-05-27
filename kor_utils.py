# 공통 상수 및 유틸 함수
KOR_NUM_MAP = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
KOR_UNIT_MAP1 = ['', '십', '백', '천']
KOR_UNIT_MAP2 = ['', '만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극', '항하사', '아승기', '나유타', '불가사의', '무량대수']

def split_by_4(num):
    num_str = str(num)[::-1]
    return [num_str[i:i+4][::-1] for i in range(0, len(num_str), 4)]
