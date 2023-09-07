from pytube import YouTube
from termcolor import colored
import os

desktop_path = os.path.expanduser("~/Desktop").replace("/", "\\")

greet = """
   <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    <><><><><><><><><><><> Youtube to MP3 <><><><><><><><><><><>
   <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    <><><><><><><><><><> created by: g4m3f4c3 <><><><><><><><><>
   <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""

print(colored(greet, 'red'))

try:
    output_directory = input(colored("Where would you like to download the file? Please enter a path or leave blank to download to Desktop: ", 'yellow')).strip()

    if not output_directory:
        output_directory = desktop_path
    
    print(colored(f"Download path is set to: {output_directory}", 'dark_grey'))
    
    while True:
        url = input(colored("Please enter a Youtube URL: ", 'yellow')).strip()

        video = YouTube(url)
        filename = f"{video.author} - {video.title}.mp3"
        
        print(colored(f"\nDownloading {filename}", 'cyan'))
        print(colored(f"Duration: {round(video.length // 60, 2)}.{video.length % 60} minutes", 'dark_grey'))
        print(colored(f"View Count: {video.views}", 'dark_grey'))
        print(colored(f"Published Date: {video.publish_date}", 'dark_grey'))
        print(colored(f"Thumbnail Image URL: {video.thumbnail_url}", 'dark_grey'))

        stream = video.streams.filter(only_audio=True).first()

        stream.download(output_path = output_directory, filename = filename)

        print(colored(f"\nDownloaded {filename} successfully!", 'green'))
        
        continue_download = input(colored("\nContinue? (y/n): ", 'magenta')).strip()
        
        if continue_download == 'y':
            continue
        else:
            print(colored("\nThanks for using the Youtube to MP3 Converter!", 'blue'))
            break
except:
    print("Unable to fetch video information. Please check the video URL or your network connection.")