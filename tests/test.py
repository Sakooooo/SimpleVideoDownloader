import os
import colorama

# har har har har
colorama.init()

youtube = os.path.isfile("videos/youtube/video.mp4")
tiktok = os.path.isfile("videos/tiktok/video.mp4")

# Check if regular works
os.system("python src/main.py")
print(colorama.Fore.BLUE + "No args test complete!")

# Youtube Download test
# TODO:: Finish this
