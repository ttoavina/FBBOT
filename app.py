import requests
from fbchat import Client
from fbchat.models import *
import json

def wiki(query):
	r = requests.get('https://fr.wikipedia.org/api/rest_v1/page/summary/{}'.format(query))
	data = json.loads(r.text)
	print(data)
	print(data)
	if(data["title"].upper() != query.upper()):
		return "{} introuvable,vérifiez l\'orthographe des termes de recherche".format(query)
	return data["extract"]



class Bot(Client):
    def onMessage(self, author_id = None , message_object = None , thread_id = None , thread_type = ThreadType.USER , **kwargs):        
        res = ''
        self.markAsRead(author_id)
        id = author_id
        print("new message from" + id)
        msg = message_object.text
        print(msg)
        self.send(Message(text = wiki(msg)),thread_id = author_id,thread_type = ThreadType.USER)
        


if __name__ == "__main__":
    client = Bot("ttokiniainatoavina3@gmail.com","jakal000002")
    client.listen()

    
    