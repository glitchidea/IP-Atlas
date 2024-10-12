#!/usr/bin/env python3

import geoip2.database

city_db_path = 'GeoLite2-City.mmdb'
country_db_path = 'GeoLite2-Country.mmdb'
asn_db_path = 'GeoLite2-ASN.mmdb'

def get_ip_info(ip_address):
    try:
        city_reader = geoip2.database.Reader(city_db_path)
        country_reader = geoip2.database.Reader(country_db_path)
        asn_reader = geoip2.database.Reader(asn_db_path)

        city_response = city_reader.city(ip_address)
        print(f"IP: {ip_address}")
        print(f"City: {city_response.city.name}")
        print(f"Region: {city_response.subdivisions.most_specific.name}")
        print(f"Country: {city_response.country.name}")
        print(f"Location: {city_response.location.latitude}, {city_response.location.longitude}")
        print(f"Google Maps: https://www.google.com/maps?q={city_response.location.latitude},{city_response.location.longitude}")
        print(f"Postal: {city_response.postal.code}")
        print(f"Timezone: {city_response.location.time_zone}")

        country_response = country_reader.country(ip_address)
        print(f"Country Code: {country_response.country.iso_code}")

        asn_response = asn_reader.asn(ip_address)
        print(f"ASN: {asn_response.autonomous_system_number}")
        print(f"ASN Name: {asn_response.autonomous_system_organization}")

        city_reader.close()
        country_reader.close()
        asn_reader.close()

    except geoip2.errors.AddressNotFoundError:
        print("IP adresi bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    while True:
        ip = input("Enter IP address (press 'q' to exit): ").strip()

        if ip.lower() == 'q':
            break

        get_ip_info(ip)
        print("-" * 50)
