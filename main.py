import customtkinter as CTT
from PIL import Image
import utils_main, dataset_open
from ctk_scrollable_dropdown.ctk_scrollable_dropdown import *

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
                           text = utils_main.date_text, font = ('Montserrat', 20), text_color='#FFFFFF',
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
coordinate = "7°59' LS 112°45' BT"
altitude = 445
timezone = 7
param_coordinate = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8',
                        text = f"Koordinat: {coordinate}", anchor = 'w').place(x=765.52, y = 330)
param_altitude = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8',
                        text = f"Ketinggian: {altitude} MDPL", anchor = 'w').place(x=765.52, y = 357 )
timezone = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 247.95, height = 12.99,
                        text_color = '#000000', font = ('Montserrat', 13), bg_color= '#D8E1E8',
                        text = f'Zona Waktu: GMT+0{timezone}', anchor = 'w').place(x=765.52, y = 385)
#fiqih_frame
fiqih_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 163, corner_radius=15)
fiqih_frame.place(x=759, y = 433)
fiqih_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', width = 163.12, height = 30.32,
                        text_color = '#000000', font = ('Montserrat', 15, 'underline'), bg_color= '#D8E1E8',
                        text = 'Ketetapan Fiqih').place(x=811.2, y = 440.26)

koreksi_dhuhur_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Koreksi Waktu Dhuhur:', font = ('Montserrat', 12)).place(x = 764, y = 467)
koreksi_dhuhur_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8', width = 50,
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
koreksi_dhuhur_option.set('10')
koreksi_dhuhur_option.place(x = 967, y = 467)

bayangan_ashar_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Tetapan Ashar:', font = ('Montserrat', 12)).place(x = 764, y = 497)
bayangan_ashar_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8', width = 50,
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
bayangan_ashar_option.set("Syafi'i(+1)")
bayangan_ashar_option.place(x = 929, y = 497)

ketinggian_shubuh_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Ketinggian Shubuh:', font = ('Montserrat', 12)).place(x = 764, y = 527)
ketinggian_shubuh_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8', width = 50,
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
ketinggian_shubuh_option.set("18°")
ketinggian_shubuh_option.place(x = 962, y = 527)

ketinggian_isya_text = CTT.CTkLabel(master = main_frame, fg_color = '#D8E1E8', text_color = '#000000', bg_color = '#D8E1E8',
                            text = 'Ketinggian Isya:', font = ('Montserrat', 13)).place(x = 764, y = 557)
ketinggian_isya_option = CTT.CTkOptionMenu(master = main_frame, fg_color = '#D8E1E8', button_color='#D8E1E8', width = 50,
                                     font = ('Montserrat', 12), dropdown_font=('Montserrat', 10), 
                                    corner_radius= 0, bg_color='#D6E4F6', text_color='#000000', anchor = 'e')
ketinggian_isya_option.set("18°")
ketinggian_isya_option.place(x = 962, y = 557)

#tabel_frame
tabel_frame = CTT.CTkFrame(master = main_frame, fg_color = '#B2CBDE', width = 730,
                           height = 302, corner_radius=15)
tabel_frame.place(x=14, y = 291)

#dropdown
def kota_dropdown_func(x):
    provinsi_option.set(x)
    kota_dropdown = CTkScrollableDropdown(kota_option, values = dataset_open.get_cities(x))

provinsi_dropdown = CTkScrollableDropdown(provinsi_option, values=dataset_open.get_provinces(), command = kota_dropdown_func)
app.mainloop()