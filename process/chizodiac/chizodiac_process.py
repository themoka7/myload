import importlib
import os
import sys

import json
from korean_lunar_calendar import KoreanLunarCalendar
from datetime import datetime, timedelta

from process.common.eightchar import get_eightchar

#selected_chizodiac = {'gender': '남성', 'calendar': '양력', 'year': '1981', 'month': '3', 'day': '28', 'time': '24'}
selected_chizodiac = {'gender': '여성', 'calendar': '양력', 'year': '1991', 'month': '11', 'day': '19', 'time': '02'}

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

def get_chizodiac_data(selected_chizodiac):


    eightchar = get_eightchar(selected_chizodiac['calendar'], selected_chizodiac['year'], selected_chizodiac['month'], selected_chizodiac['day'], selected_chizodiac['time'])




    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'json', f'data.json')

    earthly_branches_index = earthly_branches.index(eightchar['KorEarthlyYearText'])



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
            if(selected_chizodiac['time'] == '24'):
                offset = offset+1
            third_index = (second_index + offset) % 12
            third_key = list(json_data.keys())[third_index]
            #print(third_key)
            #print(json_data[third_key]['생일'][selected_chizodiac['gender']])

            matching_hour = next((item for item in birth_hour if item["value"] == selected_chizodiac['time']), None)

            offset = earthly_branches.index(matching_hour['kor_label'])
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

            eightchar.update(content_data)

            eightchar.update(selected_chizodiac)

    #print(eightchar)
    return eightchar


#get_chizodiac_data(selected_chizodiac)