import requests
# import config
import json
import urllib.request
import datetime

# headers = {"Authorization": "bearer "+config.client_id, "User-Agent": "ChangeMeClinet/0.1 by YourUsername"}
# #makes a call to the reddit website, specifically to the top pots in the wallpaper subreddit
# response = requests.get("https://oauth.reddit.com/r/wallpapers/top", headers=headers)

# #posts results from this call to the below file
filename = 'results.json'
# with open(filename, 'w') as f:
#     json.dump(response.json(), f, indent=4)

#from this file the data is read and the url file is grabbed
with open(filename, 'r') as f:
   data = f.read()
posts = json.loads(data)
print(posts["data"]["children"][0]["data"]["url_overridden_by_dest"])
url = posts["data"]["children"][0]["data"]["url_overridden_by_dest"]
r = urllib.request.urlopen(url)
with open(str(datetime.date.today()) + ".png", "wb") as f:
    f.write(r.read())