import urllib.request, urllib.parse
import json, ssl

#Service url
service_url = "https://py4e-data.dr-chuck.net/opengeo?"

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#input, create socket, encode and decode data, transform it to string
while True:
    address = input("Enter address >>> ")
    if address == 'quit':
        print('You quit')
        quit()
    elif len(address) < 1:
        break

    address = address.strip()
    par = dict()
    par['q'] = address
    url = service_url + urllib.parse.urlencode(par)

    print("Getting data from", url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
    except:
        print("Connection error")
        quit()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except ValueError:
        print('Failed to decode,', data, 'try again')
        quit()

    if 'features' not in js:
        print('Something went wrong, try again')
        quit()

#find all that was asked in data and print
    if 'features' in js and len(js['features']) > 0:
        properties = js['features'][0]['properties']

        lon = properties.get('lon', 'N/A')
        lat = properties.get('lat', 'N/A')
        type_r = properties.get('result_type', 'N/A')
        plus_c = properties.get('plus_code', 'N/A')
        time_z = properties.get('timezone', {}).get('display_name', 'N/A')
        display_n = properties.get('display_name', 'N/A')
        country = properties.get('country', 'N/A')
        county = properties.get('county', 'N/A')

        print(country, ',', county, ',', display_n)
        print('Longitude:', lon, 'Latitude:', lat)
        print('Result Type:', type_r)
        print('Time Zone:', time_z)
        print('Plus code:', plus_c)
    else:
        print('No results, try again')
