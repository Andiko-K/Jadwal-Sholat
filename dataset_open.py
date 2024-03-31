import csv, requests
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
        city = row['region']
        latitude = row['latitude']; longitude = row['longitude']
        altitude = row['altitude']; timezone = row['timezone']

        if city not in city_loc_dict:
            city_loc_dict[city] = {'latitude': latitude, 'longitude': longitude,
                                    'altitude': altitude, 'timezone': timezone}
    data.close()
    return city_loc_dict


def get_cities(city_loc_dict):
    return [key for key in city_loc_dict.keys()]

def get_value(city, city_loc_dict):
    return city_loc_dict[city]

### Metode untuk mendapatkan lokasi pengguna melalui IP Address

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f"https://freeipapi.com/api/json/{ip_address}").json()
    city = response.get("cityName")
    province = response.get("regionName")

    user_data ={'city': city.upper(), 'province': province.upper()}
    return user_data