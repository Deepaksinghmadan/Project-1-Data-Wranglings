pip install pytube
import pytube
url=input("Enter The URL")
yt=pytube.Youtube(url)
videos=yt.streams.filter(file_extension="mp4").all()
for i in videos:
	if i.resolution=="360p":
		i.download()
		break
print("Downloading %s successful" %y)