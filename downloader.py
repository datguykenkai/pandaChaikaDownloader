import os
from clint.textui import progress
from requests import get
from get_info import artist_dir

def download_file(url, file_path, total_size):
    reply = get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in progress.bar(reply.iter_content(chunk_size=1024), expected_size=(total_size/1024) + 1): 
            if chunk:
                file.write(chunk)
                file.flush()

def create_artist_dir(download_dir:str, artist: str):
    path = artist_dir(download_dir, artist)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created new folder for artist\n")