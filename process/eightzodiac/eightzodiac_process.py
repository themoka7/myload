import itertools
import os
from pathlib import Path
import json

from process.common.eightchar import get_eightchar


# 데이터에 십성 추가 함수
current_dir = os.path.dirname(os.path.abspath(__file__))

Heavenly_Five_Elements = {
    '갑': '목=木,양=陽', '을': '목=木,음=陰', '병':'화=火,양=陽', '정': '화=火,음=陰',
    '무': '토=土,양=陽', '기': '토=土,음=陰', '경': '금=金,양=陽', '신': '금=金,음=陰',
    '임': '수=水,양=陽', '계': '수=水,음=陰'
}

Earthly_Five_Elements = {
    '자': '수=水,음=陰', '축': '토=土,음=陰',
    '인': '목=木,양=陽', '묘': '목=木,음=陰', '진': '토=土,양=陽',
    '사': '화=火,양=陽', '오': '화=火,음=陰', '미': '토=土,음=陰',
    '신': '금=金,양=陽', '유': '금=金,음=陰', '술': '토=土,양=陽',
    '해': '수=水,양=陽'
}



def add_ten_gods(eightchar_data, day_heavenly):


    print(1)
    ten_gods1 = json.loads(Path(current_dir,'json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods1']
    #print(ten_gods1)
    print(2)
    ten_gods2 = json.loads(Path(current_dir,'json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods2']
    result = {}
    for key, value in eightchar_data.items():
        if "KorHeavenly" in key  and key != 'KorHeavenlyDayText':
            result[key + 'TenGod'] = ten_gods1.get(day_heavenly, {}).get(value, '알 수 없음')
        if "KorEarthly" in key:
            result[key + 'TenGod'] = ten_gods2.get(day_heavenly, {}).get(value, '알 수 없음')
    return result

# 메인 함수 정의
def get_eightzodiac_data(data):
    # 사주 정보 추출
    eightchar = get_eightchar(data['calendar'], data['year'], data['month'], data['day'], data['time'])
    print("추출된 사주 정보:", eightchar)

    # 오행과 음양 추가
    eightchar.update({'HeavenlyYearElement': Heavenly_Five_Elements.get(eightchar['KorHeavenlyYearText'], "")})
    eightchar.update({'HeavenlyMonthElement': Heavenly_Five_Elements.get(eightchar['KorHeavenlyMonthText'], "")})
    eightchar.update({'HeavenlyDayElement': Heavenly_Five_Elements.get(eightchar['KorHeavenlyDayText'], "")})
    eightchar.update({'HeavenlyTimeElement': Heavenly_Five_Elements.get(eightchar['KorHeavenlyTimeText'], "")})

    eightchar.update({'EarthlyYearElement': Earthly_Five_Elements.get(eightchar['KorEarthlyYearText'], "")})
    eightchar.update({'EarthlyMonthElement': Earthly_Five_Elements.get(eightchar['KorEarthlyMonthText'], "")})
    eightchar.update({'EarthlyDayElement': Earthly_Five_Elements.get(eightchar['KorEarthlyDayText'], "")})
    eightchar.update({'EarthlyTimeElement': Earthly_Five_Elements.get(eightchar['KorEarthlyTimeText'], "")})
    # 오행과 음양 추가

    #print(is_strong_day_master(eightchar))


    # 일간으로 십성 추가
    day_heavenly = eightchar['KorHeavenlyDayText']
    ten_gods_data = add_ten_gods(eightchar, day_heavenly)
    eightchar.update(ten_gods_data)
    eightchar.update({'KorHeavenlyDayTextTenGod':'나'})

    print("십성 추가된 사주 정보:", eightchar)

    print(eightchar['KorHeavenlyTimeText'])
    print(eightchar['KorHeavenlyDayText'])
    print(eightchar['KorHeavenlyMonthText'])
    print(eightchar['KorHeavenlyYearText'])

    print(eightchar['KorEarthlyTimeText'])
    print(eightchar['KorEarthlyDayText'])
    print(eightchar['KorEarthlyMonthText'])
    print(eightchar['KorEarthlyYearText'])
    
    
    #천간합 추출
    Heavenly_list = [eightchar['KorHeavenlyTimeText'],eightchar['KorHeavenlyDayText'],eightchar['KorHeavenlyMonthText'],eightchar['KorHeavenlyYearText']]
    #Heavenly_list = ['갑', '기', '무', '계']

    #가능한 조합

    print('1')
    KorHeavenlySum = json.loads(Path(current_dir, 'json/plus.json').read_text(encoding='utf-8'))['KorHeavenlySum']
    print('2')
    using_Heavenly_list = ["".join(pair) for pair in itertools.permutations(Heavenly_list, 2)]
    KorHeavenlySumResult = {pair: KorHeavenlySum[pair] for pair in using_Heavenly_list if pair in KorHeavenlySum}

    print('---천간합---')
    print(KorHeavenlySumResult)

    eightchar.update({'KorHeavenlySumResult': KorHeavenlySumResult})

    # 지지합 추출
    Earthly_list = [eightchar['KorEarthlyTimeText'], eightchar['KorEarthlyDayText'],eightchar['KorEarthlyMonthText'], eightchar['KorEarthlyYearText']]
    #2글자 조합
    KorEarthlySum = json.loads(Path(current_dir,'json/plus.json').read_text(encoding='utf-8'))['KorEarthlySum']

    usingEarthlylistFor2 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 2)]
    KorEarthlySumResultFor2 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistFor2 if pair in KorEarthlySum}

    usingEarthlylistfor3 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 3)]
    KorEarthlySumResultFor3 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistfor3 if pair in KorEarthlySum}



    EarthlyMergedResult = {**KorEarthlySumResultFor2, **KorEarthlySumResultFor3}
    print('---지지합---')
    print(EarthlyMergedResult)
    eightchar.update({'KorEarthlySumResult': EarthlyMergedResult})



    # 살추출

    eight_list = [ eightchar['KorHeavenlyDayText'],

                      eightchar['KorEarthlyTimeText'], eightchar['KorEarthlyDayText'],
                      eightchar['KorEarthlyMonthText'], eightchar['KorEarthlyYearText']
                  ]
    kill_data = json.loads(Path(current_dir,'json/kill.json').read_text(encoding='utf-8'))

    using_eight_list = ["".join(pair) for pair in itertools.permutations(eight_list, 2)]
    kill_data_result = {pair: kill_data[pair] for pair in using_eight_list if pair in kill_data}

    eightchar.update({'kill_data_result' : kill_data_result})
    print('---살---')


    #처음 입력값 추가
    eightchar.update(data)



    #신약/추출
    eightchar.update({'strength' : evaluate_strength(
                    determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0], eightchar['EarthlyMonthElement'].split(',')[0].split('=')[0]),
                    determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],eightchar['EarthlyDayElement'].split(',')[0].split('=')[0]),
                    determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],eightchar['EarthlyYearElement'].split(',')[0].split('=')[0]),
                    determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],eightchar['EarthlyTimeElement'].split(',')[0].split('=')[0]))})



    #일간으로 보는 성격,특징
    dailyTextData = json.loads(Path(current_dir, 'json/dailyText.json').read_text(encoding='utf-8'))

    eightchar.update({'daily_text' : dailyTextData[eightchar['KorHeavenlyDayText']+eightchar['KorEarthlyDayText']]});
    


    #대운정하기
    print(eightchar)
    direction = 'forward'

    if(eightchar['gender'] == '남자' and eightchar['HeavenlyYearElement'].split(',')[1].split('=')[0] == '음' ):
        direction = 'back'
    if (eightchar['gender'] == '여자' and eightchar['HeavenlyYearElement'].split(',')[1].split('=')[0] == '양'):
        direction = 'back'

    heavenly_idx = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
    earthly_idx = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

    # 현재 천간의 인덱스 찾기
    current_heavenly_index = heavenly_idx.index(eightchar['KorHeavenlyMonthText'])

    # 다음 천간 인덱스 계산
    if direction == 'forward':
        next_heavenly_index = (current_heavenly_index + 1) % len(heavenly_idx)  # 순환하여 처음으로 돌아감
    else:
        next_heavenly_index = (current_heavenly_index - 1) % len(heavenly_idx)  # 순환하여 마지막으로 돌아감

    # 다음 천간 값 가져오기
    next_heavenly = heavenly_idx[next_heavenly_index]

    print(eightchar['KorHeavenlyMonthText'])
    print(next_heavenly)

    # 현재 지지의 인덱스 찾기
    current_earthly_index = earthly_idx.index(eightchar['KorEarthlyMonthText'])

    # 다음 지지 인덱스 계산
    if direction == 'forward':
        next_earthly_index = (current_earthly_index + 1) % len(earthly_idx)  # 순환하여 처음으로 돌아감
    else:
        next_earthly_index = (current_earthly_index - 1) % len(earthly_idx)  # 순환하여 마지막으로 돌아감

    # 다음 지지 값 가져오기
    next_earthly = earthly_idx[next_earthly_index]


    print(eightchar['KorEarthlyMonthText'])
    print(next_earthly)

    print(direction)

    return eightchar


