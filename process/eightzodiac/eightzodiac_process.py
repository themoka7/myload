from process.common.eightchar import get_eightchar

data = {'gender': '여성', 'calendar': '양력', 'year': '1991', 'month': '11', 'day': '19', 'time': '02'}

def get_eightzodiac_data(data):


    eightchar = get_eightchar(data['calendar'], data['year'], data['month'], data['day'], data['time'])


    #print(eightchar)

    return eightchar


get_eightzodiac_data(data)