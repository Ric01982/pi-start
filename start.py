import urllib.request
import time

version = "0907221402"
scriptlist = (open("/usr/local/src/scriptlist.dat","r")).read()


while True:
        urllib.request.urlretrieve("https://github.com/Ric01982/pi-start/raw/main/scriptlist.dat","/usr/local/src/scriptlist.dat")
        
        for script in scriptlist:
                
                urllib.request.urlretrieve("https://github.com/Ric01982/pi-start/raw/main/"&script,"/usr/local/src/"&script)

        time.sleep(30)







