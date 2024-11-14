from datetime import datetime, timedelta

from korean_lunar_calendar import KoreanLunarCalendar

heavenly_stems = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
chi_heavenly_stems = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
earthly_branches = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']


birth_hour = [{ "value": "00", "label": "子", "kor_label" : "자" },
    { "value": "02", "label": "丑" , "kor_label" : "축"},
    { "value": "04", "label": "寅" , "kor_label" : "인"},
    { "value": "06", "label": "卯" , "kor_label" : "묘"},
    { "value": "08", "label": "辰" , "kor_label" : "진"},
    { "value": "10", "label": "巳" , "kor_label" : "사"},
    { "value": "12", "label": "午" , "kor_label" : "오"},
    { "value": "14", "label": "未" , "kor_label" : "미"},
    { "value": "16", "label": "申" , "kor_label" : "신"},
    { "value": "18", "label": "酉" , "kor_label" : "유"},
    { "value": "20", "label": "戌" , "kor_label" : "술"},
    { "value": "22", "label": "亥" , "kor_label" : "해"},
    { "value": "24", "label": "子" , "kor_label" : "자"}
  ]

def get_eightchar(type, year, month, day, time):


    year = int(year)
    month = int(month)
    day = int(day)
    time = time


    calendar = KoreanLunarCalendar()
    #print(calendar)
    if type != '양력':
        calendar.setLunarDate(year, month, day, False)
        #print(calendar.SolarIsoFormat().split('-'))
        year = int(calendar.SolarIsoFormat().split('-')[0])
        month = int(calendar.SolarIsoFormat().split('-')[1])
        day = int(calendar.SolarIsoFormat().split('-')[2])


    # params : year(년), month(월), day(일)
    #print(year)
    #print(month)
    #print(day)
    calendar.setSolarDate(year, month, day)
    # Korean GapJa String
    KorGapJa = calendar.getGapJaString()
    #print(KorGapJa)
    ChiGapJa = calendar.getChineseGapJaString()
    #print(ChiGapJa)



    # 루프 돌며 일치하는 항목 찾기
    matching_hour = next((item for item in birth_hour if item["value"] == time), None)



    new_data = {
        "Lunar": calendar.LunarIsoFormat(),
        "Solar": calendar.SolarIsoFormat(),
        "KorHeavenlyYearText": KorGapJa.split()[0][0],
        "KorEarthlyYearText": KorGapJa.split()[0][1],
        "ChiHeavenlyYearText": ChiGapJa.split()[0][0],
        "ChiEarthlyYearText": ChiGapJa.split()[0][1],

        "KorHeavenlyMonthText": KorGapJa.split()[1][0],
        "KorEarthlyMonthText": KorGapJa.split()[1][1],
        "ChiHeavenlyMonthText": ChiGapJa.split()[1][0],
        "ChiEarthlyMonthText": ChiGapJa.split()[1][1],

    }

    if time == '24':
        date = datetime(year, month, day) + timedelta(days=1)  # 하루 더하기
        calendar.setSolarDate(date.year, date.month, date.day)
        KorGapJa = calendar.getGapJaString()
        ChiGapJa = calendar.getChineseGapJaString()


    day_data = {
        "KorHeavenlyDayText": KorGapJa.split()[2][0],
        "KorEarthlyDayText": KorGapJa.split()[2][1],
        "ChiHeavenlyDayText": ChiGapJa.split()[2][0],
        "ChiEarthlyDayText": ChiGapJa.split()[2][1]
    }
    new_data.update(day_data)

    day_gan = KorGapJa.split()[2][0]
    time_index = earthly_branches.index(matching_hour['kor_label'])

    KorHeavenlyTimeText = calculate_hour_pillar(day_gan, time_index)

    time_data = {
        "KorHeavenlyTimeText": KorHeavenlyTimeText,
        "KorEarthlyTimeText": matching_hour['kor_label'],
        "ChiHeavenlyTimeText": chi_heavenly_stems[heavenly_stems.index(KorHeavenlyTimeText)],
        "ChiEarthlyTimeText": matching_hour['label']
    }

    new_data.update(time_data)



    return new_data


