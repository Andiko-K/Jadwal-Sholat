import csv
def open_data(link = './dataset/dataset_region.csv') -> dict[str, float]:
    '''
    Mempersiapkan data dari dataset_region.csv yang berisi provinsi, kota, dan properti lain
    supaya dapat digunakan pada program
    Input:
        link (string)
    Output:
        city_loc_dict (dictionary)
    '''
    data =  open(link, 'r')
    city_loc = csv.DictReader(data)

    city_loc_dict = {}
    for row in city_loc:
        province = row['province']; city = row['region']
        latitude = row['latitude']; longitude = row['longitude']
        altitude = row['altitude']; timezone = row['timezone']

        if province not in city_loc_dict:
            city_loc_dict[province] = {}
            city_loc_dict[province][city] = {'latitude': latitude, 'longitude': longitude,
                                    'altitude': altitude, 'timezone': timezone}
    data.close()
    return city_loc_dict

def get_provinces(city_loc_dict):
    return [key for key in city_loc_dict.keys()]

def get_cities(province, city_loc_dict):
    return [key for key in city_loc_dict[province].keys()]

def get_value(province, city, city_loc_dict):
    return city_loc_dict[province][city]