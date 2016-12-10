import dpkt
import socket

def printPcap(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ##parse and decode into a  friendly way
            print(ts,len(buf))      ##timestamp &&buf is the buffer
            ip = eth.data ##class dpkt.ip.IP (including len,id,p,sum,src,dst,opts data(with sport,dport,ulen,sum...)...)
            ##get the data
            src = socket.inet_ntoa(ip.src)
            ##"socket" see in doc. src:source
            dst = socket.inet_ntoa(ip.dst)
            ##dst: destination
            print('[+] Src: ' + src + ' --> Dst: ' + dst)
        except:
            pass


def main():
    f = open('data.pcap',"rb")
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == '__main__':    main()
