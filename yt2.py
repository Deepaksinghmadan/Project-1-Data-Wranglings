'''
# pip install pytube
# url = input("Enter video url: ")
# print(yt.thumbnail_url)
from pytube import YouTube
from tkinter import *
def youtubedl():
	print(status.set("Download in progress"))
	try:
		link = url.get()
		yt = YouTube(link)
		# videotitle.set(yt.title)
		videos = yt.streams.filter(file_extension="mp4").all()
		count = 0
		res = resolution.get()
		for i in videos:
			if i.resolution==res:
				count += 1
				if count<= 1: i.download(r"C:\Users\Arun\Desktop\videos")
				else: break
		status.set("Download complete.")
	except:
		status.set("Download failed.")
root = Tk()
f = Frame()
f.grid(column=1,row=3)
url = StringVar()
resolution = StringVar()
videotitle = StringVar()
status = StringVar()
Label(f,text="Enter YouuTube URL: ").grid(column=0,row=0)
Label(f,text="Enter video resolution: ").grid(column=1,row=0)
Entry(f,textvariable=url).grid(column=0,row=1)
Entry(f,textvariable=resolution).grid(column=1,row=1)
Label(f,textvariable=videotitle).grid(column=0,row=2)
Label(f,textvariable=status).grid(column=0,row=3)
Button(f,text="Download",command=youtubedl).grid(column=1,row=4)
root.mainloop()
'''