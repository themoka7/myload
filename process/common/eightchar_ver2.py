import datetime
import time as ttm
# Constants
montharray = [0, 21355, 42843, 64498, 86335, 108366, 130578, 152958,
              175471, 198077, 220728, 243370, 265955, 288432, 310767, 332928,
              354903, 376685, 398290, 419736, 441060, 462295, 483493, 504693, 525949]

monthst = ['입춘', '우수', '경칩', '춘분', '청명', '곡우',
           '입하', '소만', '망종', '하지', '소서', '대서',
           '입추', '처서', '백로', '추분', '한로', '상강',
           '입동', '소설', '대설', '동지', '소한', '대한', '입춘']

gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
ji = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

ganji = ['甲子','乙丑','丙寅','丁卯','戊辰',
        '己巳','庚午','辛未','壬申','癸酉',
        '甲戌','乙亥','丙子','丁丑','戊寅',

        '己卯','庚辰','辛巳','壬午','癸未',
        '甲申','乙酉','丙戌','丁亥','戊子',
        '己丑','庚寅','辛卯','壬辰','癸巳',

        '甲午','乙未','丙申','丁酉','戊戌',
        '己亥','庚子','辛丑','壬寅','癸卯',
        '甲辰','乙巳','丙午','丁未','戊申',

        '己酉','庚戌','辛亥','壬子','癸丑',
        '甲寅','乙卯','丙辰','丁巳','戊午',
        '己未','庚申','辛酉','壬戌','癸亥']

kor_ganji = [
    '갑자', '을축', '병인', '정묘', '무진',
    '기사', '경오', '신미', '임신', '계유',
    '갑술', '을해', '병자', '정축', '무인',

    '기묘', '경진', '신사', '임오', '계미',
    '갑신', '을유', '병술', '정해', '무자',
    '기축', '경인', '신묘', '임진', '계사',

    '갑오', '을미', '병신', '정유', '무술',
    '기해', '경자', '신축', '임인', '계묘',
    '갑진', '을사', '병오', '정미', '무신',

    '기유', '경술', '신해', '임자', '계축',
    '갑인', '을묘', '병진', '정사', '무오',
    '기미', '경신', '신유', '임술', '계해'
]


weekday = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

s28day = ['角', '亢', '저', '房', '心', '尾', '箕',
          '斗', '牛', '女', '虛', '危', '室', '壁',
          '奎', '누', '胃', '昴', '畢', '자', '參',
          '井', '鬼', '柳', '星', '張', '翼', '진']

# Unit constants
unityear, unitmonth, unitday, unithour, unitmin, unitsec = 1996, 2, 4, 22, 8, 0
unitmyear, unitmmonth, unitmday, unitmhour, unitmmin, unitmsec = 1996, 2, 19, 8, 30, 0
moonlength = 42524  # 42524 minutes 2.9 seconds


from typing import Tuple

def disptimeday(year: int, month: int, day: int) -> int:
    """
    Calculate the number of days from January 1st of the given year to the specified date.
    """
    e = 0
    for i in range(1, month):
        e += 31
        if i in [2, 4, 6, 9, 11]:
            e -= 1
        if i == 2:
            e -= 2
            if year % 4 == 0:
                e += 1
            if year % 100 == 0:
                e -= 1
            if year % 400 == 0:
                e += 1
            if year % 4000 == 0:
                e -= 1
    return e + day



