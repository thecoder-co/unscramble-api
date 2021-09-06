from fastapi import FastAPI
import unscramble as unc
import time
import  requests
app = FastAPI()

@app.get("/")
async def root():
    return {"details": "UnscrambleAPI...   baseurl/unscramble/<word>/<length>"}

@app.get("/unscramble/{word}/{length}")
async def unscramble_len(length: int,word):
    start = time.time()
    words = unc.main(length, word)
    end = time.time()
    timed = end - start
    return {"words": words, "time": timed}

#@unscrmamble.get("/search/{word}")
#def search(word):
#    start = time.time()
#    app_id = '9d7691cf1c35eafb5194dbb6a49b1932ed0f19de'
#    app_key = '9d7691cf1c35eafb5194dbb6a49b1932ed0f19de'
#    language = 'en-gb'
#    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word.lower()
#    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
#    end = time.time()
#    timed = end - start
#    return r.json()

