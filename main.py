import customtkinter as CTT
from PIL import Image
import utils_main, utils_prayer #perlu update, gabungkan utils_main dengan fungsi lain
from ctk_scrollable_dropdown.ctk_scrollable_dropdown import *
import CTkTable
"""GUI Program"""
app = CTT.CTk()
app.title('Jadwal Sholat')
app.geometry('1036x605')
app.resizable(0,0)
CTT.set_appearance_mode('light')

#main-frame------------------------------------------------------------------------------------------------------------------------------
main_frame = CTT.CTkFrame(master = app, fg_color="#FFFFFF", width = 1036,
                          height = 645)
main_frame.pack(fill = 'both', expand = True)

#header----------------------------------------------------------------------------------------------------------------------------------
header = CTT.CTkFrame(master = main_frame, fg_color="#304674", width = 1036,
                      height = 186, corner_radius=0)
header.place(x = 0, y = 0)
header_label = CTT.CTkLabel(master = main_frame, fg_color = '#304674', text = 'JADWAL SHOLAT',
                           width=487, height = 24, bg_color='#304674', justify = 'center',
                           font = ('Montserrat', 40, 'bold'), text_color = '#FFFFFF')
header_label.place(x=274, y =19)
header_date = CTT.CTkLabel(master = main_frame, fg_color='#304674', width=487, height = 24,
                           text = '', font = ('Montserrat', 20), text_color='#FFFFFF',
                           bg_color='#304674', justify = 'center')
header_date.place(x = 274, y = 68)

#sholat_frame----------------------------------------------------------------------------------------------------------------------------
sholat_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D6E4F6', width = 769,
                            height = 154, corner_radius=0)
sholat_frame.place(x=133, y = 117)

##setting lokasi-------------------------------------------------------------------------------------------------------------------------
provinsi_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6',
                              font = ('Montserrat', 15), text = 'Provinsi: ', bg_color='#D6E4F6')
provinsi_label.place(x=160, y = 135)
provinsi_option =  CTT.CTkOptionMenu(master = main_frame, fg_color = '#D6E4F6', button_color='#D6E4F6', width = 265,
                                     height = 24, font = ('Montserrat', 15), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000')
provinsi_option.set(' ')
provinsi_option.place(x=220, y = 137)

kota_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6',
                              font = ('Montserrat', 15), text = 'Daerah: ', bg_color='#D6E4F6')
kota_label.place(x=495, y = 135)
kota_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D6E4F6', button_color='#D6E4F6', width = 340,
                                     height = 24, font = ('Montserrat', 15), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000')
kota_option.set(' ')
kota_option.place(x=550, y = 137)

##jadwal sholat (main)-------------------------------------------------------------------------------------------------------------------
subuh_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 70.34, height = 21,
                              font = ('Montserrat', 15), text = 'Subuh', bg_color='#D6E4F6').place(x = 152.93, y = 184)
subuh_time = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 70.34, height = 24,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
subuh_time.place(x = 152.93, y = 224)

terbit_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 63.3, height = 21,
                              font = ('Montserrat', 15), text = 'Terbit', bg_color='#D6E4F6').place(x = 285.39, y = 184)
terbit_time = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 63.3, height = 21,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
terbit_time.place(x = 285.39, y = 224)

dhuhur_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 83.23, height = 21,
                              font = ('Montserrat', 15), text = 'Dhuhur', bg_color='#D6E4F6').place(x = 410.82, y = 184)
dhuhur_time = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 83.23, height = 21,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
dhuhur_time.place(x = 410.82, y = 224)

ashar_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 62.13, height = 21,
                              font = ('Montserrat', 15), text = 'Ashar', bg_color='#D6E4F6').place(x = 556.18, y = 184)
ashar_time = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 62.13, height = 21,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
ashar_time.place(x = 556.18, y = 224)

maghrib_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 91.44, height = 21,
                              font = ('Montserrat', 15), text = 'Maghrib', bg_color='#D6E4F6').place(x = 680.44, y = 184)
