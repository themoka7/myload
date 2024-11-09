# 가상의 get_eightchar2 함수를 정의합니다 (실제 코드에서는 필요없습니다)
import calendar

from process.common.eightchar_ver2 import get_eightchar2


def get_mansae_data(year, month):
    results = {}
    # 해당 월의 마지막 날짜 계산
    last_day = calendar.monthrange(year, month)[1]

    for day in range(1, last_day + 1):  # 실제 있는 날짜만큼 반복
        result = get_eightchar2('양력', str(year), str(month), str(day), '00')
        #print(result)
        lunar_full = result['Lunar']
        lunar_parts = lunar_full.split('-')  # ["2024", "10", "1"]
        results[day] = f"Lunar: {lunar_parts[1]}.{lunar_parts[2]},char: {result['ChiHeavenlyDayText']}{result['ChiEarthlyDayText']}"

    return results