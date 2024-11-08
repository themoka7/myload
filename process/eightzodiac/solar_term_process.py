import os
from pathlib import Path

import json
from datetime import datetime, timedelta
import math

from process.common.eightchar import get_eightchar
from process.common.eightchar_ver2 import solortoso24

current_dir = os.path.dirname(os.path.abspath(__file__))

class SolarCalculator:
    def __init__(self):
        # 절기 간격 (초 단위) - 평균값을 기준으로 정의
        self.term_offsets = [
            -6418939,  -3871136, -1299777,
            1310827,  3966413,  6660762,
            9376511,  12089855,  14777792,
            17424841,  20027093,  22592403
        ]
        # 절기 이름 리스트
        self.term_names = [
            '입춘',  '경칩',  '청명',
            '입하', '망종',  '소서',
            '입추','백로',  '한로',
            '입동',  '대설',  '소한'
        ]
        # 2000년 춘분점 (2000-03-20 16:35:15, KST 기준)
        self.base_date = datetime(2000, 3, 20, 16, 35, 15)
        self.tropical_year_seconds = 31556925.216  # 평균 태양년 (초)
        self.seconds_per_degree = self.tropical_year_seconds / 360  # 1도 당 초 단위 시간

    def calculate_solar_terms(self, target_year):
        # 2000년부터 target_year까지 경과 시간을 누적
        years_diff = target_year - 2000
        accumulated_time = self.tropical_year_seconds * years_diff
        base_date_for_year = self.base_date + timedelta(seconds=accumulated_time)

        terms = []
        for i, offset in enumerate(self.term_offsets):
            # 기본 절기 계산
            term_date = base_date_for_year + timedelta(seconds=offset)

            # 시황경 보정 적용
            correction = self.solar_longitude_correction(i * 30)  # 각 절기의 목표 시황경 각도
            corrected_term_date = term_date + timedelta(seconds=correction)

            terms.append((self.term_names[i], corrected_term_date))
        return terms

    def solar_longitude_correction(self, target_longitude):
        """시황경 보정을 위한 함수"""
        degree_per_second = self.seconds_per_degree
        # 예시로 주어진 -0.0039682710를 사용해 보정값 계산
        correction_factor = -0.0039682710 * degree_per_second
        return correction_factor

    def find_adjacent_terms(self, target_date):
        """특정 날짜에 대해 이전과 이후 절기를 반환"""
        year = target_date.year
        terms = []

        # 이전 연도와 이후 연도 포함하여 절기 계산
        for y in [year - 1, year, year + 1]:
            terms.extend(self.calculate_solar_terms(y))

        # 절기 정렬
        terms.sort(key=lambda x: x[1])

        previous_term = None
        next_term = None

        # 주어진 날짜 이전과 이후 절기 찾기
        for i in range(len(terms) - 1):
            term_name, term_date = terms[i]
            _, next_term_date = terms[i + 1]

            if term_date <= target_date < next_term_date:
                previous_term = (term_name, term_date)
                next_term = terms[i + 1]
                break

        return previous_term, next_term


