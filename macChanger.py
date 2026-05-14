import random
import subprocess
import re

list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
mac = ""
for i in range(12):
    mac += random.choice(list)
#print(mac)
result = subprocess.check_output("ifconfig eth0", shell = True).decode()
#print(result)

#oldmac = re.search("ether (.+)", result).group().split()[1]  # mac adresine ulaşıyoruz.
#print(oldmac)

oldmac = re.search("ether(.*?) txq", result).group(1).strip() # mac adresine ulaşıyoruz.
#print(oldmac)

subprocess.check_output("ifconfig eth0 down", shell=True)
subprocess.check_output("ifconfig eth0 hw ether "+ mac, shell=True)
subprocess.check_output("ifconfig eth0 up", shell=True)

print(oldmac)
print(mac)