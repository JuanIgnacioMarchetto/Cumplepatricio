import time
import sys
import webbrowser
from colorama import init, Fore, Back, Style
from datetime import datetime

init(autoreset=True)

def animacion_carga():
    for _ in range(2): 
        for symbol in '|/-\\':
            sys.stdout.write(Fore.GREEN + f'\rCargando {symbol} ')
            sys.stdout.flush()
            time.sleep(0.2)
    print(Fore.GREEN + "\r¡Carga completa!")


def pedir_datos():
    print(Fore.YELLOW + Style.BRIGHT + "¡Bienvenido! Por favor ingresa los siguientes datos:")
    nombre = input(Fore.CYAN + "Nombre completo: ")
    fecha_actual = input(Fore.CYAN + "Fecha de hoy (dd/mm/yyyy): ")
    return nombre, fecha_actual

def verificar_datos(nombre, fecha_actual):
    if nombre == "Juan Patricio Marchetto" and fecha_actual == "10/09/2024":
        return True
    return False

nombre, fecha_actual = pedir_datos()

animacion_carga()

if verificar_datos(nombre, fecha_actual):
    print(Fore.CYAN + Style.BRIGHT + "\n¡Feliz cumpleaños, Juan Patricio Marchetto!")
    webbrowser.open('.Este equipo/Disco local(c)/Usuarios/march/Patricio/Index.html')  
else:
    print(Fore.RED + Style.BRIGHT + "\nDatos incorrectos, por favor inténtalo nuevamente.")
