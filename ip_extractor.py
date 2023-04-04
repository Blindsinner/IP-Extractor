          
import socket
import ipaddress
from ipwhois import IPWhois
import geocoder
import nmap

def get_open_ports(ip, port_range='1-1024'):
    nm = nmap.PortScanner(nmap_search_path=(r'C:\Program Files (x86)\Nmap\nmap.exe',))
    nm.scan(ip, port_range)
    if ip in nm.all_hosts():
        open_ports = [port for port in nm[ip]['tcp'] if nm[ip]['tcp'][port]['state'] == 'open']
    else:
        open_ports = []
    return open_ports

def get_ip_info(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f"IP Version: {'IPv6' if ip_obj.version == 6 else 'IPv4'}")
        if ip_obj.version == 4:
            ip_class = None
            if ip_obj.is_multicast:
                ip_class = 'D'
            elif ip_obj.is_private:
                ip_class = 'C' if ip_obj in ipaddress.ip_network('192.168.0.0/16') else 'B' if ip_obj in ipaddress.ip_network('172.16.0.0/12') else 'A'
            print(f"IP Class: {ip_class}")
        # Reverse DNS
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"Hostname: {hostname[0]}")
        except socket.herror:
            print("Hostname not found")

        # Open Ports
        port_range = '1-1024'  # Adjust this to scan a different range of ports
        open_ports = get_open_ports(ip, port_range)
        print(f"Open Ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")

        # Network ID, Subnet Mask, Host Address, Network Class, and Possible Subnet Count
        whois = IPWhois(ip)
        whois_info = whois.lookup_rdap()
        network_cidr = whois_info['network']['cidr']
        network_obj = ipaddress.ip_network(network_cidr, strict=False)

        print(f"Network ID: {network_obj.network_address}")
        print(f"Subnet Mask: {network_obj.netmask}")
        print(f"Host Address: {ip_obj}")
        print(f"Network Class: {'Classless' if network_obj.is_private else 'Classful'}")
        print(f"Possible Subnet Count: {2 ** (32 - network_obj.prefixlen)}")

        print(f"ASN: {whois_info['asn']}")
        print(f"ISP: {whois_info['asn_description']}")

        if 'country' in whois_info:
            print(f"Country: {whois_info['country']}")
        else:
            print("Country information not available")

        print(f"Network: {whois_info['network']['cidr']}")
        geo_info = geocoder.ip(ip)
        if geo_info.ok:
            print(f"Latitude: {geo_info.lat}")
            print(f"Longitude: {geo_info.lng}")
            print(f"City: {geo_info.city}")
            print(f"State: {geo_info.state}")
            print(f"Postal Code: {geo_info.postal}")

    except ValueError:
        print("Invalid IP address")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = input("Enter the IP address: ")
    get_ip_info(ip)


