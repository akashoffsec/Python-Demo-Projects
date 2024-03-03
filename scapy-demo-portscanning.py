from scapy.all import *

# First we have to decleare the handshakes
SYN = 0x02
RST = 0x04
ACK = 0x10

target = input("Enter the target IP or Domain: ")

for port in [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    80,   # HTTP
    443,  # HTTPS
    3306, # MySQL
    1433, # MSSQL
    5432, # PostgreSQL
    53,   # DNS
    3389, # RDP
    137,  # NetBIOS
    138,  # NetBIOS
    139,  # NetBIOS
    445,  # SMB
    2049, # NFS
    161,  # SNMP
]:
    tcp_connect = sr1(IP(dst=target)/TCP(sport=RandShort(), dport=port, flags="S"), timeout=1, verbose=False)
    if tcp_connect and tcp_connect.haslayer(TCP):
        response_flags = tcp_connect.getlayer(TCP).flags
        if response_flags == (SYN + ACK):
            snd_rst = send(IP(dst=target)/TCP(sport=RandShort(), dport=port, flags="AR"), verbose=False)
            print("{} is open!".format(port))
        elif response_flags == (RST + ACK):
            print("{} is closed!".format(port))
    else:
        print("{} is closed!".format(port))