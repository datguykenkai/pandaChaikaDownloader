import os

from get_info import get_artist_name, get_artist_results, get_size, get_title, artist_dir
from user_input import get_confirm_download, get_download_range, get_download_dir
from downloader import download_file, create_artist_dir

def main():
    term_size = os.get_terminal_size()

    artist = get_artist_name()
    
    url_arr = get_artist_results(artist)
    download_start, download_end = get_download_range(len(url_arr))

    print("_" * term_size.columns)
    
    total_size = 0
    print("\nPreview: (Individual sizes are not completely accurate)\n")
    for count, url in enumerate(url_arr[download_start-1:download_end], 1):
        title = get_title(url)
        size_text, size_bytes = get_size(url)
        total_size += size_bytes
        print(f"{download_start-1 + count}. {title}  |  {size_text}")

    
    print("_" * term_size.columns)
    print(f"Total size: {round(total_size/1024, 2)}MB  |  {round(total_size/1073741824, 2)}GB")
    print("_" * term_size.columns)

    confirm_download = get_confirm_download()

    if(confirm_download):
        download_dir = get_download_dir()
        create_artist_dir(download_dir, artist)
        for count, url in enumerate(url_arr[download_start-1:download_end], 1):
            title = get_title(url)
            size_text, size_bytes = get_size(url)
            print(f"{download_start-1 + count}. {title}")
            download_file(url, artist_dir(download_dir, artist)+fr"/{title}.zip", size_bytes)

if __name__ == "__main__":
    main()