gan_cycles = {
    '갑': ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계', '갑', '을'],
    '기': ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계', '갑', '을'],
    '을': ['병', '정', '무', '기', '경', '신', '임', '계', '갑', '을', '병', '정'],
    '경': ['병', '정', '무', '기', '경', '신', '임', '계', '갑', '을', '병', '정'],
    '병': ['무', '기', '경', '신', '임', '계', '갑', '을', '병', '정', '무', '기'],
    '신': ['무', '기', '경', '신', '임', '계', '갑', '을', '병', '정', '무', '기'],
    '정': ['경', '신', '임', '계', '갑', '을', '병', '정', '무', '기', '경', '신'],
    '임': ['경', '신', '임', '계', '갑', '을', '병', '정', '무', '기', '경', '신'],
    '무': ['임', '계', '갑', '을', '병', '정', '무', '기', '경', '신', '임', '계'],
    '계': ['임', '계', '갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
}
def calculate_hour_pillar(day_gan, hour_branch_index):
    gan_cycle = gan_cycles[day_gan]
    return gan_cycle[hour_branch_index]

#get_eightchar('양력', '1981','3','28','02')




# 오행 상생/상극 관계 설정
element_relationships = {
    "목": {"생": "화", "극": "토"},
    "화": {"생": "토", "극": "금"},
    "토": {"생": "금", "극": "수"},
    "금": {"생": "수", "극": "목"},
    "수": {"생": "목", "극": "화"}
}


def determine_support(day_element, branch_element):
    # 일간과 지지가 같은 오행이거나, 일간을 생해주는 오행일 경우 지원함
    if branch_element == day_element:
        return True
    elif element_relationships[day_element]["생"] == branch_element:
        return True
    else:
        return False


# 신강 신약 판단 함수 (이전 코드)
def evaluate_strength(month_branch, day_branch, year_branch, hour_branch):
    month_status = "O" if month_branch else "X"
    day_status = "O" if day_branch else "X"
    year_status = "O" if year_branch else "X"
    hour_status = "O" if hour_branch else "X"

    # 최강 조건 - 월지와 일지에서 힘을 얻고, 년지나 시지에서도 힘을 얻음
    if month_branch and day_branch and (year_branch or hour_branch):
        return f"최강|월지와 일지에서 힘을 얻고, 년지나 시지에서도 도움을 받음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 중강 조건 - 월지와 일지에서 힘을 얻고, 년지와 시지에서는 힘을 얻지 못함
    elif month_branch and day_branch:
        return f"중강|월지와 일지에서 힘을 얻고, 년지와 시지에서 추가적인 도움을 받지 못함|시지={hour_status},일지={day_status}, 월지={month_status},년지={year_status}"

    # 강 조건 - 월지에서 힘을 얻고, 년지 또는 시지에서도 도움을 받음
    elif month_branch and (year_branch or hour_branch):
        return f"강|월지에서 힘을 얻고, 년지 또는 시지에서 추가적인 힘을 받음|시지={hour_status}, 일지={day_status},월지={month_status},년지={year_status}"

    # 최약 조건 - 월지와 일지 모두에서 힘을 얻지 못하고, 년지와 시지에서도 도움을 받지 못함
    elif not month_branch and not day_branch and not (year_branch or hour_branch):
        return f"최약|월지와 일지 모두에서 힘을 얻지 못하며, 년지와 시지에서도 지원이 없음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 중약 조건 - 월지에서는 힘을 얻지 못하지만, 일지 또는 년지/시지에서 부분적인 도움을 받음
    elif not month_branch and (day_branch or year_branch or hour_branch):
        return f"중약|월지에서 힘을 얻지 못하지만, 일지 또는 년지/시지에서 일부 도움을 받음|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 약 조건 - 월지에서 힘을 얻으나, 일지, 년지, 시지에서 추가적인 도움을 받지 못함
    elif month_branch and not (day_branch or year_branch or hour_branch):
        return f"약|월지에서만 힘을 얻고, 다른 지지에서는 도움을 받지 못함|시지={hour_status},일지={day_status},월지={month_status},년지={year_status}"

    # 기타 경우
    else:
        return f"없음|조건에 맞지 않는 경우|시지={hour_status},일지={day_status},월지={month_status},년지={year_status})"