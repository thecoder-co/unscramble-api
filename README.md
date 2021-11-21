# Unscramble API
unscramble api with fast api

Finds all length anagrams in strings, therefore unscrambling the string

https://unscramble.deta.dev/ 

# How to use

https://unscramble.deta.dev/unscramble/{word} 

optional parameters: length... defines maximum length of returned words

baseurl/unscramble/{word}?length={length}

## Example response

{"string":"test","unscrambled_words":["e","es","est","et","s","se","set","sett","st","stet","t","te","test","ts","tst"],"time":0.5432431697845459}

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy)
