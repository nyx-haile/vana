import urllib.request as request
from urllib import parse as parse
import json
import random


def par(data):
	return parse.urlencode(data).encode()

url="https://api.vana.com/api/v0/"

#Read the authentication file
f = open('auth', 'r')
auth = f.read()
f.close()

g = open('email', 'r')
email = g.read()
g.close()

#Generate test request to check if auth token is valid.
req = request.Request(url+"account/balance")
req.add_header('Authorization', auth)
resp = request.urlopen(req)
print(resp.read())

#Take user input for request data
data = {}
data['email']=email

data['prompt'] = input("Prompt: ")
data["seed"]= int(input("Seed [default:-1]: ") or "-1")
data["n"]= int(input("Number of samples [default: 6]: ") or 6)
data["numberOfSteps"] = int(input("Steps [default:200]: ") or 200)
data['exhibitId'] =  data['prompt']+'-'+str(data['seed'])+'-'+str(data['n'])+'-'+str(data['numberOfSteps'])

#make the request and print it to the console

req = request.Request("https://api.vana.com/api/v0/images/generations", data=par(data))
print(par(data))
req.add_header('Authorization', auth)
resp = request.urlopen(req)
print(resp.read())

#Sharp Focus, studio photo, intricate details, highly detailed, cinematic, perfect composition, beautiful octane render, 8k, concept art, perfect light, soft natural perfect cinematic volume light,

# content, context, similarities

"lo-fi pixel art high quality poster of {target_token}, solid background, retro poster portrait, aesthetic image, interesting fun cute pastel colors, happy image, smile, amazing art, video game art, pastel colors, sharp image, 64-bit, polygon, mario, zelda, sega, nintendo, retro game"
"8bit retro pixel art style poster of {target_token} clear design, pastel colors vibrant exciting fun design, happy cheerful 1980s retro video game art style, nintendo pokemon mario sonic sega street fighter"
"A die-cast poster of {target_token}, old advertisement, 1950 1960 1970 poster, bright colores die-print high contrast vivid bright image, 8k high quality image"
