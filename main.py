import customtkinter as CTT
from PIL import Image
import utils_prayer, utils_main

today = utils_prayer.get_today()
today_hijri = utils_prayer.Greg_to_Hij(today)
date_text = utils_main.date_string(today, today_hijri)


#GUI Program
app = CTT.CTk()
app.title('Jadwal Sholat')
app.geometry('1036x605')
app.resizable(0,0)
CTT.set_appearance_mode('light')

#main-frame
main_frame = CTT.CTkFrame(master = app, fg_color="#FFFFFF", width = 1036,
                          height = 645)
main_frame.pack(fill = 'both', expand = True)

#header
header = CTT.CTkFrame(master = main_frame, fg_color="#304674", width = 1036,
                      height = 186, corner_radius=0)
header.place(x = 0, y = 0)
header_label = CTT.CTkLabel(master = main_frame, fg_color = '#304674', text = 'JADWAL SHOLAT',
                           width=487, height = 24, bg_color='#304674', justify = 'center',
                           font = ('Montserrat', 40, 'bold'), text_color = '#FFFFFF')
header_label.place(x=274, y =19)
header_date = CTT.CTkLabel(master = main_frame, fg_color='#304674', width=487, height = 24,
                           text = date_text, font = ('Montserrat', 20), text_color='#FFFFFF',
                           bg_color='#304674', justify = 'center')
header_date.place(x = 274, y = 68)

#sholat_frame
sholat_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D6E4F6', width = 769,
                            height = 154, corner_radius=0)
sholat_frame.place(x=133, y = 117)

#parameter_frame
param_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 122, corner_radius=15)
param_frame.place(x=759, y = 291)

#fiqih_frame
fiqih_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 163, corner_radius=15)
fiqih_frame.place(x=759, y = 433)

#tabel_frame
tabel_frame = CTT.CTkFrame(master = main_frame, fg_color = '#B2CBDE', width = 730,
                           height = 302, corner_radius=15)
tabel_frame.place(x=14, y = 291)
app.mainloop()