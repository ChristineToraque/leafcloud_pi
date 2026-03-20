import socket
import threading
import ipaddress
import time

def get_local_ip():
    """Attempts to determine the local IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't actually connect, just used to get the interface IP
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def check_port(ip, port, open_ports):
    """Checks if a port is open on a given IP."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Short timeout for speed
    result = sock.connect_ex((str(ip), port))
    if result == 0:
        try:
            hostname = socket.gethostbyaddr(str(ip))[0]
        except socket.herror:
            hostname = "Unknown Hostname"
        open_ports.append((str(ip), hostname))
    sock.close()

def scan_network(subnet, port=22):
    """Scans the subnet for open ports."""
    print(f"Scanning subnet: {subnet} for port {port}...")
    network = ipaddress.ip_network(subnet, strict=False)
    threads = []
    open_ports = []

    # Limit threads to avoid overwhelming the system/network
    max_threads = 100
    
    ips = list(network.hosts())
    
    for i, ip in enumerate(ips):
        t = threading.Thread(target=check_port, args=(ip, port, open_ports))
        threads.append(t)
        t.start()
        
        # Simple throttle to keep active threads in check
        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    # Join remaining threads
    for t in threads:
        t.join()

    return open_ports

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Your local IP is: {local_ip}")
    
    # Assume /24 subnet (255.255.255.0)
    subnet = ".".join(local_ip.split('.')[:3]) + ".0/24"
    
    found_devices = scan_network(subnet)
    
    print("\nDevices found with SSH (Port 22) open:")
    if found_devices:
        for ip, hostname in sorted(found_devices):
            print(f" - {ip} ({hostname})")
            print(f"   Try: ssh tin@{ip}")
    else:
        print("No devices found with port 22 open.")