def disp2days(y1: int, m1: int, d1: int, y2: int, m2: int, d2: int) -> int:
    # y1, m1, d1부터 y2, m2, d2까지의 일수 계산
    if y2 > y1:
        p2 = disptimeday(y2, m2, d2)
        p1 = disptimeday(y1, m1, d1)
        p1n = disptimeday(y1, 12, 31)
        pp1 = y1
        pp2 = y2
        pr = -1
    else:
        p1 = disptimeday(y2, m2, d2)
        p1n = disptimeday(y2, 12, 31)
        p2 = disptimeday(y1, m1, d1)
        pp1 = y2
        pp2 = y1
        pr = 1

    if y2 == y1:
        dis = p2 - p1
    else:
        dis = p1n - p1
        ppp1 = pp1 + 1
        ppp2 = pp2 - 1

        i = dis

        while ppp1 <= ppp2:
            if (ppp1 == -9000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 4014377
            if (ppp1 == -8000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 3649135
            if (ppp1 == -7000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 3283893
            if (ppp1 == -6000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 2918651
            if (ppp1 == -5000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 2553408
            if (ppp1 == -4000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 2188166
            if (ppp1 == -3000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1822924
            if (ppp1 == -2000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1457682
            if (ppp1 == -1750) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1366371
            if (ppp1 == -1500) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1275060
            if (ppp1 == -1250) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1183750
            if (ppp1 == -1000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1092439
            if (ppp1 == -750) and (ppp2 > 1990):
                ppp1 = 1991
                i += 1001128
            if (ppp1 == -500) and (ppp2 > 1990):
                ppp1 = 1991
                i += 909818
            if (ppp1 == -250) and (ppp2 > 1990):
                ppp1 = 1991
                i += 818507
            if (ppp1 == 0) and (ppp2 > 1990):
                ppp1 = 1991
                i += 727197
            if (ppp1 == 250) and (ppp2 > 1990):
                ppp1 = 1991
                i += 635887
            if (ppp1 == 500) and (ppp2 > 1990):
                ppp1 = 1991
                i += 544576
            if (ppp1 == 750) and (ppp2 > 1990):
                ppp1 = 1991
                i += 453266
            if (ppp1 == 1000) and (ppp2 > 1990):
                ppp1 = 1991
                i += 361955
            if (ppp1 == 1250) and (ppp2 > 1990):
                ppp1 = 1991
                i += 270644
            if (ppp1 == 1500) and (ppp2 > 1990):
                ppp1 = 1991
                i += 179334
            if (ppp1 == 1750) and (ppp2 > 1990):
                ppp1 = 1991
                i += 88023

            i += disptimeday(ppp1, 12, 31)
            ppp1 += 1

        dis = i
        dis += p2
        dis *= pr

    return dis


def getminbytime(uy, umm, ud, uh, umin, y1, mo1, d1, h1, mm1):
    dispday = disp2days(uy, umm, ud, y1, mo1, d1)
    t = dispday * 24 * 60 + (uh - h1) * 60 + (umin - mm1)
    return t





def getdatebymin(tmin, uyear, umonth, uday, uhour, umin):
    y1 = uyear - tmin // 525949
    if tmin >= 0:
        y1 += 2
        while True:
            y1 -= 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, 1, 1, 0, 0)
            if t >= tmin:
                break
        mo1 = 13
        while True:
            mo1 -= 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, 1, 0, 0)
            if t >= tmin:
                break
        d1 = 32
        while True:
            d1 -= 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, 0, 0)
            if t >= tmin:
                break
        h1 = 24
        while True:
            h1 -= 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, h1, 0)
            if t >= tmin:
                break
        t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, h1, 0)
        mi1 = t - tmin
    else:
        y1 -= 2
        while True:
            y1 += 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, 1, 1, 0, 0)
            if t < tmin:
                break
        y1 -= 1
        mo1 = 0
        while True:
            mo1 += 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, 1, 0, 0)
            if t < tmin:
                break
        mo1 -= 1
        d1 = 0
        while True:
            d1 += 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, 0, 0)
            if t < tmin:
                break
        d1 -= 1
        h1 = -1
        while True:
            h1 += 1
            t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, h1, 0)
            if t < tmin:
                break
        h1 -= 1
        t = getminbytime(uyear, umonth, uday, uhour, umin, y1, mo1, d1, h1, 0)
        mi1 = t - tmin

    return y1, mo1, d1, h1, mi1




def getweekday(syear, smonth, sday):
    # disp2days 함수를 Python에 맞게 정의했다고 가정합니다.
    # unityear, unitmonth, unitday는 기준 날짜입니다. 필요에 맞게 수정하세요.
    unityear, unitmonth, unitday = 2023, 1, 1  # 예시 기준 날짜

    # disp2days 함수가 두 날짜 사이의 일수를 계산한다고 가정
    d = disp2days(syear, smonth, sday, unityear, unitmonth, unitday)

    # 7로 나눈 몫과 나머지 계산
    i = d // 7
    d = d - (i * 7)

    # d가 0~6 범위 내에 들어올 때까지 조정
    while (d > 6) or (d < 0):
        if d > 6:
            d -= 7
        else:
            d += 7

    # d가 0보다 작으면 7을 더해 양수로 조정
    if d < 0:
        d += 7

    return d



