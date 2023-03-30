import argparse

parser = argparse.ArgumentParser("[LINK]")
parser.add_argument("link", help="Link to video (Youtube, Tiktok)")
args = parser.parse_args()

# debug
# this makes it print twice
#print(args.link)
