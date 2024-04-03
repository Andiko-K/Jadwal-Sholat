from datetime import datetime
from math import *
import copy

#Dictionary dan list untuk bulan dan tanggal tiap jenis penanggalan
greg_month = { 'Januari': 31, 'Februari': 28, 'Maret': 31, 'April': 30, 'Mei': 31, 'Juni': 30,
                'Juli': 31, 'Agustus': 31, 'September': 30, 'Oktober': 31, 'November': 30, 'Desember': 31}

hijri_month = { 'Muharram': 30, 'Safar': 29, 'Rabiul Awal': 30, 'Rabiul Akhir': 29, 'Jumadil Awal': 30, 'Jumadil Akhir': 29,
                          'Rajab': 30, 'Syaban': 29, 'Ramadhan': 30, 'Syawal': 30, 'Zulkaidah': 29, 'Zulhijah': 29}

#Nilai sisa bagi di mana tahun Hijriyah berupa kabisat
hijri_leap = [2,5,7,10,13,16,18,21,24,26,29]

#Nilai konstanta
koreksi_dhuhur = [i for i in range(-10, 11)]
bayangan_ashar = {"Syafi'i(+1)": 1, 'Hanafi(+2)':2}
ketinggian_shubuh = [15,16,17.7,18,19.5,20]
ketinggian_isya = [14,15,17.5,18]

#Cek tahun kabisat pada Penanggalan Masehi dan Hijriyah
def leap_greg(date: dict[str, int]) -> dict[str, int]:
    '''
    Mengecek apakah tahun input berupa kabisat
    input:
        date : dictionary berisi {day, month, year} dalam masehi
    output:
        greg_month
    '''
    year = int(date['year'])
    is_leap_year = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
                
    if is_leap_year:
        greg_month['Februari'] = 29
    else:
        greg_month['Februari'] = 28

    return greg_month

def leap_hijri(date: dict[str, int]) -> dict[str, int]:
    '''
    Mengecek apakah tahun input berupa kabisat
    input:
        date : dictionary berisi {day, month, year} dalam hijriyah
    output:
        hijri_month
    '''
    year = int(date['year'])
    is_leap_year = year%30
                
    if is_leap_year in hijri_leap:
        hijri_month['Zulhijah'] = 30
    else:
        hijri_month['Zulhijah'] = 29

    return hijri_month

def Greg_to_JD(date: dict[str, int]) -> float:
    '''
    Konversi penanggalan Gregorian menuju JD
    input:
        date : dictionary berisi {day, month, year} dalam masehi
    output:
        JD (float)
    '''
    day,month,year = int(date['day']), int(date['month']), int(date['year'])
    if month < 3:
        month += 12; year -= 1
    alpha = int(year/100)
    alpha = 2 + int(alpha/4)-alpha

    JD = 1720995 + int(365.25*year) + int(30.6001*(month+1))+alpha+day
    return JD

def Hij_to_JD(date: dict[str, int]) -> float:
    '''
    Konversi penanggalan Hijriyah menuju JD
    input:
        date : dictionary berisi {day, month, year} dalam masehi
    output:
        JD (float)
    '''
    day,month,year = int(date['day']), int(date['month']), int(date['year'])
    sum_of_Hij = 30*354+11
    JD = int(year/30)*sum_of_Hij + 1948438.5
    residue = year%30

    for i in range(len(hijri_leap)):
        if residue > hijri_leap[i]:
            JD += 355
        else:
            JD += ((residue - hijri_leap[i-1])*354)

    for i in enumerate(hijri_month.items()):
        if month > (i[0]+1):
            JD += i[1][1] 
    JD+=(day+.5)
    return JD

def Greg_to_Hij(date: dict[str, int]) -> dict[str, int]:
    JD = Greg_to_JD(date) -1.5
    sum_of_Hij = 30*354+11
    JD_Hij = JD - 1948438.5 #JD dimulai dari 0 Muharram 1 H

    year = 30*int(JD_Hij/sum_of_Hij)
    leap_residue = JD_Hij%sum_of_Hij 
    #sisa tanggal yang tidak terbagi pada year sebagai residue pembagian
    #menyatakan bahwa residue belum mengalami satu putaran 30 tahun penuh
    year_residue = int(leap_residue/354)
    year += year_residue+1 

    day = leap_residue%354

    for i in enumerate(hijri_leap):
        if year_residue > i[1]:
            day -= 1
    for m in hijri_month:
        if day <= hijri_month[m]:
            month = m
            break
        else:
            day -= hijri_month[m]
    hijri_dict = {'day': day, 'month': month, 'year': year}
    return hijri_dict
    

