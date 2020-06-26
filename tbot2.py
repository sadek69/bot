from websocket import create_connection
import json
import time
import os
import schedule
import telebot
from telebot import types

bot = telebot.TeleBot('your bot token')







totalsell = 0
totalbuy = 0
maxsell = 0
maxbuy = 0

def datareset() :
    totalsell = 0
    totalbuy = 0
    maxsell = 0
    maxbuy = 0





schedule.every().day.at("00:00").do(datareset)

clear = lambda: os.system('clear')

ws = create_connection("wss://api-pub.bitfinex.com/ws/2")
ws.connect("wss://api-pub.bitfinex.com/ws/2")
ws.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')

while True:

    schedule.run_pending()

    result = ws.recv()
    result = json.loads(result)

    if (len(result)) > 2 and (len(result)) < 4 :
         

        os.system('clear')

        if result[2][2] < 0 :
            totalsell = totalsell+result[2][2]
            if maxsell > result[2][2] :
                maxsell = result[2][2]

        if result[2][2] > 0 :
            totalbuy = totalbuy+result[2][2]
            if maxbuy < result[2][2] :
                maxbuy = result[2][2]
        if result[2][2]>=10 or result[2][2] <=-10 :
            bot.send_message(chat_id='your channel id', text='deal volume : '+str(result[2][2])+' price : '+str(result[2][3]))
            bot.send_message(chat_id='your channel id', text='totalbuy : '+str(totalbuy)+' totalsell : '+str(totalsell))

        print('totalbuy : ',totalbuy,'totalsell : ',totalsell)
        print('maxbuy : ',maxbuy,'maxsell : ',maxsell)
        print('last deal ','size : ',result[2][2],'price : ',result[2][3])








bot.polling()
ws.close()
