import requests
import json


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
