from fbchat import Client
from fbchat.models import *
from tool import *


class Bot(Client):
    def onFriendRequest(self, from_id=None, msg=None):
        data = {}
        with open('database.json','r',encoding="utf-8") as f:
            data = json.load(f)
        
        helper ='Pour effectuer une recherche sur wikipedia,Envoyer wiki: <Mot clé à rechercher> \n(Exemple: wiki:Google)\nPour afficher le parole d\'une chanson,Envoyer lyrics:<Nom du groupe(ou d\'artiste)=titre> \n(Exemple: lyrics:Avenged sevenfold=Set me free) \nPour suggérer des modifications,Envoyer suggestion: <votre suggestion>'   
            
        self.markAsRead(from_id)
        id = from_id
        print("new message from" + id)
        msgs = msg.text
        if(msg.upper() == "AIDE"):
            self.send(Message(text = helper),thread_id = from_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:5].upper() == "WIKI:"):
            self.send(Message(text = wiki(msg[5:].strip())),thread_id = from_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:11].upper() == "SUGGESTION:"):
            data["suggestion"].append(msg[11:])
            save(data)
            self.send(Message(text = "Nous avons bien reçu votre suggestion!Merci"),thread_id = from_id,thread_type = ThreadType.USER)
        
        elif (msg[:7].upper() == "LYRICS:"):
            self.send(Message(text = lyrics(msg[7:])),thread_id = from_id,thread_type = ThreadType.USER)
        
        
        else:
            self.send(Message(text = "Erreur... Envoyez \"AIDE\" pour apprendre à utiliser le chatbot"),thread_id = from_id,thread_type = ThreadType.USER)
        
        
    def onPendingMessage(self, author_id = None , message_object = None , thread_id = None , thread_type = ThreadType.USER , **kwargs):
        data = {}
        with open('database.json','r',encoding="utf-8") as f:
            data = json.load(f)
        
        helper ='Pour effectuer une recherche sur wikipedia,Envoyer wiki: <Mot clé à rechercher> \n(Exemple: wiki:Google)\nPour afficher le parole d\'une chanson,Envoyer lyrics:<Nom du groupe(ou d\'artiste)=titre> \n(Exemple: lyrics:Avenged sevenfold=Set me free) \nPour suggérer des modifications,Envoyer suggestion: <votre suggestion>'   
            
        self.markAsRead(author_id)
        id = author_id
        print("new message from" + id)
        msg = message_object.text
        if(msg.upper() == "AIDE"):
            self.send(Message(text = helper),thread_id = author_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:5].upper() == "WIKI:"):
            self.send(Message(text = wiki(msg[5:].strip())),thread_id = author_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:11].upper() == "SUGGESTION:"):
            data["suggestion"].append(msg[11:])
            save(data)
            self.send(Message(text = "Nous avons bien reçu votre suggestion!Merci"),thread_id = author_id,thread_type = ThreadType.USER)
        
        elif (msg[:7].upper() == "LYRICS:"):
            self.send(Message(text = lyrics(msg[7:])),thread_id = author_id,thread_type = ThreadType.USER)
        
        
        else:
            self.send(Message(text = "Erreur... Envoyez \"AIDE\" pour apprendre à utiliser le chatbot"),thread_id = author_id,thread_type = ThreadType.USER)
        
        
    def onMessage(self, author_id = None , message_object = None , thread_id = None , thread_type = ThreadType.USER , **kwargs):        
        data = {}
        with open('database.json','r',encoding="utf-8") as f:
            data = json.load(f)
        
        helper ='Pour effectuer une recherche sur wikipedia,Envoyer wiki: <Mot clé à rechercher> (Exemple: wiki:Google)\nPour afficher le parole d\'une chanson,Envoyer lyrics:<Nom du groupe(ou d\'artiste):titre> (Exemple: lyrics:Avenged sevenfold=Set me free) \nPour suggérer des modifications,Envoyer suggestion: <votre suggestion>'   
            
        self.markAsRead(author_id)
        id = author_id
        print("new message from" + id)
        msg = message_object.text
        if(msg.upper() == "AIDE"):
            self.send(Message(text = helper),thread_id = author_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:5].upper() == "WIKI:"):
            self.send(Message(text = wiki(msg[5:].strip())),thread_id = author_id,thread_type = ThreadType.USER)
            
            
        elif (msg[:11].upper() == "SUGGESTION:"):
            data["suggestion"].append(msg[11:])
            save(data)
            self.send(Message(text = "Nous avons bien reçu votre suggestion!Merci"),thread_id = author_id,thread_type = ThreadType.USER)
        
        elif (msg[:7].upper() == "LYRICS:"):
            print(lyrics(msg[7:]))
            self.send(Message(text = lyrics(msg[7:])),thread_id = author_id,thread_type = ThreadType.USER)
        
        
        else:
            self.send(Message(text = "Erreur... Envoyez \"AIDE\" pour apprendre à utiliser le chatbot"),thread_id = author_id,thread_type = ThreadType.USER)
        
        
        


if __name__ == "__main__":
    client = Bot("","")
    client.listen()

    
    
