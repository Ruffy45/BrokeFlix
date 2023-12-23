Overview
Movie Watcher is a Python script that allows users to watch movies or TV shows locally by generating an embed URL from the IMDb ID and optionally specifying the season and episode numbers for TV shows.

Features
IMDb ID Retrieval: Fetches the IMDb ID for a given movie or TV show using the Open Movie Database (OMDb) API.

Local Streaming: Generates an embed URL for the specified IMDb ID, season, and episode (if applicable) to enable local streaming.

Usage
API Key Setup:

Obtain an API key from OMDb API and replace "c826c758" with your actual API key.
Run the Script:

Execute the script by running python main.py in the command line.
The script will prompt you to enter the type of content (movie or TV show) and the title.
Input IMDb ID:

The script will retrieve the IMDb ID for the entered movie or TV show title.
If successful, it will display the IMDb ID.
Optional TV Show Details:

If watching a TV show, the script will ask for the season and episode numbers.
Generate Embed URL:

The script constructs an embed URL using the IMDb ID and optional season/episode details.
Open in Default Browser:

The script uses webbrowser to open the generated embed URL in the default web browser.
Requirements
Python 3.x
requests library: Install using pip install requests
webbrowser module: Built-in module, no separate installation required
Notes
Ensure that you have a valid OMDb API key for IMDb ID retrieval.
The script opens the generated embed URL in the default web browser for local streaming.
Disclaimer
This script is for educational purposes and personal use. Respect the terms of service of external APIs and websites. The author is not responsible for any misuse of the script.

