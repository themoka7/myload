import os
import json
from skyfield.api import load, utc
from skyfield.framelib import ecliptic_frame
from datetime import datetime, timedelta


def get_dailystarzodiac_data():
    new_data = []  # 새로운 데이터를 저장할 리스트


    # Skyfield 타임스케일과 태양계 데이터 로드
    ts = load.timescale()
    planets = load('de421.bsp')
    moon = planets['moon']
    earth = planets['earth']

    # 오늘의 시작 시간 (UTC 기준)

    korea_time = (datetime.utcnow() + timedelta(hours=9)).replace(tzinfo=utc)

    t = ts.utc(korea_time )


    # 황도 12궁 구간 설정
    signs = [
        "양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리",
        "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"
    ]

    # 각 시간에 따른 달의 별자리 위치 계산

    # 지구에서 본 달의 위치 계산
    astrometric = earth.at(t).observe(moon).apparent()
    ecliptic_latlon = astrometric.frame_latlon(ecliptic_frame)
    ecliptic_longitude = ecliptic_latlon[1].degrees  # 달의 황도 경도

    # 별자리 구간 계산 (황도 경도를 30도로 나눔)
    index = int(ecliptic_longitude // 30)  # 각 별자리는 30도씩 차지
    zodiac_sign = signs[index]

    # 출력
    #print(f"{t.utc_datetime().strftime('%Y-%m-%d %H:%M:%S')} - 달은 '{zodiac_sign}'에 위치 (황도 경도: {ecliptic_longitude:.2f}도)")
    #print(ecliptic_longitude)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'json', f'data.json')

    ecliptic_longitude = round(float(ecliptic_longitude), 2)
    new_data = {
        "zodiac_sign": zodiac_sign,
        "ecliptic_longitude": ecliptic_longitude
    }

    if os.path.exists(file_path):
        #print('1')
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            #print(json_data)
            for range_str, zodiac_data in json_data.items():
                start, end = map(float, range_str.split("~"))

                if start <= ecliptic_longitude < end:
                    #print('2')
                    #print(zodiac_data)
                    zodiac_data = {
                        "zodiac_data": zodiac_data
                    }
                    new_data.update(zodiac_data)



    return new_data

#print(get_dailystarzodiac_data())