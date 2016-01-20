import requests


def reverse_string(word_string):
    if word_string == "":
        return word_string
    if isinstance(word_string, str):
        reverse_data = ','.join(reversed(word_string.split(',')))
        print(reverse_data)
        return reverse_data
    else:
        print("The input type is %s, not string" % type(word_string))
        return None


if __name__ == '__main__':
    target_latitude = 25.126743
    target_longitude = 121.503891

    data_format = "json"

    target_url = "http://nominatim.openstreetmap.org/reverse?format=%s&lat=%s&lon=%s&zoom=18&addressdetails=1" % (
        data_format, target_latitude, target_longitude)

    r = requests.get(target_url)

    data_dict = r.json()
    print(data_dict['display_name'])

    reverse_string(data_dict['display_name'])
    reverse_string(2342342)
