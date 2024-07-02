import requests
from random import randint
from dotenv import load_dotenv
import os
import telegram

def get_last_comic_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    last_comic_number = response.json()['num']
    return last_comic_number

def get_random_comic(last_comic_number):
    random_number = randint(1, last_comic_number)
  
    url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    image_url = response.json()['img']
    comments = response.json()['alt']

    image_respone = requests.get(image_url)
    image_respone.raise_for_status()
    image_name = f'image_{random_number}.png'
  
    with open(image_name, 'wb') as file:
        file.write(image_respone.content)
      
    return image_name, comments

def send_comic_to_TG_chat(token, chat_id, image_name, comments):
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=comments)
    with open(image_name, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)
    os.remove(image_name)

if __name__ == '__main__':
    load_dotenv()
    last_comic_number = get_last_comic_number()
    image_name, comments = get_random_comic(last_comic_number)
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    token = os.environ['TELEGRAM_BOT_TOKEN']
    send_comic_to_TG_chat(token, chat_id, image_name, comments)
    

