# csv to mp3 #

## *Description:* ###

This script takes a .csv file that contains a list of song titles and artist 
names, searches youtube for those songs, grabs links to the songs, and 
downloads videos and converts them to mp3 format.

Allows you to listen to these songs when you don't have internet!

*Not to be used to download music illegally!*
*Please follow local copyright law & support artists*

## *Why:*
Sometimes you don't have an internet connection and this is is an easy & lazy
way to download a couple of songs w/o worrying about looking for torrents for
individual songs or tediously going through a list of songs w/ youtube2mp3.

Not recommended for building a large library--made for getting ~5-15 new songs
to drag to an mp3 player to before going on a run or bike ride

## *Instructions:* ##

### NOTE: This is only verified to work on Linux/MacOS systems.
Windows system can also run this script, but may need some modifications to some commands. Most likely the `source` command below.

0. Clone this repo:
```
$ git clone https://github.com/ChristianStout/csv_to_mp3.git
```

1. Install ffmpeg (https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
You can do so by looking in their (documentation)[https://ffmpeg.org/download.html].
(This guide)[https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg] may also be helpful.

2. Navigate to this repo on your local machine, and create a virtual evnironment.
### Why? 
`pip3` is no longer reccomended to be run directly on a machine, so we create a virtual envirment in the repo directory.

To do so, run this command:
```bash
cd <path-to-this-repo>
python3 -m venv .
source bin/activate
```

### NOTE: The `source` command must be run on any new terminal instance before running the script again.
Otherwise, the installed libraries will not be found.

3. Install needed libraries
Run this command in the repo directory:

```bash
pip3 install yt-dlp bs4 pandas requests lxml 
```

If for any reason when attemping to run the script it says their is a library missing, just run:
```bash
pip3 install <possible-missing-library>
```

4. Create a `csv` with a `song` and `artist` field (case sensitive)
It can have more fields, but it MUST contain those exact field names.

5. Run script
You may want to `cd` into a directory that you want your music. Then with the same terminal instance
that ran the `source bin/active` command, run
`python3 <path-to-repo>/csv_to_mp3.py <path-to-csv-file>`

6. Enjoy!

## Troubleshooting

### I got the wrong song/version
If you notice a song is incorrect, find the exact version's link on youtube, and run:
```bash
python -m yt-dlp -f mp3 <url>
```
This calls yt-dlp directly from the library we downloaded earlier.

### A song is missing/failed
In this case, there will be a `failed_songs.csv` in the directory where you downloaded your music.
There many possible reasons a specific song can fail. It may have been tagged for kids, or it may have
had no results. In this case you will need manual intervention. Run the command in the above section to
manually download the song you want.

### I tried to run this script again in a new terminal instance, but it wont run
Since we are running in a virtual environment, the `source` command *must* be run on any new terminal
instance before running the script again. Otherwise, the installed libraries will not be found.
```
source <path-to-repo>/bin/activate
```

### It says there is a missing library
If for any reason when attemping to run the script it says their is a library missing, in the repo directory, run:
```bash
pip3 install <missing-library>
```


