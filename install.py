import os

os.system("clear")
print("***[-----ACTUALIZANDO PAQUETES-----]***")
os.system("apt update && apt upgrade && apt install python3 python3-pip")
print("***[-----INSTALANDO REQUERIMIENTOS-----]***")
os.system("pip install google colorama socket platform psutil datetime")

print("""
    \t---------------------------------------------------------
    \tInstalacion terminada, ahora podra arrancar el script!...
    \t---------------------------------------------------------""")
