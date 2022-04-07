from fileinput import filename
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import sys


def select_file_en():
    global en_filename
    filetypes = (
        ('All files', '*.*'),       
        )

    filename = fd.askopenfilename(
        title='Choose a file to encrypt',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
        )
    en_filename = filename
      
def select_file_de():
    global de_filename
    filetypes = ( 
        ('All files', '*.*'),               
    )

    filename = fd.askopenfilename(
        title='Choose a file to decrypt',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    de_filename = filename

def select_key():
    global de_key
    filetypes = ( 
        ('All files', '*.*'),               
    )

    key = fd.askopenfilename(
        title='Choose a file to decrypt',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=key
    )
    de_key = key

def encrypt(en_filename):
    to_encrypt = open(en_filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(en_filename + ".key", "wb") as key_out:
        key_out.write(key)
        encrypted = bytes(a^b for (a,b) in zip(to_encrypt, key))
    with open(en_filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

def decrypt(de_filename, de_key):
    file = open(de_filename, "rb").read()
    key = open(de_key, "rb").read()
    decrypted = bytes(a^b for (a,b) in zip(file, key))
    with open(de_filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)


root = tk.Tk()

root.configure(bg='#EEAABB')

root.title('NDA')

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

root.attributes('-alpha',1)

root.attributes('-topmost', 0)

program_directory=sys.path[0]
root.iconphoto(True, tk.PhotoImage(file=os.path.join(program_directory, "favicon.png")))

def openHelpWindow():
    help = tk.Tk() 

    help.configure(bg='#EEAABB')

    help.title('Help')

    window_width = 400
    window_height = 300

    screen_width = help.winfo_screenwidth()
    screen_height = help.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    help.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    help.resizable(False, False)

    help.attributes('-alpha',1)

    help.attributes('-topmost', 0)

    ttk.Label(help, wraplength=window_width, background='#EEAABB', text='NDA(Encrypt/Decrypt Application) is a tool, meant to make IT-Security easy for everybody. No nerdy extras or passwords to remember. !Just be sure to NOT lose the .key file! \n\nHOW TO:\n1a. Select your file you want to encrypt\n2a. Hit encrypt\n\n1b. Select your file you want to decrypt\n2b. Select the keyfile that has been created when encrypting\n3b. Hit Decrypt\n\nQuestions or suggestions? feel free to send me an E-Mail at'
    ).pack(ipadx='0', ipady='0')

    textBox = tk.Entry(help)
    textBox.insert(0, "XX@XX.de")
    textBox.configure(state='readonly', readonlybackground='#ff7b7b', relief='sunken')
    textBox.pack(ipadx='22')

    help.mainloop()

root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)

buttonFont = font.Font(family='Helvetica', size=12, weight='bold')

tk.Button(root, cursor='hand2', text='Select file to encrypt', bg='#FF6D6D', fg='#ffffff', command=select_file_en).place(anchor='nw', relx='0.25', rely='0.12', x='0', y='0')

tk.Button(root, cursor='hand2', text='Encrypt file', font=buttonFont, bg='#FF6D6D', fg='#ffffff', command= lambda: encrypt(en_filename)).place(anchor='nw', relx='0.78', rely='0.12', x='0', y='0')

ttk.Separator(root, orient='horizontal').place(anchor='nw', relheight='0.02', relwidth='1.0', relx='0.0', rely='0.30', y='0') #bg='#ff7b7b'

tk.Button(root, cursor='hand2', text='Select file to decrypt', bg='#FF6D6D', fg='#ffffff', command=select_file_de).place(anchor='nw', relx='0.25', rely='0.4', x='0', y='0')

tk.Button(root, cursor='hand2', text='Select key', bg='#FF6D6D', fg='#ffffff', command=select_key).place(anchor='nw', relx='0.57', rely='0.4', x='0', y='0')

tk.Button(root, cursor='hand2', text='Decrypt file', font=buttonFont, bg='#FF6D6D', fg='#ffffff', command= lambda: decrypt(de_filename, de_key)).place(anchor='nw', relx='0.78', rely='0.4', x='0', y='0')

ttk.Label(root, background='#ff7b7b', text='v 0.2').grid(column='1', row='6')

tk.Button(root, background='#ff7b7b', text='Help', command=openHelpWindow).grid(column='4', row='6') 

textBox = tk.Entry(root)
textBox.insert(0, "XX@XX.de")
textBox.configure(state='readonly', readonlybackground='#ff7b7b', relief='sunken')
textBox.grid(column='3', row='6', ipadx='22')

root.mainloop()