#Fungsi untuk mendapatkan tanggal saat ini
def get_today():
    dt = datetime.now()
    date = [int(i) for i in dt.strftime('%d %m %Y %H %M').split(' ')]
    greg_month_name = [month for month in greg_month.keys()]
    date_dict = {'day': date[0], 'month': date[1],
                 'month_name': greg_month_name[date[1]-1],'year': date[2]}
    return date_dict

#Algoritma untuk waktu sholat
class prayer_time:
    def __init__(self, pos: dict[str, float], JD: float, const: dict[str, int]):
        self.lat = float(pos['latitude'])
        self.long = float(pos['longitude'])
        self.alt = float(pos['altitude'])
        self.zona = float(pos['timezone'])

        self.JD_zona = JD - self.zona/24

        self.KA = float(const['KA'])
        self.h_isya = float(const['h_isya'])
        self.h_subuh = float(const['h_subuh'])
        self.cor = float(const['koreksi'])

    def acot(self, x):
        return atan(1/x)
    
    def time_angle(self, JD):
        T = 2*pi*(JD-245145)/365.25
        return T
    
    def sun_declination(self, time_angle, JD):
        T = time_angle(JD)
        delta = (0.37877+23.264*sin((radians(57.297*T-79.547))) +
                0.3812*sin((radians(57.297*2*T-82.682)))+
                0.17132*sin((radians(57.297*3*T-59.722))))
        return delta
    
    def equation_of_time(self, JD):
        U = (JD-245145)/36525
        L0 = 280.46607+36000.7698*U #mean latitude of the sun

        ET = (-(1789+237*U)*sin(radians(L0))-(7146-62*U)*cos(radians(L0))
                +(9934-14*U)*sin(2*radians(L0))-(29+5*U)*cos(2*radians(L0))
                +(74+10*U)*sin(3*radians(L0))+(320-4*U)*cos(3*radians(L0))
                -212*sin(4*radians(L0)))/1000
        return ET
    
    def hour_angle(self, delta, h, lat):
        x = (sin(radians(h))-sin(radians(lat))*sin(radians(delta)))/(cos(radians(lat))*cos(radians(delta)))
        return degrees(acos(x))
    
    def prayer(self):
        ET = self.equation_of_time(self.JD_zona)
        delta = self.sun_declination(self.time_angle, self.JD_zona)
        transit = 12+self.zona-self.long/15-ET/60

        ashar_alt = self.KA + tan(abs(delta-self.lat)/(180/pi))
        h_ashar = (180/pi)*self.acot(ashar_alt)
        h_maghrib = -0.83333-0.0347*sqrt(self.alt)

        subuh_time = transit - self.hour_angle(delta, -1*self.h_subuh, self.lat)/15
        rise_time = transit - self.hour_angle(delta, h_maghrib, self.lat)/15
        dhuhur_time = transit
        ashar_time = transit + self.hour_angle(delta, h_ashar, self.lat)/15
        maghrib_time = transit + self.hour_angle(delta, h_maghrib, self.lat)/15
        isya_time = transit + self.hour_angle(delta, -1*self.h_isya, self.lat)/15

        sholat = {
            'subuh': f'{int(subuh_time):02d}:{int(subuh_time%1*60):02d}',
            'terbit': f'{int(rise_time):02d}:{int(rise_time%1*60):02d}',
            'dhuhur': f'{int(dhuhur_time):02d}:{int(dhuhur_time%1*60 + self.cor):02d}',
            'ashar': f'{int(ashar_time):02d}:{int(ashar_time%1*60):02d}',
            'maghrib': f'{int(maghrib_time):02d}:{int(maghrib_time%1*60):02d}',
            'isya': f'{int(isya_time):02d}:{int(isya_time%1*60):02d}'
        }
        return sholat

def prayer_table(date: dict[str, float], pos: dict[str, float], const: dict[str, int]):
    table = [['Tgl. Masehi', 'Subuh', 'Terbit', 'Dhuhur', 'Ashar', 'Maghrib', 'Isya']]
    date_copy = copy.deepcopy(date)
    date_in_month = greg_month[date_copy['month_name']]
    for day in range(1, date_in_month+1):
        date_copy['day'] = day
        date_masehi_str = f"{day}/{date['month']}/{date['year']}"

        JD = Greg_to_JD(date_copy)
        time = prayer_time(pos, JD, const)
        time = time.prayer()
        subuh = time['subuh']; terbit = time['terbit']; dhuhur = time['dhuhur']
        ashar = time['ashar']; maghrib = time['maghrib']; isya = time['isya']

        table.append([date_masehi_str, subuh, terbit, dhuhur, ashar, maghrib,
                      isya])
    return table
