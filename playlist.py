import os
from yt_dlp import YoutubeDL

def download_playlist(playlist_url, download_path):
    try:
        print("Initializing download with yt_dlp...")
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': os.path.join(download_path, '%(playlist_title)s/%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Playlist downloaded successfully to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_or_playlist_url = input("Enter the YouTube video or playlist link: ").strip()
    download_path = os.path.expanduser("~D:\Toturials")  # Default download path
    print(f"Videos will be downloaded to: {download_path}")
    
    if "list=" in video_or_playlist_url:
        print("Detected a playlist URL. Starting playlist download...")
        download_playlist(video_or_playlist_url, download_path)
    else:
        print("Detected a single video URL. Starting single video download...")
        download_playlist(video_or_playlist_url, download_path)
