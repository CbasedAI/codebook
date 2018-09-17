import requests
from wxpy import *
import json

def talks_robot(info = '你叫什么名字'):
    api_url = 'http://www.tuling123.com/openapi/api'
    #在这里插入你的API_KEY即可
    api_key = '0ddb4721baa54faaa42c107fdcdf49cc'
    data = {'key': api_key,
                'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys

bot = Bot()
@bot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_robot(info=message)
    return replys

embed()