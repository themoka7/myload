import itertools
import os
from pathlib import Path
import json

from process.common.eightchar import get_eightchar


# 데이터에 십성 추가 함수
def add_ten_gods(eightchar_data, day_heavenly):
    ten_gods1 = json.loads(Path('json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods1']
    #print(ten_gods1)
    ten_gods2 = json.loads(Path('json/ten_gods.json').read_text(encoding='utf-8'))['ten_gods2']
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

    # 일간으로 십성 추가
    day_heavenly = eightchar['KorHeavenlyDayText']
    ten_gods_data = add_ten_gods(eightchar, day_heavenly)
    eightchar.update(ten_gods_data)

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
    KorHeavenlySum = json.loads(Path('json/plus.json').read_text(encoding='utf-8'))['KorHeavenlySum']
    using_Heavenly_list = ["".join(pair) for pair in itertools.permutations(Heavenly_list, 2)]
    KorHeavenlySumResult = {pair: KorHeavenlySum[pair] for pair in using_Heavenly_list if pair in KorHeavenlySum}


    eightchar.update({'KorHeavenlySumResult': KorHeavenlySumResult})

    # 지지합 추출
    Earthly_list = [eightchar['KorEarthlyTimeText'], eightchar['KorEarthlyDayText'],eightchar['KorEarthlyMonthText'], eightchar['KorEarthlyYearText']]
    #2글자 조합
    KorEarthlySum = json.loads(Path('json/plus.json').read_text(encoding='utf-8'))['KorEarthlySum']

    usingEarthlylistFor2 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 2)]
    KorEarthlySumResultFor2 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistFor2 if pair in KorEarthlySum}

    usingEarthlylistfor3 = ["".join(pair) for pair in itertools.permutations(Earthly_list, 3)]
    KorEarthlySumResultFor3 = {pair: KorEarthlySum[pair] for pair in usingEarthlylistfor3 if pair in KorEarthlySum}

    print(KorEarthlySumResultFor2)
    print(KorEarthlySumResultFor3)

    EarthlyMergedResult = {**KorEarthlySumResultFor2, **KorEarthlySumResultFor3}
    eightchar.update({'KorEarthlySumResult': EarthlyMergedResult})

    print(eightchar)


    return eightchar

# 예시 데이터
data = {'gender': '남자', 'calendar': '양력', 'year': '1983', 'month': '2', 'day': '15', 'time': '08'}

# 함수 호출
get_eightzodiac_data(data)
