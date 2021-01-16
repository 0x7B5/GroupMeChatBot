import requests 
import praw
import configparser
from flask import Flask, request

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__, static_url_path="")

bot_name = config['GROUPME']['Bot_Name']
bot_ID = config['GROUPME']['Bot_ID']
bot_host = config['APP']['Host']

@app.route('/', methods=['POST'])
def got_message():
    data = request.get_json()

    if data['name'] != bot_name: 
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)
    
    return "ok", 200



def send_message(message):
  url  = 'https://api.groupme.com/v3/bots/post'
  data = {
          'bot_id' : bot_ID,
          'text'   : message,
         }
  response = requests.post(url, data=data)

if __name__ == "__main__":
    app.run(host=bot_host)
