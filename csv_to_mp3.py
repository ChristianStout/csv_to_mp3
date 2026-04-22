#!/usr/bin/env python3

'''
# csv to mp3 #

Original Author: (HarryMaher)[https://github.com/HarryMaher]
Modification By: (ChristianStout)[https://github.com/ChristianStout], 04-22-2026

# The following is the original README. Please read the updated version in `README.md`.

### What it does: ###

This simple script takes a .csv list of popular song titles and artist names
and searches youtube for that song, grabs the first link that isn't an ad and
downloads the video and converts it to mp3 using youtube-dl/ffmpeg.

So you can listen to these songs off the [internet] grid!

### Why: ###
Sometimes you don't have an internet connection and this is is an easy & lazy
way to download a couple of offline songs w/o worrying about torrenting
individual songs or using youtube2mp3 for each individual song.

Not recommended for building a large library - intended for getting a few songs to
drag to my watch and dumb phone so I can listen to a couple new songs while out

*Not to be used to download music illegally!*
*Please follow local copyright law & support artists!!*



### *Instructions:* ###
1. Install ffmpeg (https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
2. Install youtube_dl, pandas, and bs4 with "pip3 install packagename"
3. Create a songs.csv in the same directory as this auto_yt_dl with a "song" and "artist" field
   (see current songs.csv for example of what it should look like)
4. Run this "python csv_to_mp3.py" (may take about a minute per song)
5. Drag the music to your offline device, and enjoy!

Note: It really only works for fairly popular songs that are on youtube.


todo:
- figure out how to get a csv output from spotify
- maybe worry about output song names?
- make into .exe?

credit:
https://stackoverflow.com/questions/30825371/extract-audio-equivalent-for-youtubedl-class

requires:
ffmpeg - google how to install it and put it in the same directory as your
all below modules (youtube_dl, pandas, bs4) - install w/ "pip3 install youtube_dl" and etc.

'''
import yt_dlp as youtube_dl
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import os
import csv

songs_csv = "songs.csv"
cache: dict[str, set[str]] = dict()
failed_csv_rows = ["song", "artist", "error"]

def yt_dler(vid_link):
    # d/l settings
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        # 'quiet': True,
        'restrictfilenames': True
        }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([vid_link])

def reg_failed_song(file, count, e, song, artist):
    writer = csv.writer(file)
    if count == 0:
        writer.writerows(failed_csv_rows)
    writer.writerows([song, artist, f'{e}'])

def main():
    # Modification by ChristianStout - Require commandline args
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: csv_to_mp3 [CSV_FILE]")
        return

    # First argument must be the CSV path, or fail
    songs_csv = args[0]

    if not os.path.isfile(songs_csv):
        print(f"Error: {songs_csv} is not a valid file")
        return

    songs = pd.read_csv(songs_csv)
    i = 0
    failed_songs = open("failed_songs.csv", "w", newline='')
    failed_count = 0
    while i < len(songs["song"]):
        # in case there are any repitions, we want to cache artist and song, and skip any we have already done
        artist = songs["artist"][i]
        song = songs["song"][i]
        if not artist in cache.keys():
            cache[artist] = set()
        if song in cache[artist]:
            print("Duplicate found: {artist} - {song}. Skipping...")
            i += 1
            continue
        cache[artist].add(song)

        this_search = f"{artist} {song} official audio"
    
        try:
            yt_dler(f'ytsearch:{this_search}')
        except Exception as e:
            print("A song failed: {artist} - {song}. Skipping...")
            reg_failed_song(failed_songs, failed_count, e, song, artist)
            failed_count += 1
        i += 1

    if failed_count > 0:
        print("WARNING: Errors occurred during this process, and some songs were not downloaded.")
        print(" The songs are saved to `failed_songs.csv` in this directory.")
        print(" Please refer to the README for instruction on how to download manually.")

    failed_songs.close()

if __name__ == "__main__":
    main()
