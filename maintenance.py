from fbchat import Client
from fbchat.models import *
import json
from tool import *

data = {"maintenance":[],"suggestion":[]}



class Bot(Client):
    def onMessage(self, author_id = None , message_object = None , thread_id = None , thread_type = ThreadType.USER , **kwargs):        
        data =  {}
        with open("database.json",'r',encoding="utf-8")as f:
            data = json.load(f) 

        self.markAsRead(author_id)
        id = author_id
        if author_id not in data["ID"]:
            data["ID"].append(author_id)
            save(data)
            

        self.send(Message(text = "Maintenance en cours..."),thread_id = author_id,thread_type = ThreadType.USER)
        


if __name__ == "__main__":
    msg = 'Le chatbot est de nouveau disponible avec des nouvelles fonctionnalites...\n Envoyez AIDE por plus d\'information'
    client = Client("ttokiniainatoavina3@gmail.com","jakal000003")
    data =  {}
    with open("database.json",'r',encoding="utf-8")as f:
        data = json.load(f) 
    
    for obj in data["ID"]:
        client.send(Message(text = msg),thread_id = obj,thread_type = ThreadType.USER)
    
    

    
    