def get_solar_term(eightchar):
    print('****')
    print(eightchar)
    #print(eightchar['gender'])
    #print(eightchar['HeavenlyYearElement'].split(',')[1].split('=')[0])

    location = 'forward'

    # 대운 방향 결정
    if eightchar['gender'] == '남성' and eightchar['HeavenlyYearElement'].split(',')[1].split('=')[0] == '음':
        location = 'back'
    if eightchar['gender'] == '여성' and eightchar['HeavenlyYearElement'].split(',')[1].split('=')[0] == '양':
        location = 'back'

    print('location : ' + location)


    # SolarCalculator 인스턴스 생성 및 날짜 변환
    '''calculator = SolarCalculator()
    target_date = datetime.strptime(eightchar['Solar'], '%Y-%m-%d')
    previous_term, next_term = calculator.find_adjacent_terms(target_date)

    print(previous_term)
    print(next_term)'''

    inginame, ingiyear, ingimonth, ingiday, ingihour, ingimin, midname, midyear, midmonth, midday, midhour, midmin, outginame, outgiyear, outgimonth, outgiday, outgihour, outgimin = solortoso24(
        int(eightchar['year']), int(eightchar['month']), int(eightchar['day']), 23, 25)

    #print(ingiyear, ingimonth, ingiday , 23, 25)
    #print(outgiyear, outgimonth, outgiday)

    target_date = datetime( int(eightchar['year']), int(eightchar['month']), int(eightchar['day']), 23, 25)
    previous_term = datetime(ingiyear, ingimonth, ingiday, 23, 25)
    next_term = datetime(outgiyear, outgimonth, outgiday, 23, 25)



    # 절기 출력
    '''if previous_term:
        print(f"이전 절기: {previous_term[0]} - {previous_term[1].strftime('%Y-%m-%d %H:%M:%S')}")
    if next_term:
        print(f"다음 절기: {next_term[0]} - {next_term[1].strftime('%Y-%m-%d %H:%M:%S')}")'''

    # 날짜 차이 계산 및 대운수 결정
    days_difference = None
    if location == 'back' and previous_term:
        days_difference = (target_date - previous_term).days
        #print(f"이전 절기와의 날짜 차이: {days_difference}일")
    elif location == 'forward' and next_term:
        days_difference = (next_term - target_date).days
        #print(f"다음 절기와의 날짜 차이: {days_difference}일")


    if days_difference is not None:
        quotient = days_difference // 3  # 3으로 나눈 몫
        remainder = days_difference % 3  # 3으로 나눈 나머지

        # 반올림 규칙에 따라 대운수 결정
        if remainder == 2:
            daewon = quotient + 1
        else:
            daewon = quotient

        #print(f"대운수: {daewon} (3으로 나눈 결과: {quotient}, 나머지: {remainder})")

    #print(eightchar['KorHeavenlyMonthText'])
    #print(eightchar['KorEarthlyMonthText'])

    ganji_combination = eightchar['KorHeavenlyMonthText'] + eightchar['KorEarthlyMonthText']

    SixtyData = json.loads(Path(current_dir, 'json/60.json').read_text(encoding='utf-8'))
    start_index = SixtyData.get(ganji_combination, None)

    if start_index is None:
        print("조합을 찾을 수 없습니다.")
        return []

        # 방향에 따른 인덱스 리스트 생성
    result_indices = []
    if location == 'back':
        result_indices = [(start_index - i) % 60 for i in range(1, 11)]
    elif location == 'forward':
        result_indices = [(start_index + i) % 60 for i in range(1, 11)]

        # 인덱스에 해당하는 갑자 조합과 대운수 추가


    result_terms_with_daewon = {}
    for i, index in enumerate(result_indices):
        term_name = list(SixtyData.keys())[index]
        daewon_value = daewon + i * 10  # 10씩 증가하는 대운수
        result_terms_with_daewon[term_name] = daewon_value




    # foreach 방식으로 딕셔너리를 순회하며 출력

    ganji_year_combination = eightchar['KorHeavenlyYearText'] + eightchar['KorEarthlyYearText']
    start_index = SixtyData.get(ganji_year_combination, None)

    ganji_month_combination = eightchar['KorHeavenlyMonthText'] + eightchar['KorEarthlyMonthText']
    start_month_index = SixtyData.get(ganji_month_combination, None)

    result = {}
    for ganji, daewon in result_terms_with_daewon.items():

        term_name = list(SixtyData.keys())[(start_index+daewon) % 60 ]

        array = [];
        for i in range(0, 10):
            #print(daewon)
            #print(start_index)
            #print(i+start_index+daewon)
            array.append(list(SixtyData.keys())[(i+start_index+(daewon-1)) % 60 ]+','+str((i +int(eightchar['year']) + (daewon-1))))
            #print('-')

        result.update({ganji :{ 'daewon' : daewon , 'array' : array }})


    print(result)



    return result