import requests

# API 설정
service_key = "JtJhymvob4OUmGDWOar%2FKiCLEpSRPEBCvPRAdiwCH9699h4K%2B876%2FW0vCqWuuxz8SVqu%2BypCSWEkfpraCtscKw%3D%3D"
year = 1981

# 월별 데이터를 저장할 리스트
results = []

for month in range(1, 13):  # 1월부터 12월까지
    sol_month = f"{month:02}"  # 월을 2자리 형식으로 만듦
    url = f"https://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/get24DivisionsInfo"
    params = {
        "serviceKey": service_key,
        "solYear": year,
        "solMonth": sol_month,
        "kst": "0120",  # 한국표준시간
        "sunLongitude": "285",
        "numOfRows": "10",
        "pageNo": "1"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # XML 응답을 파싱
        results.append(response.text)
        print(f"{sol_month}월 데이터 성공적으로 가져옴")
    else:
        print(f"{sol_month}월 데이터 가져오기 실패: {response.status_code}")

# 모든 데이터를 리스트에 저장 후 처리 가능
print("1981년 1월부터 12월까지 데이터 수집 완료.")
