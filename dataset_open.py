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
    region = csv.DictReader(data)

    region_dict = {}
    for row in region:
        province = row['province']; city = row['region']
        latitude = row['latitude']; longitude = row['longitude']
        altitude = row['altitude']; timezone = row['timezone']

        if province not in region_dict:
            region_dict[province] = {}
        
        region_dict[province][city] = {'latitude': latitude, 'longitude': longitude,
                                'altitude': altitude, 'timezone': timezone}
    data.close()
    return region_dict


def get_provinces(data: dict[str, float]) -> list[str]:
    '''
    Mendapatkan list provinsi dari dataset yang diberikan
    Input:
        data (dict), didapatkan dari open_data()
    Output:
        province_list
    '''
    provinces_list = [key for key in data.keys()]
    return provinces_list

dataset = open_data()
provinces = get_provinces(dataset)

def get_cities(province: str, data : dict[str, float] = dataset) -> list[str]:
    '''
    Mendapatkan list kota dari provinsi dan dataset yang diberikan
    Input:
        data (dict), didapatkan dari open_data(), province_list
    Output:
        city_list
    '''
    try:
        city_list = [key for key in data[province].keys()]
    except:
        city_list = []
    return city_list

def get_value(province: str, city: str, data: dict[str, float] = dataset) -> dict[str, float]:
    '''
    Mendapatkan value (lat, long, alt, dan tz) dari suatu daerah
    berdasarkan kota dan provinsi
    Input:
        province: str(nama provinsi)
        city: str(nama kota)
        data (dict)
    Output:
        value
    '''
    value = data[province][city]
    return value