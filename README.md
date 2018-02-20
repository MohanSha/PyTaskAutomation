# PyTaskAutomation
A list of scripts to automate your daily tasks

<img src="https://media.giphy.com/media/RPZu7v6zA2WOI/giphy.gif" width="700"/>


# How to use the files
1. Make sure you have Python 2.x or 3.x and pip installed on your machine.
2. Run the command to install the necessary packages.
> pip install -r requirements.txt 

## Torrent Downloader
1. Download the *torrent_downloader.py* file and save it any directory that you wish.
2. Run the file using
> python torrent_downloader.py
3. In the same directory, you will find a *test.txt* file which contains the magnet link of your selected torrent. Open your torrent client. Click on the icon resembling [--] i.e Add torrent from URL.
   Copy the entire magnet link and paste it in the box provided and your torrent will start streaming. I've done it for one the proxies of the pirate bay and they have stopped providing *.torrent* files.
   If you manage to get the *.torrent* file, you can automate the last step as well. I'll stick with the magnet link.

## Downloads folder cleaner
1. Download the *clean_folder.py* file and save it in your *Downloads* directory.
2. Run the file using
> python clean_folder.py
3. Your files will be arranged. You can add more extensions in the code if you like.


## MovieDB and subtile renamer
1. Download the *movie_db_and_subs_renamer.py* and paste it in your *Movies* directory if you have one.
2. Run the file using 
> python movie_db_and_subs_renamer.py
  * I haven't considered all the cases of movie names here. This'll work best if you have a folder of movies with folder names containing only the respective movie name and year of release or just the movie name.
    This script can be improved further by forming a regex to match any folder name and extracting only the movie name from it.

## Cleverbot

A chatbot created using cleverbot API.

## Full Contact

Takes email ID as input and provides information like Full name, address, etc., using FullContact API.

## IPL

Get the ipl updates at every 30 seconds.

## Quora

It enables you to use quora from cmd/terminal/shell. It will ask you to enter any question that you need to search on quora, then according to that it will search some(8-10) relevant questions from which you can select a question and after that it will give you an answer of that question. Lastly it'll ask you whether you want more answers(y/n), if you choose 'y' then it'll redirect you to that Quora page where the question and its answers are present.

## Wolfram Bot

Wolfram Alpha is an online service that answers factual queries directly by computing the answer from externally sourced "curated data".Using it's API, this provides various no. of services.

## Youtube

The program takes name of a song then it will open your default web-browser and it will play that song on youtube.

## Kiara

A mini digital assistant to which can give you information like general questions, weather news, math, and wikipedia info of that topic.It has Text-To-Speech feature.

## Lorem Ipsum

Generate one paragraph of short lorem ipsum using loripsum.net API.

## Youtube Crawler

This is a python script which lets the user download the mp3 type audio file of any video of youtube. It also gives the user an option to download the lyrics in a text file if the video is a song. It makes it very easy for the user to download a video/song of his choice as it just asks the user to enter the name of the video.The results get better and more precise if the user specifies the name of the artist as well.

## Earthquake Alert

Monitoring earthquakes around the planet using data from [https://earthquake.usgs.gov/](https://earthquake.usgs.gov/).

