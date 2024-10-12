#!/usr/bin/env python3

import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            print(f"IP: {data.get('ip', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"Region: {data.get('region', 'N/A')}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Location: {data.get('loc', 'N/A')}")
            print(f"Google Maps: https://www.google.com/maps?q={data.get('loc', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
            print(f"Postal: {data.get('postal', 'N/A')}")
            print(f"Timezone: {data.get('timezone', 'N/A')}")
            
            asn = data.get('asn', {})
            print(f"ASN: {asn.get('asn', 'N/A')}")
            print(f"ASN Name: {asn.get('name', 'N/A')}")
            print(f"ASN Domain: {asn.get('domain', 'N/A')}")
            print(f"ASN Route: {asn.get('route', 'N/A')}")
            
            company = data.get('company', {})
            print(f"Company Name: {company.get('name', 'N/A')}")
            print(f"Company Domain: {company.get('domain', 'N/A')}")
            print(f"Company Type: {company.get('type', 'N/A')}")
            
            privacy = data.get('privacy', {})
            print(f"VPN: {privacy.get('vpn', 'N/A')}")
            print(f"Proxy: {privacy.get('proxy', 'N/A')}")
            print(f"Tor: {privacy.get('tor', 'N/A')}")
            print(f"Relay: {privacy.get('relay', 'N/A')}")
            print(f"Hosting: {privacy.get('hosting', 'N/A')}")
            print(f"Service: {privacy.get('service', 'N/A')}")
            
            abuse = data.get('abuse', {})
            print(f"Abuse Address: {abuse.get('address', 'N/A')}")
            print(f"Abuse Country: {abuse.get('country', 'N/A')}")
            print(f"Abuse Email: {abuse.get('email', 'N/A')}")
            print(f"Abuse Name: {abuse.get('name', 'N/A')}")
            print(f"Network: {abuse.get('network', 'N/A')}")
            print(f"Phone: {abuse.get('phone', 'N/A')}")
            
        else:
            print("Bilgi alınamadı. Lütfen tekrar deneyin.")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    while True:
        ip = input("Enter IP address (press 'q' to exit): ").strip()
        
        if ip.lower() == 'q':
            break
        
        get_ip_info(ip)
        
        input("Press Enter to continue...")
