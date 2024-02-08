'''from youtube_video_viewer_bot import *
youtube.watch_video(time='160', video_url='https://www.youtube.com/watch?v=LMmuChXra_Mhttps://www.youtube.com/watch?v=NK1BM-HREiI&pp=ygUQYWZyZWVuIGluIGxvbmRvbg%3D%3D') #provide time in seconds'''
import webbrowser
import time
import os

'''url = input("Enter the youtube URL:")'''
url = 'https://www.youtube.com/watch?v=NK1BM-HREiI&pp=ygUQYWZyZWVuIGluIGxvbmRvbg%3D%3D'
refresh = input("Enter the refresh time in seconds:")
count = input("How many views do you want? ")


def openURL():
    webbrowser.open(url)
    time.sleep(int(refresh))

    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()

openURL()