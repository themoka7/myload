# 가상의 get_eightchar2 함수를 정의합니다 (실제 코드에서는 필요없습니다)
import calendar
import datetime
import time
from datetime import datetime, timedelta

from process.common.eightchar_ver2 import get_eightchar2, ganji
from process.common.eightchar_ver2 import getlunarfirst


def get_mansae_data(year, month):
    first = get_eightchar2('양력', str(year), str(month), '1', '00')


    print(first)

    last_day = calendar.monthrange(year, month)[1]
    #print('last_day'+str(last_day))

    lunar_date = datetime.strptime(first['Lunar'], '%Y-%m-%d')  # 형식에 맞게 수정 필요
    current_month = lunar_date.month  # 현재 월
    current_year = lunar_date.year  # 현재 연도


    last = getlunarfirst(year, month, last_day)
    print('last : ' + str(last))

    last_day_of_month = last[2]  # 예: 음력 2월의 마지막 날짜가 29일
    results = {}
    change_status = False
    for day in range(1, last_day+1):  # 실제 있을 수 있는 날짜 만큼 반복
        # 만약 'day'가 해당 달의 마지막 날짜를 넘으면

        if day >= last_day_of_month and change_status == False:
            # 월을 증가시키고 날짜는 1일로 초기화
            current_month += 1
            if current_month > 12:  # 12월을 넘으면 1월로 초기화하고 연도도 증가
                current_month = 1
                current_year += 1
            lunar_day = 1  # 날짜를 1일로 초기화
            change_status = True
            lunar_date = lunar_date.replace(year=current_year, month=current_month , day=lunar_day)

        elif day >= last_day_of_month and change_status == True:
            lunar_day += 1
        else:
            lunar_day = day



        # lunar_date에 (day-1)만큼 일수를 더한 새로운 날짜 계산
        new_lunar_date = lunar_date.replace(year=current_year, month=current_month) + timedelta(days=(lunar_day - 1))

        # 날짜를 '월.일' 형식으로 변환
        formatted_date = new_lunar_date.strftime('%m.%d').split('.')

        # 결과 딕셔너리 추가
        results[day] = f"Lunar: {str(int(formatted_date[0])) + '.' + str(int(formatted_date[1]))},char: {ganji[(day - 1 + first['day_index']) % 60]}"






    #print(last_day)
    #last = get_eightchar2('양력', str(year), str(month), last_day, '00')
    #print(last)
    #print(getlunarfirst(year, month, last_day))


    #print(results)
    data = {}
    data.update({'info': first['ChiHeavenlyYearText']+first['ChiEarthlyYearText']+'년 '
                    +first['ChiHeavenlyMonthText']+first['ChiEarthlyMonthText']+'월','results': results})

    return data

print(get_mansae_data(2024,11))
