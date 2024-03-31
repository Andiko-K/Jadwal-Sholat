

#Fungsi untuk parsing tanggal menjadi string pada main.py
def date_string(date_greg, date_hijri):
    str_greg = f"{date_greg['day']} {date_greg['month_name']} {date_greg['year']}"
    str_hijr = f"{int(date_hijri['day'])} {date_hijri['month']} {date_hijri['year']}"
    str_full = " / ".join([str_greg, str_hijr])
    return str_full