# 오행 상생/상극 관계 설정
element_relationships = {
    "목": {"생": "화", "극": "토"},
    "화": {"생": "토", "극": "금"},
    "토": {"생": "금", "극": "수"},
    "금": {"생": "수", "극": "목"},
    "수": {"생": "목", "극": "화"}
}

def determine_support(day_element, branch_element):
    # 일간과 지지가 같은 오행이거나, 일간을 생해주는 오행일 경우 지원함
    if branch_element == day_element:
        return True
    elif element_relationships[day_element]["생"] == branch_element:
        return True
    else:
        return False

# 신강 신약 판단 함수 (이전 코드)
def evaluate_strength(month_branch, day_branch, year_branch, hour_branch):
    month_status = "O" if month_branch else "X"
    day_status = "O" if day_branch else "X"
    year_status = "O" if year_branch else "X"
    hour_status = "O" if hour_branch else "X"

    # 최강 조건 - 월지와 일지에서 힘을 얻고, 년지나 시지에서도 힘을 얻음
    if month_branch and day_branch and (year_branch or hour_branch):
        return f"최강|월지와 일지에서 힘을 얻고, 년지나 시지에서도 도움을 받음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 중강 조건 - 월지와 일지에서 힘을 얻고, 년지와 시지에서는 힘을 얻지 못함
    elif month_branch and day_branch:
        return f"중강|월지와 일지에서 힘을 얻고, 년지와 시지에서 추가적인 도움을 받지 못함|시지={hour_status},일지={day_status}, 월지={month_status},년지={year_status}"

    # 강 조건 - 월지에서 힘을 얻고, 년지 또는 시지에서도 도움을 받음
    elif month_branch and (year_branch or hour_branch):
        return f"강|월지에서 힘을 얻고, 년지 또는 시지에서 추가적인 힘을 받음|시지={hour_status}, 일지={day_status},월지={month_status},년지={year_status}"

    # 최약 조건 - 월지와 일지 모두에서 힘을 얻지 못하고, 년지와 시지에서도 도움을 받지 못함
    elif not month_branch and not day_branch and not (year_branch or hour_branch):
        return f"최약|월지와 일지 모두에서 힘을 얻지 못하며, 년지와 시지에서도 지원이 없음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 중약 조건 - 월지에서는 힘을 얻지 못하지만, 일지 또는 년지/시지에서 부분적인 도움을 받음
    elif not month_branch and (day_branch or year_branch or hour_branch):
        return f"중약|월지에서 힘을 얻지 못하지만, 일지 또는 년지/시지에서 일부 도움을 받음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 약 조건 - 월지에서 힘을 얻으나, 일지, 년지, 시지에서 추가적인 도움을 받지 못함
    elif month_branch and not (day_branch or year_branch or hour_branch):
        return f"약|월지에서만 힘을 얻고, 다른 지지에서는 도움을 받지 못함|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 기타 경우
    else:
        return f"없음|조건에 맞지 않는 경우|시지={hour_status},일지={day_status},월지={month_status},년지={year_status})"

# 예시 데이터
# 환희
#data = {'gender': '남자', 'calendar': '양력', 'year': '2016', 'month': '8', 'day': '30', 'time': '16'}

# 정목
data = {'gender': '남자', 'calendar': '양력', 'year': '1981', 'month': '3', 'day': '28', 'time': '06'}


# 함수 호출
get_eightzodiac_data(data)
