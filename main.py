import customtkinter as CTT
from PIL import Image

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

#sholat_frame
sholat_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D6E4F6', width = 769,
                            height = 154, corner_radius=0)
sholat_frame.place(x=111, y = 117)

#parameter_frame
param_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 122, corner_radius=15)
param_frame.place(x=759, y = 29)

#fiqih_frame
fiqih_frame = CTT.CTkFrame(master = main_frame, fg_color = '#D8E1E8', width = 261,
                           height = 163, corner_radius=15)
fiqih_frame.place(x=759, y = 433)

#tabel_frame
tabel_frame = CTT.CTkFrame(master = main_frame, fg_color = '#B2CBDE', width = 730,
                           height = 302, corner_radius=15)
tabel_frame.place(x=14, y = 291)
app.mainloop()