maghrib_time= CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 91.44, height = 21,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
maghrib_time.place(x = 680.44, y = 224)

isya_label = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 41.03, height = 21,
                              font = ('Montserrat', 15), text = 'Isya', bg_color='#D6E4F6').place(x = 824.01, y = 184)
isya_time = CTT.CTkLabel(master = main_frame, text_color = '#000000', fg_color='#D6E4F6', width = 41.03, height = 21,
                              font = ('Montserrat', 15), text = '23:59', bg_color='#D6E4F6')
isya_time.place(x = 824.01, y = 224)

## line----------------------------------------------------------------------------------------------------------------------------------
horizontal_line = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 693.98,
                               height=1)
horizontal_line.place(x = 177.55, y = 168)
vertical = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 1,
                               height=77)
vertical1 = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 1,
                               height=77)
vertical2 = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 1,
                               height=77)
vertical3 = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 1,
                               height=77)
vertical4 = CTT.CTkFrame(master = main_frame, bg_color = '#000000', width = 1,
                               height=77)
vertical.place(x=241.71, y = 181)
vertical1.place(x=378.86, y = 181)
vertical2.place(x=517.19, y = 181)
vertical3.place(x=793.84, y = 181)
vertical4.place(x=655.52, y = 181)

#parameter_frame------------------------------------------------------------------------------------------------------------------------
param_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 122, corner_radius=15)
param_frame.place(x=759, y = 291)

param_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 163.12, height = 30.32,
                        text_color = '#000000', font = ('Montserrat', 15, 'underline'), bg_color= '#D8E1E8',
                        text = 'Parameter Posisi').place(x=811.2, y = 295.91)

param_coordinate = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8', anchor = 'w')
param_coordinate.place(x=765.52, y = 330)
param_altitude = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8', anchor = 'w')
param_altitude.place(x=765.52, y = 357 )
param_timezone = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8', anchor = 'w')
param_timezone.place(x=765.52, y = 385)
#fiqih_frame-----------------------------------------------------------------------------------------------------------------------------
fiqih_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 163, corner_radius=15)
fiqih_frame.place(x=759, y = 433)
fiqih_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 163.12, height = 30.32,
                        text_color = '#000000', font = ('Montserrat', 15, 'underline'), bg_color= '#D8E1E8',
                        text = 'Ketetapan Fiqih').place(x=811.2, y = 440.26)

koreksi_dhuhur_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Koreksi Waktu Dhuhur:', font = ('Montserrat', 12)).place(x = 764, y = 467)
koreksi_dhuhur_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8',
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 9), width = 120,
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
koreksi_dhuhur_option.set('10')
koreksi_dhuhur_option.place(x = 890, y = 467)

bayangan_ashar_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Tetapan Ashar:', font = ('Montserrat', 12)).place(x = 764, y = 497)
bayangan_ashar_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8',
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 10), width = 140,
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
bayangan_ashar_option.set("Syafi'i(+1)")
bayangan_ashar_option.place(x = 870, y = 497)

ketinggian_shubuh_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Ketinggian Shubuh:', font = ('Montserrat', 12)).place(x = 764, y = 527)
ketinggian_shubuh_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8',
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 9), width = 120,
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
ketinggian_shubuh_option.set("18")
ketinggian_shubuh_option.place(x = 890, y = 527)

ketinggian_isya_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Ketinggian Isya:', font = ('Montserrat', 13)).place(x = 764, y = 557)
ketinggian_isya_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8',
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 9), width = 120,
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
ketinggian_isya_option.set("18")
ketinggian_isya_option.place(x = 890, y = 557)

#tabel_frame-----------------------------------------------------------------------------------------------------------------------------
tabel_frame = CTT.CTkFrame(master = main_frame, fg_color = '#B2CBDE', width = 730,
                           height = 302, corner_radius=15)
tabel_frame.place(x=14, y = 291)

