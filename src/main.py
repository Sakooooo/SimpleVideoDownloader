import requests
import argparse

findargs = argparse.ArgumentParser("[Video Link]")
findargs.add_argument("link", help="Link to video, could be tiktok or youtube")
args = findargs.parse_args()

# debug
# print(args.link)

