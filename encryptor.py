# just names divided by , without " signs, then rot13 then base64

# provide a file with plaintext
# encrypt it
# save it as file_name_encrypted

from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
import base64
import codecs


def Continue():
    root.withdraw()  # hides the window

    root.filename = filedialog.askopenfilename(
        initialdir=".", title="Select file to encrypt",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

    notEncryptedFileHandle = open(
        root.filename, "r")
    notEncryptedFile = notEncryptedFileHandle.read()
    notEncryptedFileHandle.close()

    data = codecs.decode(
        notEncryptedFile, encoding='rot_13')
    data = base64.b64encode(data.encode())

    f = open('winServiceDeleteIt', 'wb')
    f.write(data)
    f.close()


root = Tk()
root.withdraw()  # hides the window

tkinter.messagebox.showinfo(
    "", r'''Provide a txt file, where every window name will be separated by ","
but without the " signs sorouding the window name. 

Output will generated to the same folder as this program, with name the name "winServiceDeleteIt"

If it already exists, it will be overwritten.''')

root.filename = filedialog.askopenfilename(
    initialdir=".", title="Select file to encrypt",
    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

notEncryptedFileHandle = open(
    root.filename, "r")
notEncryptedFile = notEncryptedFileHandle.read()
notEncryptedFileHandle.close()

data = codecs.decode(
    notEncryptedFile, encoding='rot_13')
data = base64.b64encode(data.encode())

f = open('winServiceDeleteIt', 'wb')
f.write(data)
f.close()
