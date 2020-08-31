##### Getting module(s)
import requests
import sys
from optparse import OptionParser

# method to be called when the user asks for help
def usage():
  print("""
  
    Usage: spy.py  -u [username] -f [file name]

    REQUIRED:
      -u or --username: Username of the victim

    OPTIONAL:
      -f or --file: the file to output the results into

  """)
  sys.exit()

#Setting up the options for the terminal
parser = OptionParser()
parser.set_conflict_handler("resolve")
parser.add_option("-u", "--username",dest="uname")
parser.add_option("-h", "--help", dest="help", action="store_true")
parser.add_option("-f", "--file", dest="fileName")
(options, args) = parser.parse_args()

# If the username is set, the help menu cannot be shown (if called at the same time)
if options.uname:
  options.help = None

# Run the help menu
### If the username is not defined
if options.uname == None:
  usage()
### If the user has asked for help
if options.help:
  usage()

##### Variables
# Sites
sites = {
  "AboutMe": "https://about.me/{}",
  "Badoo": "https://badoo.com/{}",
  "CodePen": "https://codepen.io/{}",
  "DevCommunity": "https://dev.to/{}",
  "Discogs": "https://www.discogs.com/user/{}",
  "Ello": "https://ello.co/{}",
  "Github": "https://github.com/{}",
  "IFTTT": "https://www.ifttt.com/p/{}",
  "Instagram": "https://www.instagram.com/{}",
  "Keybase": "https://keybase.io/{}",
  "MySpace": "https://myspace.com/{}",
  "PasteBin": "https://pastebin.com/u/{}",
  "Patreon": "https://www.patreon.com/{}",
  "PCPartPicker": "https://pcpartpicker.com/user/{}",
  "Pinterest": "https://www.pinterest.com/{}",
  "Reddit": "https://www.reddit.com/user/{}",
  "SoundCloud": "https://soundcloud.com/{}",
  "Spotify": "https://open.spotify.com/user/{}",
  "Tellonym": "https://tellonym.me/{}",
  "TryHackMe": "https://tryhackme.com/p/{}",
  "Twitch": "https://m.twitch.tv/{}",
  "Twitter": "https://mobile.twitter.com/{}",
  "Wordpress": "https://profiles.wordpress.org/{}",
  "Xbox": "https://xboxgamertag.com/search/{}",
  "Youtube": "https://www.youtube.com/{}",
}

# Headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# Info
print("\n")
print("""
  ===================================
  ||    ----USERNAME LOOKUP----    ||
  ||-------------------------------||
  ||        Creator: IVBecy        ||
  ||-------------------------------||
  || Inspired by sherlock-project  ||
  ||-------------------------------||
  ===================================
""")
print(f"Username: {options.uname}")
print("\n")

#### Appending username to all sites + checking
for i in sites:
  sites[i] = sites[i].format(options.uname)
  if i == "Twitter":
    req = requests.get(sites[i])
  else:
    req = requests.get(sites[i], headers=headers)
  if req.status_code == 200:
    print(f"[+] {i}: {sites[i]}")
    # If we need to write to a file
    if options.fileName:
      f = open(options.fileName, "a")
      f.write(f"{i}: {sites[i]}")
      f.write("\n")
  elif req.status_code == 404:
    print(f"[-] {i}: Not Found")
  else:
    print(f"[-] {i}: Error: {req.status_code} {req.reason}")


