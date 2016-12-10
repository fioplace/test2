import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
        return False

host = '192.168.9.3'
anonLogin(host)
