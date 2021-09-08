from fastapi import FastAPI
import unscramble as unc
import time
app = FastAPI()

@app.get("/")
def root():
    return {"details": "UnscrambleAPI...   baseurl/unscramble/<word>/<length>"}

@app.get("/unscramble/{word}/{length}")
def unscramble_len(length: int,word):
    start = time.time()
    words = unc.main(length, word)
    end = time.time()
    return {"words": words, "time": end - start}
