import requests
import sys
import time
import os
import webbrowser

def get_imdb_id(movie_title, api_key):
    omdb_url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(omdb_url)
    if response.status_code == 200:
        movie_data = response.json()
        imdb_id = movie_data.get("imdbID")
        return imdb_id
    else:
        print(f"Error getting IMDb ID. Status code: {response.status_code}")
        return None




api_key = "c826c758"

# Ask the user if they're watching a movie or a TV show
show_type = input("Are you watching a movie or a TV show? (Enter 'movie' or 'tv'): ")

# Get the IMDb ID
movie_title = input("Enter the name of the movie or TV show: ")
imdb_id = get_imdb_id(movie_title, api_key)

# for testing
if imdb_id:
    print(f"IMDb ID Found: {imdb_id}")
else:
    print("No IMDb ID found. Exiting...")
    sys.exit()

# Get the season and episode numbers if it's a TV show
season = episode = None
if show_type == 'tv':
    season = input("Enter the season number: ")
    episode = input("Enter the episode number: ")

# Construct the embed URL
embed_url = f"https://multiembed.mov/directstream.php?video_id={imdb_id}"
if season and episode:
    embed_url += f"&s={season}&e={episode}"

print(f"Embed URL: {embed_url}")

# import subprocess

# def play_video_locally(video_url):
#     try:
#         subprocess.run(['mpv', video_url], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")

# # Example usage
# play_video_locally(embed_url)
webbrowser.open(embed_url)