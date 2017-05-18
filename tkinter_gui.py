from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class App:
    def __init__(self,master):

        self.notebook = ttk.Notebook(master)
        self.notebook.pack()

        frame1 = self.frame1_config(master)
        frame2 = self.frame2_config(master)
        self.menu_config(master)

        self.notebook.add(frame1 , text = 'one')
        self.notebook.add(frame2, text = 'two')

        self.notebook.pack(fill=BOTH, expand=1)

    def function1(self):
        print("clicked")
    def function2(self):
        print("clicked2")

    def frame1_config(self, root):
        frame1= ttk.Frame(self.notebook)
        frame1.config(height = 300 , width = 400)
        ttk.Button(frame1, text = 'Button 1', command = self.function1).grid(row =1 , column =0)
        ttk.Button(frame1, text = 'Button 2', command = self.function2).grid(row =2 , column =0)
        scale = ttk.Scale(frame1, orient = HORIZONTAL , length = 400).grid(row =3 , column =0)

        month = StringVar()
        combobox = ttk.Combobox(frame1, textvariable = month)
        combobox.grid(row =4 , column =0)
        combobox.config(values = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))
        year = StringVar()
        spinbox = Spinbox(frame1 , from_ = 1990 , to = 2020, textvariable = year)
        spinbox.grid(row = 5, column=0)

        return frame1

    def frame2_config(self, root):
        frame2 = ttk.Frame(self.notebook)
        RadioButton = ttk.Radiobutton(frame2 , text = 'Breakfast').grid(row =1 , column =0)
        ttk.Checkbutton(frame2, text = ' sausage').grid(row =2 , column =0)
        ttk.Checkbutton(frame2, text = ' milk').grid(row =3 , column =0)
        ttk.Checkbutton(frame2, text = ' eggs').grid(row =4 , column =0)
        ttk.Checkbutton(frame2, text = ' pancake').grid(row =5 , column =0)
        ttk.Checkbutton(frame2, text = ' cheese').grid(row =6 , column =0)
        display = Text(frame2, width = 200 , height = 100)
        display.insert('1.0','end', ' this is my string')

        i = ImageTk.Image.open("logo.png")
        photo = ImageTk.PhotoImage(i)
        label = Label(frame2, text="test", image = photo)
        label.img = photo
        label.grid(row =7 , column =0)

        return frame2

    def menu_config(self, root):
        root.option_add('*tearOff',False)
        menubar =Menu(root)
        root.config(menu = menubar)
        File = Menu(menubar)
        Edit = Menu(menubar)
        Help_ = Menu(menubar)
        menubar.add_cascade( menu = File , label = 'File')
        menubar.add_cascade( menu = Edit , label = 'Edit')
        menubar.add_cascade( menu = Help_, label = 'Help')
        File.add_command( label = 'New', command = lambda: print(" New File"))
        File.add_separator()
        File.add_command( label = 'Open',command = lambda: print("Open File"))
        File.add_separator()
        save = Menu(File)
        File.add_cascade( menu = save , label ='Save')
        save.add_command(label ='Save_as', command = lambda: print(" Save as"))
        save.add_command(label ='Save_all',command = lambda: print(" Save all"))

def main():
    root= Tk()
    root.geometry('{}x{}'.format(800, 600))
    root.resizable(width=False, height=False)
    app = App(root)
    root.mainloop()

if __name__== "__main__":main()
