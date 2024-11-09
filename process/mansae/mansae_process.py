# 가상의 get_eightchar2 함수를 정의합니다 (실제 코드에서는 필요없습니다)
import calendar
import time

from process.common.eightchar_ver2 import get_eightchar2
from process.common.eightchar_ver2 import getlunarfirst


def get_mansae_data(year, month):

    first = get_eightchar2('양력', str(year), str(month), '1', '00')
    print(getlunarfirst(year, month, 1))

    print(first)
    last_day = calendar.monthrange(year, month)[1]

    print(last_day)
    last = get_eightchar2('양력', str(year), str(month), last_day, '00')
    print(last)
    print(getlunarfirst(year, month, last_day))



    return ''

get_mansae_data(2024,9)