def get28sday(syear, smonth, sday):
   d,i = 0, 0

   d  = disp2days(syear,smonth,sday,unityear,unitmonth,unitday);
   i = d // 28 ;
   d = d - ( i * 28 );

   # 변수 d가 주어졌다고 가정
   while (d > 27) or (d < 0):
       if d > 27:
           d -= 28
       else:
           d += 28

   d -= 11
   if d < 0:
       d += 28

   return d






def sydtoso24yd(soloryear, solormonth, solorday, solorhour, solormin):

    displ2min = getminbytime(unityear, unitmonth, unitday, unithour, unitmin,
                              soloryear, solormonth, solorday, solorhour, solormin)
    displ2day = disp2days(unityear, unitmonth, unitday, soloryear, solormonth, solorday)


    so24 = displ2min // 525949  # 무인년(1996)입춘시점부터 해당일시까지 경과년수

    if displ2min >= 0:
        so24 += 1
    so24year = -1 * (so24 % 60)
    so24year += 12
    if so24year < 0:
        so24year += 60
    if so24year > 59:
        so24year -= 60  # 년주 구함 끝

    #print('so24year')
    #print(so24year)

    monthmin100 = displ2min % 525949
    monthmin100 = 525949 - monthmin100

    if monthmin100 < 0:
        monthmin100 += 525949
    if monthmin100 >= 525949:
        monthmin100 -= 525949

    for i in range(12):
        j = i * 2
        if montharray[j] <= monthmin100 < montharray[j + 2]:
            so24month = i

    i = so24month
    t = so24year % 10
    t = t % 5
    t = t * 12 + 2 + i
    so24month = t  # 월주 구함 끝


    if so24month > 59:
        so24month -= 60

    so24day = displ2day % 60
    so24day = -1 * so24day
    so24day += 7

    if so24day < 0:
        so24day += 60
    if so24day > 59:
        so24day -= 60  # 일주 구함 끝

    if (solorhour == 0) or ((solorhour == 1) and (solormin < 30)):
        i = 0

    if ((solorhour == 1) and (solormin >= 30)) or (solorhour == 2) or \
       ((solorhour == 3) and (solormin < 30)):
        i = 1

    if ((solorhour == 3) and (solormin >= 30)) or (solorhour == 4) or \
       ((solorhour == 5) and (solormin < 30)):
        i = 2

    if ((solorhour == 5) and (solormin >= 30)) or (solorhour == 6) or \
       ((solorhour == 7) and (solormin < 30)):
        i = 3

    if ((solorhour == 7) and (solormin >= 30)) or (solorhour == 8) or \
       ((solorhour == 9) and (solormin < 30)):
        i = 4

    if ((solorhour == 9) and (solormin >= 30)) or (solorhour == 10) or \
       ((solorhour == 11) and (solormin < 30)):
        i = 5

    if ((solorhour == 11) and (solormin >= 30)) or (solorhour == 12) or \
       ((solorhour == 13) and (solormin < 30)):
        i = 6

    if ((solorhour == 13) and (solormin >= 30)) or (solorhour == 14) or \
       ((solorhour == 15) and (solormin < 30)):
        i = 7

    if ((solorhour == 15) and (solormin >= 30)) or (solorhour == 16) or \
       ((solorhour == 17) and (solormin < 30)):
        i = 8

    if ((solorhour == 17) and (solormin >= 30)) or (solorhour == 18) or \
       ((solorhour == 19) and (solormin < 30)):
        i = 9

    if ((solorhour == 19) and (solormin >= 30)) or (solorhour == 20) or \
       ((solorhour == 21) and (solormin < 30)):
        i = 10

    if ((solorhour == 21) and (solormin >= 30)) or (solorhour == 22) or \
       ((solorhour == 23) and (solormin < 30)):
        i = 11

    if (solorhour == 23) and (solormin >= 30):
        so24day += 1
        if so24day == 60:
            so24day = 0
        i = 0

    t = so24day % 10
    t = t % 5
    t = t * 12 + i
    so24hour = t  # 시주 구함 끝

    #print('*****************************************')
    #print(so24, so24year, so24month, so24day, so24hour)
    #print(so24, so24year, so24month, so24day, so24hour)
    #print('*****************************************')
    return so24, so24year, so24month, so24day, so24hour



