import itertools
import os
from pathlib import Path
import json

from process.common.eightchar import get_eightchar
from process.eightzodiac.solar_term_process import get_solar_term

# 데이터에 십성 추가 함수
current_dir = os.path.dirname(os.path.abspath(__file__))

Heavenly_Five_Elements = {
    '갑': '목=木,양=陽,갑=甲', '을': '목=木,음=陰,을=乙', '병': '화=火,양=陽,병=丙', '정': '화=火,음=陰,정=丁',
    '무': '토=土,양=陽,무=戊', '기': '토=土,음=陰,기=己', '경': '금=金,양=陽,경=庚', '신': '금=金,음=陰,신=辛',
    '임': '수=水,양=陽,임=壬', '계': '수=水,음=陰,계=癸'
}

Earthly_Five_Elements = {
    '자': '수=水,음=陰,자=子', '축': '토=土,음=陰,축=丑',
    '인': '목=木,양=陽,인=寅', '묘': '목=木,음=陰,묘=卯', '진': '토=土,양=陽,진=辰',
    '사': '화=火,양=陽,사=巳', '오': '화=火,음=陰,오=午', '미': '토=土,음=陰,미=未',
    '신': '금=金,양=陽,신=申', '유': '금=金,음=陰,유=酉', '술': '토=土,양=陽,술=戌',
    '해': '수=水,양=陽,해=亥'
}

EarthlyHeaven_Elements = {
    '인': '무=戊,병=丙,갑=甲', '묘': '갑=甲,　=　,을=乙', '진': '을=乙,경=庚,무=戊',
    '사': '무=戊,경=庚,병=丙', '오': '병=丙,기=己,정=丁', '미': '정=丁,을=乙,기=己',
    '신': '무=戊,임=壬,경=庚', '유': '경=庚,　=　,신=辛', '술': '신=辛,정=丁,무=戊',
    '해': '무=戊,갑=甲,임=壬', '자': '임=壬,　=　,계=癸', '축': '계=癸,신=辛,기=己'

}


