import os

from process.eightzodiac.eightzodiac_process import get_eightzodiac_data



current_dir = os.path.dirname(os.path.abspath(__file__))

data = {'gender': '남자', 'calendar': '양력', 'year': '1980', 'month': '3', 'day': '11', 'time': '06'}
Plust_Elements = {
    '목': '수',
    '화': '목',
    '토': '화',
    '금': '토',
    '수': '금',


}

print(get_eightzodiac_data(data))

ea = get_eightzodiac_data(data)



base = ea['HeavenlyDayElement']


print(Plust_Elements[base.split(',')[0].split('=')[0]])
print('-')
point = 0
time_units = ['Time',  'Month', 'Year']


for unit in time_units:
    a = ea[f'Heavenly{unit}Element']

    '''생관계인 경우 40점'''
    if Plust_Elements[base.split(',')[0].split('=')[0]] == a.split(',')[0].split('=')[0]:
        point += 40
    '''같은 경우 30점'''
    if base.split(',')[0].split('=')[0] == a.split(',')[0].split('=')[0]:
        point += 30




print(point)
print( ea['HeavenlyYearElement'])
print( ea['HeavenlyMonthElement'])
print( ea['HeavenlyDayElement'])
print( ea['HeavenlyTimeElement'])


print( ea['EarthlyYearElement'])
print( ea['EarthlyMonthElement'])
print( ea['EarthlyDayElement'])
print( ea['EarthlyTimeElement'])