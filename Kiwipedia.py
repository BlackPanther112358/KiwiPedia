client_id = "RMXy-SFKr8q61EUEdG2cDA"
secret_key = "tc1C9XNg9HpKlMIxHxV12uVQ9RLfVg"

import requests, json
auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

data = {  
    "grant_type": "password",
    "username": "abhay21508",
    "password": "apiproject"
}

headers = {"User-Agent": "Abhay200010"}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth = auth, data = data, headers = headers)

token = res.json()['access_token']
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {token}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

x = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)
print(x.json())
# import requests, json

# # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
# auth = requests.auth.HTTPBasicAuth('tn-A6UAOUcTqwGW9d-XErg', 'd-FjQO7mQ2rKCZF23A5RWgnE6Doegg')

# # here we pass our login method (password), username, and password
# data = {'grant_type': 'password',
#         'username': 'abhay21508',
#         'password': 'apiproject'}

# # setup our header info, which gives reddit a brief description of our app
# headers = {'User-Agent': 'Kiwipedia_reddit_info'}

# # send our request for an OAuth token
# res = requests.post('https://www.reddit.com/api/v1/access_token',
#                     auth=auth, data=data, headers=headers)
# print(res.text)
# reddit = praw.Reddit(client_id='RMXy-SFKr8q61EUEdG2cDA', client_secret='tc1C9XNg9HpKlMIxHxV12uVQ9RLfVg', username='abhay21508', password='apiproject', user_agent='useragentforapi')


# # print(reddit.read_only)
# subreddit = reddit.subreddit('python')

# hot_python = subreddit.hot(limit=5)

# for el in hot_python:
#     print(el)
