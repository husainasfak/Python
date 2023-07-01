import tkinter as tk
from compressModule import compress, decompress
from tkinter import filedialog
from random import randint


def openFile(input):
    print('file opening')
    fileName = filedialog.askopenfilename(
        initialdir='/', title='Select a file to compress')

    input.delete(0, tk.END)
    input.insert(0, fileName)
    return fileName


def compression(i, o, output_area):
    output_area['text'] = o
    compress(i, o)


def deCompression(i, o, output_area):
    decompress(i, o)


window = tk.Tk()

window.title("Compression Engine")
window.geometry("600x400")

input_label = tk.Label(window, text='File to be compressed')
input_label.grid(row=0, column=0)
input_entery = tk.Entry(window)
input_entery.grid(row=0, column=1)


choose_file_btn = tk.Button(
    window, text='Choose from computer', command=lambda: openFile(input_entery))
choose_file_btn.grid(row=0, column=2)

output_lable = tk.Label(window, text="Name of the compressed file : ")
output_lable.grid(row=1, column=0)

output_file = tk.Label(window)
output_file.grid(row=1, column=1)

compress_button = tk.Button(window, text="Compress", command=lambda: compression(
    input_entery.get(), f'compressedFile{randint(0,100)}.txt', output_file))
compress_button.grid(row=2, column=1)


window.mainloop()