def add_ten_gods(eightchar_data, day_heavenly):
    #print(1)
    ten_gods1 = json.loads(Path(current_dir, 'json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods1']
    # print(ten_gods1)
    #print(2)
    ten_gods2 = json.loads(Path(current_dir, 'json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods2']
    result = {}
    for key, value in eightchar_data.items():
        if "KorHeavenly" in key and key != 'KorHeavenlyDayText':
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

    # print(is_strong_day_master(eightchar))

    # 지장간
    time_units = ['Time', 'Day', 'Month', 'Year']

    for unit in time_units:
        # 지장간
        elements = EarthlyHeaven_Elements.get(eightchar[f'KorEarthly{unit}Text']).split(',')
        EarthlyHeavenText = ''

        for element in elements:
            current_text = element.split('=')[0] + '=' + element.split('=')[1] + ',' + Heavenly_Five_Elements.get(
                element.split('=')[0], "")
            EarthlyHeavenText += current_text + '|'

        # 지장간 업데이트
        eightchar.update({f'EarthlyHeaven{unit}Element': EarthlyHeavenText[:-1]})
    # 지장간

    # 일간으로 십성 추가
    day_heavenly = eightchar['KorHeavenlyDayText']
    ten_gods_data = add_ten_gods(eightchar, day_heavenly)
    eightchar.update(ten_gods_data)
    eightchar.update({'KorHeavenlyDayTextTenGod': '나'})

    print("십성 추가된 사주 정보:", eightchar)

    print(eightchar['KorHeavenlyTimeText'])
    print(eightchar['KorHeavenlyDayText'])
    print(eightchar['KorHeavenlyMonthText'])
    print(eightchar['KorHeavenlyYearText'])

    print(eightchar['KorEarthlyTimeText'])
    print(eightchar['KorEarthlyDayText'])
    print(eightchar['KorEarthlyMonthText'])
    print(eightchar['KorEarthlyYearText'])

    # 천간합 추출
    Heavenly_list = [eightchar['KorHeavenlyTimeText'], eightchar['KorHeavenlyDayText'],
                     eightchar['KorHeavenlyMonthText'], eightchar['KorHeavenlyYearText']]
    # Heavenly_list = ['갑', '기', '무', '계']

    # 가능한 조합

    print('1')
    KorHeavenlySum = json.loads(Path(current_dir, 'json/plus.json').read_text(encoding='utf-8'))['KorHeavenlySum']
    print('2')
    using_Heavenly_list = ["".join(pair) for pair in itertools.permutations(Heavenly_list, 2)]
    KorHeavenlySumResult = {pair: KorHeavenlySum[pair] for pair in using_Heavenly_list if pair in KorHeavenlySum}

    print('---천간합---')
    print(KorHeavenlySumResult)

    eightchar.update({'KorHeavenlySumResult': KorHeavenlySumResult})

    # 지지합 추출
    Earthly_list = [eightchar['KorEarthlyTimeText'], eightchar['KorEarthlyDayText'], eightchar['KorEarthlyMonthText'],
                    eightchar['KorEarthlyYearText']]
    # 2글자 조합
    KorEarthlySum = json.loads(Path(current_dir, 'json/plus.json').read_text(encoding='utf-8'))['KorEarthlySum']

    usingEarthlylistFor2 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 2)]
    KorEarthlySumResultFor2 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistFor2 if pair in KorEarthlySum}

    usingEarthlylistfor3 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 3)]
    KorEarthlySumResultFor3 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistfor3 if pair in KorEarthlySum}

    EarthlyMergedResult = {**KorEarthlySumResultFor2, **KorEarthlySumResultFor3}
    print('---지지합---')
    print(EarthlyMergedResult)
    eightchar.update({'KorEarthlySumResult': EarthlyMergedResult})

    # 살추출

    eight_list = [eightchar['KorHeavenlyDayText'],

                  eightchar['KorEarthlyTimeText'], eightchar['KorEarthlyDayText'],
                  eightchar['KorEarthlyMonthText'], eightchar['KorEarthlyYearText']
                  ]
    kill_data = json.loads(Path(current_dir, 'json/kill.json').read_text(encoding='utf-8'))

    using_eight_list = ["".join(pair) for pair in itertools.permutations(eight_list, 2)]
    kill_data_result = {pair: kill_data[pair] for pair in using_eight_list if pair in kill_data}

    eightchar.update({'kill_data_result': kill_data_result})
    print('---살---')

    # 처음 입력값 추가
    eightchar.update(data)

    # 신약/추출
    eightchar.update({'strength': evaluate_strength(
        determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],
                          eightchar['EarthlyMonthElement'].split(',')[0].split('=')[0]),
        determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],
                          eightchar['EarthlyDayElement'].split(',')[0].split('=')[0]),
        determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],
                          eightchar['EarthlyYearElement'].split(',')[0].split('=')[0]),
        determine_support(eightchar['HeavenlyDayElement'].split(',')[0].split('=')[0],
                          eightchar['EarthlyTimeElement'].split(',')[0].split('=')[0]))})

    # 일간으로 보는 성격,특징
    dailyTextData = json.loads(Path(current_dir, 'json/dailyText.json').read_text(encoding='utf-8'))

    eightchar.update({'daily_text': dailyTextData[eightchar['KorHeavenlyDayText'] + eightchar['KorEarthlyDayText']]});

    # 세운, 대운 계산하기
    get_solar_term_data = get_solar_term(eightchar)

    result = {}
    for ganji, info in get_solar_term_data.items():
        # 각 ganji에 대한 대운수와 세운
        daewon = info['daewon']
        array = info['array']

        a = {'KorHeavenlyYearText': ganji[0],
             'KorEarthlyYearText': ganji[1]}
        tens_a = add_ten_gods(a, day_heavenly)

        print(daewon)
        print(ganji[0] + '|' + Heavenly_Five_Elements.get(ganji[0], "") + '|' + tens_a['KorHeavenlyYearTextTenGod'])
        print(ganji[1] + '|' + Earthly_Five_Elements.get(ganji[1], "") + '|' + tens_a['KorEarthlyYearTextTenGod'])

        result_array = [];
        for year_info in array:
            ganji_year, year = year_info.split(',')
            b = {'KorHeavenlyYearText': ganji_year[0],
                 'KorEarthlyYearText': ganji_year[1]}

            tens_b = add_ten_gods(b, day_heavenly)

            ganji_year, year = year_info.split(',')
            print(f" - {year}")
            print(ganji_year[0] + '|' + Heavenly_Five_Elements.get(ganji_year[0], "") + '|' + tens_b['KorHeavenlyYearTextTenGod'])
            print(ganji_year[1] + '|' + Earthly_Five_Elements.get(ganji_year[1], "") + '|' + tens_b['KorEarthlyYearTextTenGod'])
            result_array.append({year : ganji_year[0] + '|' + Heavenly_Five_Elements.get(ganji_year[0], "") + '|' + tens_b['KorHeavenlyYearTextTenGod'] + '*' +ganji_year[1] + '|' + Earthly_Five_Elements.get(ganji_year[1], "") + '|' + tens_b['KorEarthlyYearTextTenGod'] })

            print()  # 항목 간 구분을 위한 빈 줄
        print(result_array)

        result.update({daewon: {'daewon': daewon,'data':ganji[0] + '|' + Heavenly_Five_Elements.get(ganji[0], "") + '|' + tens_a['KorHeavenlyYearTextTenGod']+'*'+ganji[1] + '|' + Earthly_Five_Elements.get(ganji[1], "") + '|' + tens_a['KorEarthlyYearTextTenGod'], 'array': result_array}})






    eightchar.update({'future': result})

    print(eightchar)
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
# data = {'gender': '남자', 'calendar': '양력', 'year': '2016', 'month': '8', 'day': '30', 'time': '16'}

# 정목
data = {'gender': '남자', 'calendar': '양력', 'year': '1981', 'month': '3', 'day': '28', 'time': '06'}

# 함수 호출
get_eightzodiac_data(data)
