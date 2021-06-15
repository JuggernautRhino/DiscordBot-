import requests
import json
import yt_search

def reverse(string):
    revstring = ''
    index = len(string)
    while index > 0:
        revstring += string[index -1]
        index = index -1
    return revstring 
    
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_quote_today():
  response = requests.get("https://zenquotes.io/api/today")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_alot_quotes():
  response = requests.get("https://zenquotes.io/api/quotes")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def yturl(url):
    start = "https://www.youtube.com/watch?v="
    youtubeurl = start + str(url)
    return youtubeurl

def make_a_word(b1,b2,b3,b4,b5,b6):
    if b6 == "0":    
        if b5 == "0":    
            if b4 == "0":
                if b3 == "0":
                    if b2 == "0":
                        if b1 == "0":
                            ba = "0"
                        else:ba = b1
                    else:ba = b1 + " " + b2
                else:ba = b1 + " "+ b2 + " " + b3
            else:ba = b1 +" "+b2+" "+b3+" "+b4
        else:ba = b1 +" "+b2+" "+b3+" "+b4 + " " + b5
    else:ba = b1 +" "+b2+" "+b3+" "+b4 + " " + b5 + " " + b6
    return ba


def _search(b1,b2 = "0",b3 = "0",b4 = "0",b5 = "0",b6 = "0"):
    yt = yt_search.build("AIzaSyBNsZ6TUJVBP61YAUtvoOwh28mtSxWlC3I")
    term = make_a_word(b1,b2,b3,b4,b5,b6)
    search_result = yt.search(term, sMax=1, sType=["video"])
    url = (search_result.videoId)
    title = (search_result.title)
    url = url[0]
    fullurl = yturl(url)
    print(f"Person is adding this song to queue: {fullurl}, with the term: {term}")
    return fullurl, title
