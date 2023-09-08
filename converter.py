from pytube import YouTube
from termcolor import colored
import os

def print_greet():
    greet_text = """
     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗██████╗ ██████╗ ████████╗██████╗ ██████╗ 
    ██╔════╝██╔═████╗████╗  ██║██║   ██║╚════██╗██╔══██╗╚══██╔══╝╚════██╗██╔══██╗
    ██║     ██║██╔██║██╔██╗ ██║██║   ██║ █████╔╝██████╔╝   ██║    █████╔╝██████╔╝
    ██║     ████╔╝██║██║╚██╗██║╚██╗ ██╔╝ ╚═══██╗██╔══██╗   ██║    ╚═══██╗██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ██████╔╝██║  ██║   ██║   ██████╔╝██║  ██║
    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝
                                created by: g4m3f4c3
    """
    print(colored(greet_text, 'red'))
    

def print_video_info(video, filename):
    duration = f"{round(video.length // 60, 2)}.{video.length % 60}"
    
    print(colored(f"\nDownloading {filename}", 'cyan'))
    print(colored(f"Duration: {duration} minutes", 'dark_grey'))
    print(colored(f"View Count: {video.views}", 'dark_grey'))
    print(colored(f"Published Date: {video.publish_date}", 'dark_grey'))
    print(colored(f"Author: {video.author}", 'dark_grey'))
    print(colored(f"Thumbnail Image URL: {video.thumbnail_url}", 'dark_grey'))


def run():
    try:
        output_directory = input(colored("Where would you like to download the file? Please enter a path or leave blank to download to Desktop: ", 'yellow')).strip()

        # Set the output directory to desktop by default
        if not output_directory:
            output_directory = os.path.expanduser("~/Desktop").replace("/", "\\")
        
        print(colored(f"Download path is set to: {output_directory}", 'dark_grey'))
        
        while True:
            url = input(colored("Please enter a Youtube URL: ", 'yellow')).strip()

            video    = YouTube(url)
            filename = f"{video.title}.mp3"
            
            print_video_info(video, filename)

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
        
        
print_greet()
run()