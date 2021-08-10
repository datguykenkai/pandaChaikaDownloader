from easygui import diropenbox

def get_download_range(num_url: int):
    while True:
        try:
            download_start, download_end = input(f"Enter download start and end (Format: start end) (inclusive) (Total: {num_url}): ").strip().split(" ")
            download_start = int(download_start)
            download_end = int(download_end)
            if(download_end <= num_url and download_start >= 1 and download_start <= download_end):
                return download_start, download_end
            print("Invalid numbers \n")
        except ValueError:
            print("Invalid numbers \n")

def get_confirm_download():
    while True:
        confirm = input("Download (y/n):")
        if(confirm == "y"):
            return True
        elif(confirm == "n"):
            return False
        
        print("invalid value")

def get_download_dir():
    return diropenbox()
    # return input("Folder to put downloads to:")