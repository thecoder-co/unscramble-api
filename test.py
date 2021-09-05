import requests
import json
app_id = "5c7beb4f"
app_key = "787014af77f3cdcf57ea131f4ee21bf4414741c6"
language = "en-gb"
word_id = "example"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r)