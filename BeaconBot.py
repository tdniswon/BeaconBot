import requests

params = {    
    'bot_id' : 'b282106da75b494564e7700ba6',
    'text' : 'Xbox',
    'attachments' : [
        {
            "type" : "image",
            "url" : "https://i.groupme.com/836x960.jpeg.45edd5f33c9342e5a9184a64b6d7fa8d"
        }
    ]
}

data = {
    'text' : 'Xbox',
    'picture_url': 'https://i.groupme.com/836x960.jpeg.45edd5f33c9342e5a9184a64b6d7fa8d'
}

r = requests.post('https://api.groupme.com/v3/bots/post', params = params, data = data)
print(r)