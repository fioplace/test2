import zipfile
import threading
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)

        print ('Found Password:',password)
        return password
    except:
        pass

def main():
    zFile=zipfile.ZipFile('unzip.zip')
    passFile=open('dictionary.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        t=threading.Thread(target=extractFile,args=(zFile,password))
        t.start()


