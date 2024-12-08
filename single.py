import os
from yt_dlp import YoutubeDL

def download_video(video_url, download_path):
    try:
        print("Initializing download with yt_dlp...")
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Download completed successfully. Video saved to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video link: ").strip()
    download_path = os.path.expanduser("~D:\Toturials")  # download path
    print(f"Videos will be downloaded to: {download_path}")
    download_video(video_url, download_path)



