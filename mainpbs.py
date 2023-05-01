import os
import yt_dlp

# Define the video URL
video_url = 'https://www.pbs.org/video/watch-call-the-midwife-season-12-starting-february/'

# Create a folder on the user's desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
folder_name = 'CBS'
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Create subfolders for the video and metadata
video_folder_path = os.path.join(folder_path, 'Video')
metadata_folder_path = os.path.join(folder_path, 'Metadata')
os.makedirs(video_folder_path, exist_ok=True)
os.makedirs(metadata_folder_path, exist_ok=True)

# Define yt-dlp options
ydl_opts = {
    'outtmpl': os.path.join(video_folder_path, '%(title)s.%(ext)s'),
    'format': 'best',
    'writethumbnail': True,
    'writeinfojson': True
}

# Download the video and metadata
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# Move the metadata file to the Metadata folder
for file in os.listdir(video_folder_path):
    if file.endswith(".info.json"):
        os.rename(os.path.join(video_folder_path, file),
                  os.path.join(metadata_folder_path, file))

# Print the path to the folder
print('Folder path:', folder_path)