year_text = CTT.CTkEntry(master = main_frame, fg_color='#FFFFFF', bg_color = '#B2CBDE', font=('Montserrat',12),border_width=0,
                         width = 120, height = 25, text_color = '#000000', corner_radius=5, justify = 'center')
year_text.place(x=30, y =302)
month_text = CTT.CTkOptionMenu(master = main_frame, fg_color = '#FFFFFF', bg_color = '#B2CBDE',button_color='#FFFFFF',
                               font = ('Montserrat', 12), dropdown_font=('Montserrat', 11), width = 125, height=25,
                               text_color='#000000', anchor = 'center')
month_text.place(x=160, y = 302)

day_text = CTT.CTkOptionMenu(master = main_frame, fg_color = '#FFFFFF', bg_color = '#B2CBDE',button_color='#FFFFFF',
                               font = ('Montserrat', 12), dropdown_font=('Montserrat', 11), width = 120, height=25,
                               text_color='#000000', anchor = 'center')
day_text.place(x=290, y = 302)
day_text.set('30')

enter_button = CTT.CTkButton(master = main_frame, fg_color = '#304674', bg_color = '#B2CBDE', font = ('Montserrat', 12),
                             width = 58.24, height = 25, text_color = '#FFFFFF', text = 'Enter')
enter_button.place(x = 420, y = 302)

refresh_image = CTT.CTkImage(light_image=Image.open('./image/refresh.png'), size=(15,15))
refresh_button = CTT.CTkButton(master = main_frame, width = 15, height = 15, text = '', bg_color = '#B2CBDE', 
                               fg_color = '#0A2472', image = refresh_image)
refresh_button.place(x = 703, y = 298)

table_frame = CTT.CTkScrollableFrame(master = main_frame,fg_color = '#B2CBDE',
                                     bg_color = '#B2CBDE', width = 698, height = 239)
table_frame.place(x = 20, y = 330)

table_data0 = [['', '', '', '', '', '', ''] for i in range (1,32)]
table = CTkTable.CTkTable(master = table_frame, colors = ['#98BAD5', '#C6D3E3'], header_color='#506288', values=table_data0)
table.pack(expand = True)
#update value--------------------------------------------------------------------------------------------------------------------------------
def get_waktu_sholat():
    pos = utils_main.position_parameter(provinsi_option.get(), kota_option.get())
    JD = utils_prayer.Greg_to_JD(utils_main.date_greg)
    const = {'KA': utils_prayer.bayangan_ashar[bayangan_ashar_option.get()], 'h_isya': ketinggian_isya_option.get(),
             'h_subuh': ketinggian_shubuh_option.get(), 'koreksi': koreksi_dhuhur_option.get()}
    waktu_sholat = utils_prayer.prayer_time(pos = pos, JD = JD, const = const)
    waktu_sholat = waktu_sholat.prayer()

    subuh_time.configure(text = waktu_sholat['subuh'])
    terbit_time.configure(text = waktu_sholat['terbit'])
    dhuhur_time.configure(text = waktu_sholat['dhuhur'])
    ashar_time.configure(text = waktu_sholat['ashar'])
    maghrib_time.configure(text = waktu_sholat['maghrib'])
    isya_time.configure(text = waktu_sholat['isya'])

    refresh_button.configure(fg_color = '#7E2020')


def fill_table():
    pos = utils_main.position_parameter(provinsi_option.get(), kota_option.get())
    const = {'KA': utils_prayer.bayangan_ashar[bayangan_ashar_option.get()], 'h_isya': ketinggian_isya_option.get(),
             'h_subuh': ketinggian_shubuh_option.get(), 'koreksi': koreksi_dhuhur_option.get()}
    date = utils_main.date_greg
    table_data = utils_prayer.prayer_table(date, pos, const)
    table.configure(values = table_data)
    day = date['day']
    refresh_button.configure(fg_color = '#0A2472')
    table.edit_row(day, text_color="#E30909")

    

