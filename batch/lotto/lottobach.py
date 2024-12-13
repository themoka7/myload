import sys
from datetime import datetime, timedelta

import requests
sys.path.append('/home/kimjungmok/mysite')


from batch.lotto.db.dbinsert import dbinsert_server
from batch.lotto.db.dbinsert_local import dbinsert_local

# 기준 날짜 및 회차
base_date = datetime(2024, 12, 7)  # 기준 토요일 날짜 (1149회차)
base_round = 1149  # 기준 회차

#로컬 이건로컬


def calculate_lotto_round(target_date=None):
    """
    주어진 날짜 기준으로 로또 회차를 계산 (일요일에 변경)
    """
    if target_date is None:
        target_date = datetime.now()  # 기본: 현재 날짜 기준

    # 기준 날짜와 주어진 날짜 간의 차이 계산
    days_difference = (target_date - base_date).days
    weeks_difference = days_difference // 7  # 7일마다 한 회차

    # 현재 회차 계산 (일요일부터 다음 회차로 넘어감)
    current_round = base_round + weeks_difference
    sunday_of_week = base_date + timedelta(weeks=weeks_difference)

    # target_date가 일요일 0시 이전이라면 이전 회차를 반환
    if target_date < sunday_of_week + timedelta(days=1):
        current_round -= 1
        sunday_of_week -= timedelta(weeks=1)

    return current_round, sunday_of_week

def next_lotto_date(current_sunday):
    """
    현재 회차의 다음 일요일 날짜 계산
    """
    return current_sunday + timedelta(days=7)


# 예제: 오늘 날짜 기준으로 계산
today = datetime.now()
current_round, current_sunday = calculate_lotto_round(today)

print(f"오늘 기준 회차: {current_round}, 해당 일요일: {current_sunday.strftime('%Y-%m-%d')}")

# 다음 회차 일요일
next_sunday = next_lotto_date(current_sunday)
print(f"다음 회차 일요일: {next_sunday.strftime('%Y-%m-%d')}")



# API 호출
url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={current_round}"
response = requests.get(url)
data = response.json()

print('dbinsert_server')
dbinsert_server(data)