from fastapi import FastAPI
import unscramble as unc
import time
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Unscramble API</title>
        </head>
        <body>
            <h1>API to get word anagrams</h1>
            <p>baseurl/unscramble/{word}</p>
            <p>optional arguments: length... defines maximum length of returned words</p>
            <p>baseurl/unscramble/{word}?length={length}</p>
        </body>
    </html>
    """

@app.get("/unscramble/{word}")
def unscramble(word: str, length: Optional[int] = None):
    if length:
        start = time.time()
        words = unc.main(length, word)
    else:
        start = time.time()
        words = unc.main(len(word), word)
    return {"string": word, "unscrambled_words": words, "time": time.time() - start}
