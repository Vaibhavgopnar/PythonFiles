from pytube import YouTube
link = "https://www.youtube.com/watch?v=E-vYa8aRX4A"
youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all()   # all format videos and audios

videos = youtube_1.streams.filter(only_audio=True) # audio only

vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter : "))
videos[strm].download()
print("Successfully downloaded")

# ***** PlayList download *****

# from pytube import Playlist

# py = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()
