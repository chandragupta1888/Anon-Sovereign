import os
import subprocess
print("##configuring Anon Sovereign ##")
subprocess.run(["sudo", "apt-get", "install", "tor"]) 
source = 'proxychains.conf'
dest='/etc/proxychains.conf'
os.replace(source, dest)
#subprocess.run(["cp", "/etc/proxychains.conf", "~/Desktop/Mini_project"])
subprocess.run(["sudo", "apt-get", "-y", "install", "dnsmasq"])
print("\n Anon Sovereign configured successfully !!\n\n Now you can run \"python3 anonsov.py\"")