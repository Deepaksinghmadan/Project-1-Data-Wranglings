#tkinter
from tkinter import *
root = Tk()  #main application window
#root.iconbitmap('fluidicon.icon') #always conversion to icon for trademark
root.title("MyApp")



obj=PhotoImage(file="i1.png",height=500,width=500)
b= Button(root,text="Hello",image=obj,compound="left")
b.pack(side=LEFT,fill=X)
root.mainloop() #keep the main window open untill root.quit()

