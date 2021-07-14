from socket import *

#Function for scanning ports 
def conScan(targethost: str, targetport: int):
    #connecting with the host on desired port
    try:
        conskt = socket(AF_INET, SOCK_STREAM)
        conskt.connect((targethost, targetport))
        print('[+] Port ' , targetport,' /tcp open')
        conskt.close()

    #if connection failed     
    except:
        print('[-] Port', targetport,' /tcp closed')

#Function which converts domain name to IP (if domain name is provided by the user) and then starts scanning
def portScan(targethost: str, targetports: list):
    try:
        targetIP = gethostbyname(targethost)
    except:
        print('[-] Cannot resolve' ,targethost)
        return
    
    print('\n[+] Scan result of :', targethost)

    print(f'\nScanning {len(targetports)} port(s)')
    setdefaulttimeout(2)

    for targetport in targetports:
        conScan(targethost, int(targetport))


def main():
    target = input("Enter a site or its IP adress : ")
    portlist = []
    portsnum = int(input("Enter number of ports you want to scan : "))

#adding ports in portlist
    for p in range(portsnum):
        port = int(input("Enter port : "))
        portlist.append(port)

    portScan(target, portlist)


if __name__ == "__main__":
    main()
