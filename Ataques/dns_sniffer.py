#!/usr/bin/env python3

import scapy.all as scapy

def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()

        exclude_keywords = ["google", "cloud", "bing", "static"]

        if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords):
            domains_seen.add(domain)
            print(f"Dominio: {domain}")

def sniff(interface):


    scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0) # DNS -> 53


def main():

    interface = "ens33"
    print(f"\nInterceptando paquetes de la máquina víctima")
   
if __name__ == '__main__':
    global domains_seen
    domains_seen = set()
    main()

#En esta clase, nos centraremos en la creación de un rastreador de consultas DNS (DNS Sniffer) utilizando Scapy, una herramienta de Python orientada a la manipulación de paquetes de red para propósitos ofensivos. Un DNS Sniffer es una herramienta ofensiva que permite interceptar y analizar las consultas DNS en una red. Estas consultas son esenciales en la comunicación de Internet, ya que convierten nombres de dominio en direcciones IP.

#Con Scapy, aprenderás a capturar paquetes DNS de forma activa para explorar cómo los dispositivos en una red interactúan con servidores DNS. Este conocimiento es crucial en el contexto ofensivo, ya que permite identificar objetivos potenciales para ataques y explotar vulnerabilidades en la comunicación DNS.

#Durante la clase, te mostraremos cómo se pueden utilizar estas técnicas para reunir información valiosa sobre una red y sus usuarios, lo que puede ser utilizado en diversas estrategias de ataque. Al final de esta sesión, habrás desarrollado una herramienta ofensiva clave que te permitirá realizar reconocimientos avanzados y explotar debilidades en la gestión de DNS dentro de una red.
