# This is a simple Python script to download videos, playlists from YouTube.
# Copyright (c) 2022 Vaibhav Ganeriwala

# import modules
from pytube import YouTube

# define function

def getVideo():
    # get the link from the user
    link = input("Enter the link: ")

    # create an object of YouTube
    yt = YouTube(link)

    # get the available resolutions of the video
    videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    list_of_resolution = list(enumerate(videos))
    for i in list_of_resolution:
        print(i)

    resolution = int(input("Enter the resolution: "))

    print("Are you sure you want to download this video? (y/n)")
    choice = input("Enter your choice: ")

    if choice == 'y':
        videos[resolution].download()
        print("Downloaded successfully!")
    elif choice == 'n':
        print("Download aborted!")
    else:
        print("Invalid input!")
        getVideo()

# call the function
getVideo()