import os
import json
from korean_lunar_calendar import KoreanLunarCalendar
from datetime import datetime, timedelta

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


#selected_chizodiac = {'gender': '남성', 'calendar': '양력', 'year': '1981', 'month': '3', 'day': '28', 'time': '24'}
selected_chizodiac = {'gender': '여성', 'calendar': '양력', 'year': '1991', 'month': '11', 'day': '19', 'time': '02'}
def get_chizodiac_data(selected_chizodiac):

    year = int(selected_chizodiac['year'])
    month = int(selected_chizodiac['month'])
    day = int(selected_chizodiac['day'])
    time = selected_chizodiac['time']


    calendar = KoreanLunarCalendar()
    if selected_chizodiac['calendar'] != '양력':

        calendar.setLunarDate(year, month, day, False)
        print(calendar.SolarIsoFormat().split('-'))
        year = int(calendar.SolarIsoFormat().split('-')[0])
        month = int(calendar.SolarIsoFormat().split('-')[1])
        day = int(calendar.SolarIsoFormat().split('-')[2])


    # params : year(년), month(월), day(일)
    calendar.setSolarDate(year, month, day)
    # Korean GapJa String
    KorGapJa = calendar.getGapJaString()
    ChiGapJa = calendar.getChineseGapJaString()



    # 루프 돌며 일치하는 항목 찾기
    matching_hour = next((item for item in birth_hour if item["value"] == selected_chizodiac['time']), None)



    new_data = {
        "Lunar": calendar.LunarIsoFormat(),
        "Solar": calendar.SolarIsoFormat(),
        "KorHeavenlyYearText": KorGapJa.split()[0][0],
        "KorEarthlyYearText": KorGapJa.split()[0][1],
        "ChiHeavenlyYearText" : ChiGapJa.split()[0][0],
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
        print(calendar.LunarIsoFormat())

    day_data = {
        "KorHeavenlyDayText": KorGapJa.split()[2][0],
        "KorEarthlyDayText": KorGapJa.split()[2][1],
        "ChiHeavenlyDayText": ChiGapJa.split()[2][0],
        "ChiEarthlyDayText": ChiGapJa.split()[2][1]
    }
    new_data.update(day_data)




    day_gan = KorGapJa.split()[2][0]
    time_index = earthly_branches.index(matching_hour['kor_label'])



    KorHeavenlyTimeText =  calculate_hour_pillar(day_gan, time_index)



    time_data = {
        "KorHeavenlyTimeText": KorHeavenlyTimeText,
        "KorEarthlyTimeText": matching_hour['kor_label'],
        "ChiHeavenlyTimeText": chi_heavenly_stems[heavenly_stems.index(KorHeavenlyTimeText)],
        "ChiEarthlyTimeText": matching_hour['label']
    }

    new_data.update(time_data)




    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'json', f'data.json')

    earthly_branches_index = earthly_branches.index(new_data['KorEarthlyYearText'])
    #print(new_data['KorEarthlyYearText'])
    #print(earthly_branches_index)


    #print(new_data)
    # 파일이 존재하는지 확인
    if os.path.exists(file_path):
        # JSON 파일을 열고 데이터 로드

        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            first_key = list(json_data.keys())[earthly_branches_index]

            #print(first_key)
            #print(json_data[first_key]['생년'][selected_chizodiac['gender']])



            first_index = earthly_branches_index
            offset = int(selected_chizodiac['month'])-1
            second_index = (earthly_branches_index + offset) % 12
            second_key = list(json_data.keys())[second_index]
            #print(second_key)
            #print(json_data[second_key]['생월'][selected_chizodiac['gender']])


            offset = int(selected_chizodiac['day']) - 1
            if(time == '24'):
                offset = offset+1
            third_index = (second_index + offset) % 12
            third_key = list(json_data.keys())[third_index]
            #print(third_key)
            #print(json_data[third_key]['생일'][selected_chizodiac['gender']])

            offset = time_index
            Fourth_index = (third_index + offset) % 12
            Fourth_key = list(json_data.keys())[Fourth_index]
            #print(Fourth_key)
            #print(json_data[Fourth_key]['생시'][selected_chizodiac['gender']])

            content_data = {
                "year_type": first_key,
                "year_contenst": json_data[first_key]['생년'][selected_chizodiac['gender']],

                "month_type": second_key,
                "month_contenst": json_data[second_key]['생월'][selected_chizodiac['gender']],

                "day_type": third_key,
                "day_contenst": json_data[third_key]['생일'][selected_chizodiac['gender']],

                "time_type": Fourth_key,
                "time_contenst": json_data[Fourth_key]['생시'][selected_chizodiac['gender']]

            }

            new_data.update(content_data)

            new_data.update(selected_chizodiac)

    print(new_data)
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

get_chizodiac_data(selected_chizodiac)