import requests

while True:
    ip_add = input("Masukkan Ip Address : ")
    if ip_add == "quit" or ip_add == "q":
        break

    url = (f'https://ipapi.co/{ip_add}/json/')
    response = requests.get(f'https://ipapi.co/{ip_add}/json/').json()
    print("URL: " + (url))
    print("==========================================")
    print("IP Address: " ,response["ip"])
    print("City: " ,response["city"])
    print("Region: " ,response["region"])
    print("Country: " ,response["country_code"], "|" ,response ["country_name"])

    lat = response["latitude"]
    lon = response["longitude"]
    print("Latitude / Longitude: ", lat, ",", lon)

    map = f"http://maps.google.com/maps?z=18&q={lat},{lon}"
    print("Map: ", map)

    print("Time Zone: ", response["timezone"])
    print("Calling Code: ", response["country_calling_code"])
    print("Currency: ", response["currency"])
    print("Language: ", response["languages"])
    print("ASN: ", response["asn"])
    print("Org: ", response["org"])
    print("==========================================\n")
