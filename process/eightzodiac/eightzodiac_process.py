import itertools
import os
from pathlib import Path
import json

from process.common.eightchar import get_eightchar


# 데이터에 십성 추가 함수
current_dir = os.path.dirname(os.path.abspath(__file__))

Heavenly_Five_Elements = {
    '갑': 'GREEN, 목=木, 양=陽', '을': '목=木, 음=陰', '병': '화=火, 양=陽', '정': '화=火, 음=陰',
    '무': '토=土, 양=陽', '기': '토=土, 음=陰', '경': '금=金, 양=陽', '신': '금=金, 음=陰',
    '임': '수=水, 양=陽', '계': '수=水, 음=陰'
}

Earthly_Five_Elements = {
    '자': '수=水, 양=陽', '축': '토=土, 음=陰', '인': '목=木, 양=陽', '묘': '목=木, 음=陰',
    '진': '토=土, 양=陽', '사': '화=火, 음=陰', '오': '화=火, 양=陽', '미': '토=土, 음=陰',
    '신': '금=金, 음=陰', '유': '금=金, 양=陽', '술': '토=土, 양=陽', '해': '수=水, 음=陰'
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


    # 살추출

    print(eightchar)
    return eightchar

# 예시 데이터
# 환희
#data = {'gender': '남자', 'calendar': '양력', 'year': '2016', 'month': '8', 'day': '30', 'time': '16'}

# 정목
data = {'gender': '남자', 'calendar': '양력', 'year': '1981', 'month': '3', 'day': '28', 'time': '06'}


# 함수 호출
get_eightzodiac_data(data)