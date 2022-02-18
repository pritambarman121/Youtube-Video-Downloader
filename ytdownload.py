from pytube import YouTube

link = input("Paste link Here :")
video = YouTube(link)

print("Video Title : ",video.title)

print("Tumbnail Image : ",video.thumbnail_url)

print("Status : Downloading video".upper())
video = video.streams.get_highest_resolution()
              #Select resolution

video.download("D:\Project\Download")
              #Download location
print("\nFile Downloaded & Saved successfully".upper()) 