import urllib.request
import time

version = "0907221756"
scriptlist = (open("/usr/local/src/scriptlist.dat","r")).read().splitlines()

urllib.request.urlretrieve("https://github.com/Ric01982/pi-start/raw/main/scriptlist.dat","/usr/local/src/scriptlist.dat")

while True:
                
        for script in scriptlist:
                
                urllib.request.urlretrieve(f"https://github.com/Ric01982/pi-start/raw/main/{script}",f"/usr/local/src/{script}")
                print(f"https://github.com/Ric01982/pi-start/raw/main/{script}",f"/usr/local/src/{script}")
        time.sleep(30)


 