def kota_dropdown_command(city):
    kota_option.set(city)
    kota = kota_option.get()
    provinsi = provinsi_option.get()

    parameter_posisi = utils_main.position_parameter(provinsi, kota)

    param_coordinate.configure(text = f"Koordinat: {float(parameter_posisi['latitude']):.3f},{float(parameter_posisi['longitude']):.3f} ")
    param_altitude.configure(text = f"Ketinggian: {parameter_posisi['altitude']} MDPL")
    param_timezone.configure(text = f"Zona Waktu: GMT+0{parameter_posisi['timezone']}")
    get_waktu_sholat()


def provinsi_dropdown_command(province):
    provinsi_option.set(province)
    kota_option.set(' ')
    provinsi = provinsi_option.get()

    kota_dropdown = CTkScrollableDropdown(kota_option, values = utils_main.cities(provinsi), command = kota_dropdown_command)

def month_dropdown_command(month):
    month_text.set(month)
    year = {'year': year_text.get()}
    utils_prayer.greg_month = utils_prayer.leap_greg(year)
    day_in_months = utils_prayer.greg_month[month]
    day_dropdown = CTkScrollableDropdown(day_text, values = [i for i in range(1,day_in_months+1)],
                                         command = lambda x: day_text.set(x))

def enter_command():
    utils_main.date_greg['day'] = int(day_text.get())
    utils_main.date_greg['month_name'] = month_text.get()
    utils_main.date_greg['year'] = int(year_text.get())
    month_num = int([i for i in utils_prayer.greg_month.keys()].index(month_text.get()))+1
    utils_main.date_greg['month'] = month_num
    utils_main.date_hijri = utils_prayer.Greg_to_Hij(utils_main.date_greg)
    utils_main.date_text = utils_main.date_string(utils_main.date_greg, utils_main.date_hijri)

    header_date.configure(text = utils_main.date_text)
    get_waktu_sholat()

def refresh_button_command():
    fill_table()

def koreksi_dhuhur_dropdown_command(x):
    koreksi_dhuhur_option.set(x)
    get_waktu_sholat()
def bayangan_ashar_dropdown_command(x):
    bayangan_ashar_option.set(x)
    get_waktu_sholat()
def ketinggian_shubuh_dropdown_command(x):
    ketinggian_shubuh_option.set(x)
    get_waktu_sholat()
def ketinggian_isya_dropdown_command(x):
    ketinggian_isya_option.set(x)
    get_waktu_sholat()

provinsi_dropdown = CTkScrollableDropdown(provinsi_option, values=utils_main.provinces, command = provinsi_dropdown_command)

koreksi_dhuhur_dropdown = CTkScrollableDropdown(koreksi_dhuhur_option, values = utils_prayer.koreksi_dhuhur,
                                                command = koreksi_dhuhur_dropdown_command)
bayangan_ashar_dropdown = CTkScrollableDropdown(bayangan_ashar_option, values = utils_prayer.bayangan_ashar,
                                                command = bayangan_ashar_dropdown_command)
ketinggian_shubuh_dropdown = CTkScrollableDropdown(ketinggian_shubuh_option, values=utils_prayer.ketinggian_shubuh,
                                                   command = ketinggian_shubuh_dropdown_command)
ketinggian_isya_dropdown = CTkScrollableDropdown(ketinggian_isya_option, values = utils_prayer.ketinggian_isya,
                                                 command = ketinggian_isya_dropdown_command)

month_dropdown = CTkScrollableDropdown(month_text, values = [i for i in utils_prayer.greg_month.keys()], command = month_dropdown_command)
enter_button.configure(command = enter_command)
refresh_button.configure(command = refresh_button_command)
#initial value--------------------------------------------------------------------------------------------------------------------------
header_date.configure(text = utils_main.date_text)

day_text.set(utils_main.date_greg['day'])
year_text.insert(0,str(utils_main.date_greg['year']))
month_dropdown_command(utils_main.date_greg['month_name'])

provinsi_dropdown_command('DKI JAKARTA')
kota_dropdown_command('KOTA JAKARTA PUSAT')
fill_table()

app.mainloop()