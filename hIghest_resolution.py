from pytube import YouTube

link = input("Enter link of your video :")
yt = YouTube(link)
stream =yt.streams.get_highest_resolution()
#Choose Download Location
stream.download("D:\\Project")
print("\Downloaded Successfully".upper())