def solortoso24(soloryear, solormonth, solorday, solorhour, solormin):

    # Call to sydtoso24yd function should be implemented
    so24, so24year, so24month, so24day, so24hour = sydtoso24yd(soloryear, solormonth, solorday, solorhour, solormin)


    displ2min = getminbytime(unityear, unitmonth, unitday, unithour, unitmin,
                              soloryear, solormonth, solorday, solorhour, solormin)

    monthmin100 = displ2min % 525949
    monthmin100 = 525949 - monthmin100

    if monthmin100 < 0:
        monthmin100 += 525949
    if monthmin100 >= 525949:
        monthmin100 -= 525949

    i = so24month % 12 - 2
    if i == -2:
        i = 10
    if i == -1:
        i = 11

    inginame = i * 2
    midname = i * 2 + 1
    outginame = i * 2 + 2

    j = i * 2
    tmin = displ2min + (monthmin100 - montharray[j])
    y1, mo1, d1, h1, mi1 = getdatebymin(tmin, unityear, unitmonth, unitday, unithour, unithour)

    ingiyear = y1
    ingimonth = mo1
    ingiday = d1
    ingihour = h1
    ingimin = mi1

    tmin = displ2min + monthmin100 - montharray[j + 1]
    y1, mo1, d1, h1, mi1 = getdatebymin(tmin, unityear, unitmonth, unitday, unithour, unithour)

    midyear = y1
    midmonth = mo1
    midday = d1
    midhour = h1
    midmin = mi1

    tmin = displ2min + monthmin100 - montharray[j + 2]
    y1, mo1, d1, h1, mi1 = getdatebymin(tmin, unityear, unitmonth, unitday, unithour, unithour)

    outgiyear = y1
    outgimonth = mo1
    outgiday = d1
    outgihour = h1
    outgimin = mi1

    return inginame, ingiyear, ingimonth, ingiday, ingihour, ingimin,midname, midyear, midmonth, midday, midhour, midmin,outginame, outgiyear, outgimonth, outgiday, outgihour, outgimin


def degreelow(d: float) -> float:
    di = d
    i = int(di)
    i //= 360
    di -= (360 * i)

    while (di >= 360) or (di < 0):
        if di > 0:
            di -= 360
        else:
            di += 360
    return di


def moonsundegree(day: float) -> float:
    sl = day * 0.98564736 + 278.956807  # Average longitude
    smin = 282.869498 + 0.00004708 * day  # Perihelion longitude
    sminangle = 3.141592653589793 * (sl - smin) / 180  # Angle at perihelion
    sd = 1.919 * math.sin(sminangle) + 0.02 * math.sin(2 * sminangle)  # Longitude difference
    sreal = degreelow(sl + sd)  # True longitude

    ml = 27.836584 + 13.17639648 * day  # Average longitude
    mmin = 280.425774 + 0.11140356 * day  # Perigee longitude
    mminangle = 3.141592653589793 * (ml - mmin) / 180  # Angle at perigee
    msangle = 202.489407 - 0.05295377 * day  # Intersection longitude
    msdangle = 3.141592653589793 * (ml - msangle) / 180  # Angle at intersection
    md = (5.068889 * math.sin(mminangle) + 0.146111 * math.sin(2 * mminangle) + 0.01 * math.sin(3 * mminangle)
          - 0.238056 * math.sin(sminangle) - 0.087778 * math.sin(mminangle + sminangle)
          + 0.048889 * math.sin(mminangle - sminangle) - 0.129722 * math.sin(2 * msdangle)
          - 0.011111 * math.sin(2 * msdangle - mminangle) - 0.012778 * math.sin(2 * msdangle + mminangle))  # Longitude difference
    mreal = degreelow(ml + md)  # True longitude
    return degreelow(mreal - sreal)


