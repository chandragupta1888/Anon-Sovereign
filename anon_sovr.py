import random
import subprocess
from faker import Faker
print("# WARNING  This tool works only on LINUX Operating System. !")
mac = [ 0x00, 0x24, 0x81,
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
mac = ":".join(map(lambda x: "%02x" % x, mac))
ex = Faker()
ip = ex.ipv4()
print("{~} Changing MAC & IP address for eth0")
subprocess.run(["ifconfig", "eth0", "down"])
subprocess.run(["ifconfig", "eth0", "hw", "ether", mac])
subprocess.run(["ifconfig", "eth0", ip])
subprocess.run(["ifconfig", "eth0", "up"])
print("Changed MAC & IP address successfully")
subprocess.run(["proxychains", "firefox", "www.google.com"])
subprocess.run(["sudo", "service", "network-manager", "restart"])
print("\n\nCleaned DNS Records successfully !!\n\n")