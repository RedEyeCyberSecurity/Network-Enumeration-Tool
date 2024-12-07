import socket
from ipaddress import ip_address


def scan_network(start_ip, end_ip, port_range):
    for ip_int in range(int(ip_address(start_ip)), int(ip_address(end_ip))):
        ip = str(ip_address(ip_int))
        for port in port_range:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                try:
                    s.connect((ip, port))
                    print(f"[+] Found open port {port} at IP {ip}")
                except:
                    pass


start_ip = input("Start IP: ")
end_ip = input("End IP: ")
port_range = range(1, 1025)

scan_network(start_ip, end_ip, port_range)