def interpointdisp(day: float) -> float:
    sl = day * 0.98564736 + 278.956807  # Average longitude
    smin = 282.869498 + 0.00004708 * day  # Perihelion longitude
    sminangle = 3.141592653589793 * (sl - smin) / 180  # Angle at perihelion

    ml = 27.836584 + 13.17639648 * day  # Average longitude
    mmin = 280.425774 + 0.11140356 * day  # Perigee longitude
    mminangle = 3.141592653589793 * (ml - mmin) / 180  # Angle at perigee
    msangle = 202.489407 - 0.05295377 * day  # Intersection longitude
    msdangle = 3.141592653589793 * (ml - msangle) / 180  # Angle at intersection
    md = (5.068889 * math.sin(mminangle) + 0.146111 * math.sin(2 * mminangle) + 0.01 * math.sin(3 * mminangle)
          - 0.238056 * math.sin(sminangle) - 0.087778 * math.sin(mminangle + sminangle)
          + 0.048889 * math.sin(mminangle - sminangle) - 0.129722 * math.sin(2 * msdangle)
          - 0.011111 * math.sin(2 * msdangle - mminangle) - 0.012778 * math.sin(2 * msdangle + mminangle))  # Longitude difference
    mreal = degreelow(ml + md)  # True longitude

    ir = degreelow(mreal - msangle)
    if ir > 90:
        ir -= 180
    if ir > 90:
        ir -= 180
    return ir


def getlunarfirst(syear: int, smonth: int, sday: int):
    year, yearm, year1 = 0, 0, 0
    month, monthm, month1 = 0, 0, 0
    day, daym, day1 = 0, 0, 0
    hour, hourm, hour1 = 0, 0, 0
    min, minm, min1 = 0, 0, 0
    ip, ipm, ip1 = 0.0, 0.0, 0.0

    dm = disp2days(syear, smonth, sday, 1995, 12, 31)
    dem = moonsundegree(dm)

    d = dm
    de = dem

    while de > 13.5:
        d -= 1
        de = moonsundegree(d)

    while de > 1:
        d -= 0.04166666666
        de = moonsundegree(d)

    while de < 359.99:
        d -= 0.000694444
        de = moonsundegree(d)

    #print('d')
    #print(d)
    ip = interpointdisp(d)

    d += 0.375
    d *= 1440
    i = -1 * int(d)
    year, month, day, hour, min = getdatebymin(i, 1995, 12, 31, 0, 0)

    d = dm
    de = dem

    while de < 346.5:
        d += 1
        de = moonsundegree(d)

    while de < 359:
        d += 0.04166666666
        de = moonsundegree(d)

    while de > 0.01:
        d += 0.000694444
        de = moonsundegree(d)

    ip1 = interpointdisp(d)
    pd = d

    d += 0.375
    d *= 1440
    i = -1 * int(d)
    year1, month1, day1, hour1, min1 = getdatebymin(i, 1995, 12, 31, 0, 0)

    if (smonth == month1) and (sday == day1):
        year = year1
        month = month1
        day = day1
        hour = hour1
        min = min1

        d = pd
        ip = ip1

        while de < 347:
            d += 1
            de = moonsundegree(d)
        while de < 359:
            d += 0.04166666666
            de = moonsundegree(d)
        while de > 0.01:
            d += 0.000694444
            de = moonsundegree(d)
        ip1 = interpointdisp(d)

        d += 0.375
        d *= 1440
        i = -1 * int(d)
        year1, month1, day1, hour1, min1 = getdatebymin(i, 1995, 12, 31, 0, 0)

    d = disp2days(year, month, day, 1995, 12, 31)  # Lunar new moon
    d += 12  # Lunar 12th day
    de = moonsundegree(d)

    while de < 166.5:
        d += 1
        de = moonsundegree(d)

    while de < 179:
        d += 0.04166666666
        de = moonsundegree(d)

    while de < 179.99:
        d += 0.000694444
        de = moonsundegree(d)

    ipm = interpointdisp(d)

    d += 0.375
    d *= 1440
    i = -1 * int(d)
    yearm, monthm, daym, hourm, minm = getdatebymin(i, 1995, 12, 31, 0, 0)

    #print(year, month, day, hour, min, ip,yearm, monthm, daym, hourm, minm, ipm,year1, month1, day1, hour1, min1, ip1)
    return  year, month, day, hour, min, ip,yearm, monthm, daym, hourm, minm, ipm,year1, month1, day1, hour1, min1, ip1


