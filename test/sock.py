import socket
import optparse


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,
                            socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print('[+]%d/tcp open' % tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
        print(tgtIP)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
        socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        connScan(tgtHost, int(tgtPort))
portScan('127.0.0.1', [80,443,3389,1433,23,445,5000])