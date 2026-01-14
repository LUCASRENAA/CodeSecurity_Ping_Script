import os
import ipaddress

ip = input("Digite o endereço de IP: ")


#1-255.1-225.1-255.1-255

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False



is_valid_ip(ip)


"""
try:
    validacao_ip = ipaddress.ip_address(ip)
    print(validacao_ip)

except ValueError:
    print("IP inválido")
    exit()
"""
# ip que estou recebendo do usuário, de fato, é um ip ou não?




os.system(f"ping {ip} ")


for a in range(137,256):
     split_ip = ip.split(".")
     novo_ip = f"{split_ip[0]}.{split_ip[1]}.{split_ip[2]}.{a}"
     #print(novo_ip)
     print("começando no ip:", novo_ip)#
     
     status = os.system(f"ping {novo_ip} -n 1 | find \"TTL\" > nul")
     if status == 0:
            print(f"{novo_ip} está ativo")
     




# Quais são os computadores na minha rede de casa?
#192.168.0.1 - está ativo - roteador
#192.168.0.137 - está ativo e é o meu computador

#ping {{ ip }}