def solortolunar(solyear: int, solmon: int, solday: int):
    s0 = 0  # Initialize with appropriate values
    lnp, lnp2 = False, False
    ingiyear, midyear1, midyear2, outgiyear = 0 ,0, 0 , 0
    inginame, ingimonth, ingiday, ingihour, ingimin = 0 ,0, 0 , 0, 0
    midname1, midmonth1, midday1, midhour1, midmin1 = 0 ,0, 0 , 0, 0
    midname2, midmonth2, midday2, midhour2, midmin2 = 0 ,0, 0 , 0, 0
    outginame, outgimonth, outgiday, outgihour, outgimin = 0 ,0, 0 , 0, 0
    smomonth, smoday, smohour, smomin =  0, 0, 0, 0
    smoyear, y0, y1 = 0, 0, 0
    mo0, d0, h0, mi0 =  0, 0, 0, 0
    mo1, d1, h1, mi1 =  0, 0, 0, 0
    ip, ip0, ip1 =  0, 0, 0

    #print(getlunarfirst(solyear, solmon, solday))
    smoyear, smomonth, smoday, smohour, smomin, ip, y0, mo0, d0, h0, mi0, ip0, y1, mo1, d1, h1, mi1, ip1 = getlunarfirst(solyear, solmon, solday)

    lday = disp2days(solyear, solmon, solday, smoyear, smomonth, smoday) + 1

    i = abs(disp2days(smoyear, smomonth, smoday, y1, mo1, d1))
    if i == 30:
        largemonth = True
    if i == 29:
        largemonth = False

    inginame, ingiyear, ingimonth, ingiday, ingihour, ingimin, midname1, midyear1, midmonth1, midday1, midhour1, midmin1, outginame, outgiyear, outgimonth, outgiday, outgihour, outgimin = solortoso24(smoyear, smomonth, smoday, smohour, smomin)

    midname2 = midname1 + 2
    if midname2 > 24:
        midname2 = 1
    s0 = montharray[midname2] - montharray[midname1]
    if s0 < 0:
        s0 += 525949
    s0 = -1 * s0

    midyear2, midmonth2, midday2, midhour2, midmin2 = getdatebymin(s0, midyear1, midmonth1, midday1, midhour1, midmin1)

    if ((midmonth1 == smomonth) and (midday1 >= smoday)) or \
       ((midmonth1 == mo1) and (midday1 < d1)):
        lmonth = (midname1 - 1) // 2 + 1
        lmoonyun = False
    else:
        if ((midmonth2 == mo1) and (midday2 < d1)) or \
           ((midmonth2 == smomonth) and (midday2 >= smoday)):
            lmonth = (midname2 - 1) // 2 + 1
            lmoonyun = False
        else:
            if (smomonth < midmonth2) and (midmonth2 < mo1):
                lmonth = (midname2 - 1) // 2 + 1
                lmoonyun = False
            else:
                lmonth = (midname1 - 1) // 2 + 1
                lmoonyun = True

    lyear = smoyear
    if (lmonth == 12) and (smomonth == 1):
        lyear -= 1

    if ((lmonth == 11) and lmoonyun) or (lmonth == 12) or (lmonth < 6):
        midyear1, midmonth1, midday1, midhour1, midmin1 = getdatebymin(2880, smoyear, smomonth, smoday, smohour, smomin)

        outgiyear, outgimonth, outgiday,lnp, lnp2 = solortolunar(midyear1, midmonth1, midday1)

        outgiday = lmonth - 1
        if outgiday == 0:
            outgiday = 12

        if outgiday == outgimonth:
            if lmoonyun:
                lmoonyun = False
        else:
            if lmoonyun:
                if lmonth != outgimonth:
                    lmonth -= 1
                    if lmonth == 0:
                        lyear -= 1
                    if lmonth == 0:
                        lmonth = 12
                    lmoonyun = False
            else:
                if lmonth == outgimonth:
                    lmoonyun = True
                else:
                    lmonth-= 1
                    if lmonth == 0:
                        lyear -= 1
                    if lmonth == 0:
                        lmonth = 12



    return lyear, lmonth, lday,lmoonyun, largemonth




import math


def get_weekday(syear: int, smonth: int, sday: int) -> int:
    # Assuming disp2days and unityear, unitmonth, unitday are defined elsewhere
    d = disp2days(syear, smonth, sday, unityear, unitmonth, unitday)
    i = d // 7
    d = d - (i * 7)

    while d > 6 or d < 0:
        if d > 6:
            d -= 7
        else:
            d += 7

    if d < 0:
        d += 7
    return d

