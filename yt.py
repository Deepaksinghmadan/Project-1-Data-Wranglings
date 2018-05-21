#Downloader GUI
from pytube import YouTube
from tkinter import *

def youtubedl():
	try:
		status.set("Download in progress")
		yt = YouTube(url.get())
		yt.streams.filter(file_extension="mp4").first().download()
		status.set("Download complete for %s" %yt.title)
	except:
		status.set("Download failed.")

root = Tk()
root.title("My YouTube Downloader")

f = Frame()
f.grid(column=0,row=3)

url = StringVar()
status = StringVar()

Label(f,text="Enter YouTube video URL: ",width=60,fg="green").grid(column=0,row=0)
Entry(f,textvariable=url,width=60,bg="yellow").grid(column=0,row=1)
Label(f,textvariable=status,width=60).grid(column=0,row=2)
Button(f,text="Download",command=youtubedl,width=20,bg="purple",fg="white").grid(column=0,row=3)
root.mainloop()



from tkinter import filedialog
from tkinter import * 
import zipfile

root = Tk()
root.title("My WinZip")

def browse():
	root.filename = filedialog.askopenfilename(filetypes=(("All files","*.*"),))
	# f.set(root.filename)
	z = zipfile.ZipFile('output.zip','w')
	z.write(root.filename)
	z.close()

b = Button(root,text="Browse",command=browse)
b.pack()

# f = StringVar()
# l = Label(root,textvariable=f,font=('times',24,'bold'),fg="green")
# l.pack()
root.mainloop()



from tkinter import messagebox
from tkinter import * 

root = Tk()
try:
	messagebox.showinfo("Status","Download complete")
except:
	messagebox.showerror("Status","Download failed")
root.mainloop()
