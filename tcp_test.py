import optparse
import socket
import threading
'''
parser=optparse.OptionParser('usage %prog -H <target host> -P <target port>')
parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
parser.add_option('-P',dest='tgtPort',type='int',help='specify target port')
(options,args)=parser.parse_args()
tgtHost =options.tgtHost
tgtPort =options.tgtPort
if (tgtHost == None)|(tgtPort==None):
    print(parser.usage)
    exit(0)
else:
    print(tgtHost)
    print(tgtPort)
'''
screenLock=threading.Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSKT=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSKT.connect((tgtHost,tgtPort))
        connSKT.send('violentPython\r\n')
        results=connSKT.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open\n'%tgtPort)
        print('[+]'+str(results))
        connSKT.close()
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed\n'%tgtPort)
    finally:
        screenLock.release()


def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=socket.gethostbyname(tgtHost)
    except:
        print("[-]Cannot resolve '%s': Unknown host"%tgtHost)
        return
    try:
        tgtName= socket.gethostbyaddr(tgtIP)
        print('\n[+]Scan Results for:'+tgtName[0])
    except:
        print('\n[+]Scan Results for:'+tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port '+ str(tgtPort))
        t=threading.Thread(target=connScan, args=(tgtHost,int (tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -P <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print('[-] You must specify a target host and port[s]!')
        exit(0)
    portScan('www.qq.com',[80,21,23,443,445,8000,8080])

if __name__=='__main__':
    main()