def get_28sday(syear: int, smonth: int, sday: int) -> int:
    # Assuming disp2days and unityear, unitmonth, unitday are defined elsewhere
    d = disp2days(syear, smonth, sday, unityear, unitmonth, unitday)
    i = d // 28
    d = d - (i * 28)

    while d > 27 or d < 0:
        if d > 27:
            d -= 28
        else:
            d += 28

    d = d - 11
    if d < 0:
        d += 28
    return d

def get_julian_date(syear: int, smonth: int, sday: int) -> int:
    # Assuming disp2days is defined elsewhere
    d = disp2days(syear, smonth, sday, 1899, 12, 31)
    d = d + 2415020
    return d

def get_julian_date_point(syear: int, smonth: int, sday: int, shour: int, smin: int) -> float:
    # Assuming disp2days and getminbytime are defined elsewhere
    d = disp2days(syear, smonth, sday, 1899, 12, 31)
    d = d + 2415020
    tmin = getminbytime(syear, smonth, sday, shour, smin, syear, smonth, sday, 21, 0)
    df = d + (tmin // 1440) + ((tmin % 1440) / 1440)
    return df



def get_eightchar2(calendar,year, month, day, time):



    lyear, lmonth, lday, lmoonyun, largemonth = solortolunar(int(year), int(month), int(day))


    if calendar != '양력':
        year = lyear
        month = lmonth
        day = lday
    so24, so24year, so24month, so24day, so24hour = sydtoso24yd(int(year),int(month),int(day),int(time),30)
    new_data = {
        "Lunar": str(lyear)+'-'+str(lmonth)+'-'+str(lday),
        "Solar": str(year)+'-'+str(month)+'-'+str(day),
        "day_index" : so24day,
        "KorHeavenlyYearText": kor_ganji[so24year][0],
        "KorEarthlyYearText": kor_ganji[so24year][1],
        "ChiHeavenlyYearText": ganji[so24year][0],
        "ChiEarthlyYearText": ganji[so24year][1],

        "KorHeavenlyMonthText": kor_ganji[so24month][0],
        "KorEarthlyMonthText": kor_ganji[so24month][1],
        "ChiHeavenlyMonthText": ganji[so24month][0],
        "ChiEarthlyMonthText": ganji[so24month][1],

        "KorHeavenlyDayText": kor_ganji[so24day][0],
        "KorEarthlyDayText": kor_ganji[so24day][1],
        "ChiHeavenlyDayText": ganji[so24day][0],
        "ChiEarthlyDayText": ganji[so24day][1],

        "KorHeavenlyTimeText": kor_ganji[so24hour][0],
        "KorEarthlyTimeText": kor_ganji[so24hour][1],
        "ChiHeavenlyTimeText": ganji[so24hour][0],
        "ChiEarthlyTimeText": ganji[so24hour][1],

    }


    return new_data


#print(get_eightchar2('양력', '1981', '10' , '7', '00'))


'''
year, month, day, hour, minute = 1981, 10, 7, 6, 25
wd = getweekday(year,month,day)

s28 = get28sday(year,month,day)

lyear, lmonth, lday,lmoonyun, largemonth = solortolunar(year,month,day)
so24, so24year, so24month, so24day, so24hour = sydtoso24yd(year,month,day,23,25,)

inginame,ingiyear,ingimonth,ingiday,ingihour,ingimin,midname,midyear,midmonth,midday,midhour,midmin,outginame,outgiyear,outgimonth,outgiday,outgihour,outgimin = solortoso24(year,month,day,23,25)

print(f"양력 {year}년 {month}월 {day}일 {weekday[wd]}")
print(f"s28 -> {s28}")
print(f"음력 {lyear}년 {lmonth}월 {lday}일")


print(f"이번달 절입 : {monthst[inginame]} 양력 + {ingiyear}년 {ingimonth}월 {ingiday}일 {ingihour}시 {ingimin} 분")
print(f"이번달 중기 : {monthst[midname]} 양력 + {midyear}년 {midmonth}월 {midday}일 {midhour}시 {midmin} 분")
print(f"다음달 절입 : {monthst[outginame]} 양력 + {outgiyear}년 {outgimonth}월 {outgiday}일 {outgihour}시 {outgimin} 분")

'''


#year, month, day, hour, minute = 2024, 11, 1, 6, 25
#so24, so24year, so24month, so24day, so24hour = sydtoso24yd(year,month,day,23,25,)

#print(so24day)

#print(f"간지  {ganji[so24year]}년 {ganji[so24month]}월 {ganji[so24day]}일")

