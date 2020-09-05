import requests
import json
import xmltodict

def save(data):
    with open('database.json','w',encoding="utf-8") as f:
        json.dump(data , f)

def wiki(query):
    r = requests.get('https://fr.wikipedia.org/api/rest_v1/page/summary/{}'.format(query))
    data = json.loads(r.text)
    if(data["title"].upper() != query.upper()):
        return "{} introuvable,vérifiez l\'orthographe des termes de recherche".format(query)
    else:
        return data["extract"]
    
def lyrics(query):
    artiste,son = artist(query)
    r = requests.get('http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist={}&song={}'.format(artiste.strip(),son.strip()))
    if r.status_code != 200:
        return "Certain parole ne peut pas etre affiché dû a une probleme de \"STOP WORDS\"...Je suis en train de regler cette probleme mais vous pouvez consulter d\'autres paroles "
        
    val = json.dumps(xmltodict.parse(r.text))
    val = json.loads(val)
    if(val["GetLyricResult"]["Lyric"] == None):
        return "{} est introuvable".format(query)
    
    return(val["GetLyricResult"]["Lyric"])

def artist(query):
    i = 0
    while query[i] != "=":
        i +=1
        if i>= len(query):
            break
    
    return query[:i],query[i+1:]
            
if __name__ == "__main__":
    while 1:
        msg = str(input("Message:"))
        if (msg[:7].upper() == "LYRICS:"):
            print(lyrics(msg[7:]))
        else:
            print("error")

