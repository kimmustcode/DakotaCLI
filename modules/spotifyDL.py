import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
from pytube import YouTube 
import os 
import json
import re

api_credentials=("CLIENT_ID","CLIENT_SECRET")
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Module Start 
def mod_start():
    exit = False 

    while exit == False:
        os.system('cls')
        print(r"""
    ,-.       _,---._ __  / \
    /  )    .-'       `./ /   \
    (  (   ,'            `/    /|
    \  `-"             \'\   / |
    `.              ,  \ \ /  |
    /`.          ,'-`----Y   |
    (            ;        |   '
    |  ,-.    ,-'         |  /
    |  | (   |    Spotify | /
    )  |  \  `.___________|/
    `--'   `--'

        """)
        x = input("Spotify Downloader\n--(song)\n--(playlist)\n--(album)\n--(return)\n\n>")
        if x == 'song':
            url = input("Input URL: ")
            songD_p(url)
        elif x == 'playlist':
            url = input("Input URL: ")
            playD_p(url)
        elif x == 'album':
            url = input("Input URL: ")
            albumD_p(url)
        elif x == 'return':
            exit = True 

    return

# Song
def songD_p(url):
    info = sp.track(url)
    search = info['name'] + " - " + info['album']['artists'][0]['name'] + ' lyrics'
    fileName  = info['name'] + " - " + info['album']['artists'][0]['name'] + '.mp3'
    
    output_path="Bay/"
    dlSong(search, fileName, output_path)
    input('Enter to Continue.')
    return

# Playlist
def playD_p(url):
    output_path="Bay/"

    playlist = sp.playlist(url)
    for item in playlist['tracks']['items']:
        if item['track'] != None:
            name = item['track']['name'] + " - " + item['track']['artists'][0]['name']
            search = name + 'lyrics'
            name = re.sub(r"(?u)[^-\w.]", " ", name)
            fileName = name + ".mp3"


            dlSong(search, fileName, output_path)   

    input("Enter to Continue.")

    return 

# Album
def albumD_p(url):
    album = sp.album(url)
    artist = album["artists"][0]["name"]
    foldername = album['name'] + album['release_date'][:4] 
    s = re.sub(r"(?u)[^-\w.]", " ", foldername)
    output_path="Bay/" + s
    try:
        os.mkdir(output_path)
        for track in album['tracks']['items']:
            search = track['name'] + " - " + artist + 'lyrics'
            fileName = track['name'] + " - " + artist + '.mp3'

            dlSong(search, fileName, output_path)
    except: 
        print("Album already in folder")
    input('Enter to Continue.')

    
    return 

# Downloads one song
def dlSong(search, fileName, path):
    # Searches youtube for "Title - Artist Lyrics"
    step = YoutubeSearch(search, max_results=1).to_json()
    results = json.loads(step)

    # URL with the grabbed suffix
    fixedURL = 'https://www.youtube.com' + results['videos'][0]['url_suffix']

    yt = YouTube(fixedURL) 

    # Filter out anything not audio
    video = yt.streams.filter(only_audio=True).first() 

    # Cleans file name to be valid and downloads
    fileName = re.sub(r"(?u)[^-\w.]", " ", fileName)
    video.download(output_path=path, filename=fileName) 

    print(fileName + " downloaded!")
    return 