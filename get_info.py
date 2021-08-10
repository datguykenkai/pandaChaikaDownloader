from requests import get
from bs4 import BeautifulSoup
import os
import sys

def get_download_urls(artist: str):
    dl_url = "https://panda.chaika.moe/search/?title=&tags=artist%3A" + artist + "&filecount_from=&filecount_to=&posted_from=&posted_to=&source_type=&reason=&uploader=&category=&filesize_from=&filesize_to=&sort=public_date&asc_desc=desc&gen-ddl="
    return get(dl_url).text.split('\n')
    

def get_title(url: str):
    soup = BeautifulSoup(get(url[:-9]).content, 'html.parser')
    return soup.select_one(".title-main h5").text

def get_size(url: str):
    soup = BeautifulSoup(get(url[:-9]).content, 'html.parser')
    size_text, size_bytes = soup.select_one("li.subtitle > table > tr:nth-child(2) > td").text.split(",")
    size_bytes = int(size_bytes.strip())
    return size_text, size_bytes

def artist_dir(download_dir:str, artist: str):
    # wd = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(download_dir, f"{artist}") 

def get_artist_name():
    return input("Input artist:").lower().replace(" ", "_")

def get_artist_results(artist: str):
    url_arr = get_download_urls(artist)
    if(url_arr == [""]):
        print("No results for artist")
        sys.exit()
    return url_arr