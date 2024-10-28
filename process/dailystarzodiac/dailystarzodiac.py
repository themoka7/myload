from skyfield.api import load, utc
from skyfield.framelib import ecliptic_frame
from datetime import datetime, timedelta

# Skyfield 타임스케일과 태양계 데이터 로드
ts = load.timescale()
planets = load('de421.bsp')
moon = planets['moon']
earth = planets['earth']

# 오늘의 시작 시간 (UTC 기준)
start_time = (datetime.utcnow() - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=utc)

# 2시간 간격으로 12회 계산 (총 24시간)
interval = 2  # 시간 간격 (시간 단위)
times = [ts.utc((start_time + timedelta(hours=interval * i)).replace(tzinfo=utc)) for i in range(12)]

# 황도 12궁 구간 설정
signs = [
    "양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리",
    "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"
]

# 각 시간에 따른 달의 별자리 위치 계산
for t in times:
    # 지구에서 본 달의 위치 계산
    astrometric = earth.at(t).observe(moon).apparent()
    ecliptic_latlon = astrometric.frame_latlon(ecliptic_frame)
    ecliptic_longitude = ecliptic_latlon[1].degrees  # 달의 황도 경도

    # 별자리 구간 계산 (황도 경도를 30도로 나눔)
    index = int(ecliptic_longitude // 30)  # 각 별자리는 30도씩 차지
    zodiac_sign = signs[index]

    # 출력
    print(
        f"{t.utc_datetime().strftime('%Y-%m-%d %H:%M:%S')} - 달은 '{zodiac_sign}'에 위치 (황도 경도: {ecliptic_longitude:.2f}도)")
