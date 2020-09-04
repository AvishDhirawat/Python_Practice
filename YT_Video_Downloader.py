#!/usr/bin/env python3

# Author - Avish Dhirawat
# Date - 04/09/2000

from pytube import YouTube
import os

youtube_video_url = input("Enter the YouTube video URL : ")
yt_obj = YouTube(youtube_video_url)

try:
    yt_obj = YouTube(youtube_video_url)
    print('Video Title : '+yt_obj.title)
    print('Video Length : '+str(yt_obj.length)+ ' seconds')
    #print('Video Description : '+yt_obj.description)
    print('Video Rating : ',yt_obj.rating)
    print('Video Views Count : ',yt_obj.views)
    print('Video Author : '+yt_obj.author)
    n = input("\n\nYou want to continue [Yes/No] : ")
    if(n == "N" or n == "n" or n == "No" or n== "no"):
        exit()
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    path = os.getcwd()
    filters.get_highest_resolution().download(output_path = path+"/YouTube_Downloads", filename = yt_obj.title)
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
