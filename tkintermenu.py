#tkinter
from tkinter import *
root = Tk()  #main application window
#root.iconbitmap('fluidicon.ico') #always conversion to icon for trademark
root.title("MyApp")

def dummy():pass
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=dummy)
filemenu.add_command(label="Open",command=dummy)
filemenu.add_command(label="Save",command=dummy)
filemenu.add_separator()

filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)

#add_command()
add_cascade()



#obj=PhotoImage(file="i1.png",height=32,width=32)
#b= Button(root,text="Hello",image=obj,compound="left")
#b.pack(side=LEFT,fill=X)
root.mainloop() #keep the main window open untill root.quit()

