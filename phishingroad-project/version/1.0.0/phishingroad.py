import socket
import time
import subprocess
import requests
import re

# public ip

def get_public_ip():
    try:
        
        response = requests.get('https://httpbin.org/ip')
        
        
        public_ip = response.json()['origin']
        
        return public_ip
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Adresse IP publique : {public_ip}")
    else:
        print("Impossible de récupérer l'adresse IP publique.")

with open('ippublique.txt', 'w') as fichier:
    fichier.write(public_ip)

time.sleep(1)

# local ip

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)

        s.connect(("google.com", 80))

        local_ip = s.getsockname()[0]

        return local_ip
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    local_ip = get_local_ip()

    if local_ip:
        print(f"Adresse IP locale : {local_ip}")
    else:
        print("Impossible de recuperer l'adresse IP locale.")

with open("iplocale.txt", 'w') as file:
    file.write(local_ip)

time.sleep(1)

# chrome version 

def get_chrome_version():
    try:
        reg_query_command = 'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'

        output = subprocess.check_output(reg_query_command, shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8')

        version_match = re.search(r"version\s+REG_SZ\s+([^\r\n]+)", output)
        if version_match:
            return version_match.group(1)
        else:
            return "Version de Google Chrome introuvable"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    chrome_version = get_chrome_version()
    print(f"Version de Google Chrome : {chrome_version}")

with open("version chrome.txt", 'w') as file:
    file.write(chrome_version)

time.sleep(1)

print("By <<<<<Script/No-Sleep>>>>> (https://scriptnosleep.com)")


    





