import requests
import config
import json
import urllib.request
import datetime
import ctypes
import os

headers = {"Authorization": "bearer "+config.client_id, "User-Agent": "ChangeMeClinet/0.1 by YourUsername"}
# #makes a call to the reddit website, specifically to the top pots in the wallpaper subreddit
response = requests.get("https://oauth.reddit.com/r/wallpapers/top", headers=headers)

# #posts results from this call to the below file
filename = 'results.json'
with open(filename, 'w') as f:
    json.dump(response.json(), f, indent=4)

#from this file the data is read and the url file is grabbed
with open(filename, 'r') as f:
   data = f.read()
posts = json.loads(data)
print(posts["data"]["children"][0]["data"]["url_overridden_by_dest"])
url = posts["data"]["children"][0]["data"]["url_overridden_by_dest"]

#the image is then donwloaded, and saved under the filename with today's date
r = urllib.request.urlopen(url)
with open(str(datetime.date.today()) + ".png", "wb") as f:
    f.write(r.read())

#an absolute path to the downloaded image is generated
path = "C:\\Users\\moham\\Desktop\\python_projects\\wallpaper\\"
path += str(datetime.date.today()) + ".png"

#finds files in current directory
files = os.listdir(path)

#finds images saved previously, and deletes those older than three days to
#prevent excessive data hoarding
for file in files:
    if file[-4:] == '.png':
        new_date = (datetime.datetime.strptime(file[:-4], '%Y-%m-%d'))
        #chcecks if date of files are older than three days
        elapsed = datetime.date.today() - new_date.date()
        if elapsed > datetime.timedelta(days= 3):
            os.remove(file)
            continue
        
        
#the ctypes module is used to change the desktop background
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
