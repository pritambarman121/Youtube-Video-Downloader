from numpy import choose
from pytube import YouTube
url = input("\nenter your url :".upper())
link = YouTube(url)
video = link.streams.all()
i = 1
for stream in video:
    print(f"{str(i)} -> {str(stream)}")
    i += 1

stream_number = int(input("\nEnter number : "))
choose_format = video[stream_number-1]
location = input("Paste Download Path Location :")
choose_format.download(location)
print("\nfile downloaded & saved successfully at".upper()+location)