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
data['prompt'] = input("Prompt: ") or "{target_token}"
data["seed"]=int(input("Seed [default:-1]: ") or str(random.randint(0, 2**32)))
data["n_samples"]=int(input("Number of samples [default: 10]: ") or 10)
data["ddim_steps"]=int(input("Steps [default:200]: ") or 200)
data['exhibit_name'] = data['prompt']+'-'+str(data['seed'])+'-'+str(data['n_samples'])+'-'+str(data['ddim_steps'])

#make the request and print it to the console
req = request.Request(url+'jobs/text-to-image', data=par(data))
req.add_header('Authorization', auth)
resp = request.urlopen(req)
print(resp.read())
