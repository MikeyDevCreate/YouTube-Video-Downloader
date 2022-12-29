from pytube import YouTube

link = str(input("Enter link to the YouTube video: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()

stream.download()

print("Download was Successful!")