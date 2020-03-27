
from urllib.request import urlopen

jsonurl = urlopen('https://udacity-picasso.auth0.com/.well-known/jwks.json')

s = jsonurl.read()

print(s)




# import urllib.request




# with urllib.request.urlopen("https://udacity-picasso.auth0.com/.well-known/jwks.json") as url:
#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)