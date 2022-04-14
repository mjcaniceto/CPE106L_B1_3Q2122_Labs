#POSTLAB 2
#2. Explore the Tkinter.filedialog module to get the name of a text file 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#Root window
root = tk.Tk()
root.title('Postlab 2')
root.resizable(False, False)

#Text display
text = tk.Text(root, height=10)
text.grid(column=0, row=0, sticky='nsew')

#Button click function
def file_select():
    filetypes= (("Text files","*.txt")
                ,("All files","*.*"))
    fd = filedialog.askopenfilename(title='Select file'
                , filetypes=filetypes)
    text.insert('2.0', fd)

#Button object
button = ttk.Button(root, text="Select File",command=file_select)
button.grid(column=1, row=1, stick='w', padx=10, pady=10)

#Mainloop
root.mainloop()
