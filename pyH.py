#   // portScanner

import socket         #allow us to established connection over the internet
from IPy import IP    #need to install IPy if not installed
#   185.53.143.12, 69.164.201.231 (target)


#   // portScannerBasic //

# def checkIP(ip):
#     try:
#         IP(ip)
#         return(ip)
#     except ValueError:
#         return socket.gethostbyname(ip)

# def scanPort(ipaddress, port):
#     try:
#         sock = socket.socket()
#         sock.settimeout(0.5)
#         sock.connect((ipaddress, port))
#         print("[+] port " + str(port) + " open")
#     except:
#         print("[+] port " + str(port) + " close")

# ipaddress = input("[+] enter ip target : ")
# convertedIP = checkIP(ipaddress)

# for port in range(1,100):
#     scanPort(ipaddress, port)




# #   // scan multi port //

# def scan(target):
#     convertedIP = checkIP(target)
#     print("\n" + "[+] Scanning Target " + str(target))
#     for port in range(1, 100):
#         scanPort(convertedIP, port)

# def checkIP(ip):
#     try:
#         IP(ip)
#         return(ip)
#     except ValueError:
#         return socket.gethostbyname(ip)

# def scanPort(ipaddress, port):
#     try:
#         sock = socket.socket()
#         sock.settimeout(0.5)
#         sock.connect((ipaddress, port))
#         print("[+] Port " + str(port) + " is Open")
#     except:
#         # print("[+] Port " + str(port) + "is Closed")
#         pass

# targets = input("[+] Enter Target to Scan/s (split multi target with ,) : ")
# if "," in targets:
#     for IPaddr in targets.split(","):
#         scan(IPaddr.strip(" "))
# else:
#     scan(targets)




#   // scan multi port with banner //

def scan(target):
    convertedIP = checkIP(target)
    print("\n" + "[+] Scanning Target " + str(target))
    for port in range(1, 100):
        scanPort(convertedIP, port)

def checkIP(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def getBanner(s):
    return s.recv(1024)

def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = getBanner(sock)
            # print("[+] Port " + str(port) + " is Open" + " : " + str(banner))
            print("[+] Port " + str(port) + " is Open" + " : " + str(banner.decode().strip("\n")))
        except:
            print("[+] Port " + str(port))
    except:
        # print("[+] Port " + str(port) + "is Closed")
        pass

targets = input("[+] Enter Target to Scan/s (split multi target with ,) : ")
if "," in targets:
    for IPaddr in targets.split(","):
        scan(IPaddr.strip(" "))
else:
    scan(targets)