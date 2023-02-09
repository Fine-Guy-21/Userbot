import random
import time
import config
from pyrogram import Client, filters

ub = Client("my_account",
              api_id = config.api_id,
              api_hash = config.api_hash
            )
my_id = 5326184240

class Status :
    online:bool

status = Status() 


@ub.on_message(filters.regex('.status'))
def statuschecker(ub,message):
    try:

        text  = message.text.split(" ")[1]
        if text =="F" or text == "f" :
            status = False
            print("afk")
        elif text == "O" or text == "o":
            status = status.online
            print("nafk")
            print(status)
            
        else :
            print("Confused")  
    except Exception as e:
        print(e)



@ub.on_message(filters.private)
def Meet(ub,message):
    if not status.online:
        if message.from_user.id != my_id:
            time.sleep(2)
            message.reply(f"hello there {message.from_user.first_name},\n Please kindly wait till I'm back Online")
        else :
            print("your message")
    else :
        print("Online")



@ub.on_message(filters.regex('.a'))
def animate(ub,message):
    try:
        text = message.text.split(" ")[1]
        ub.delete_messages(message.chat.id,message.id)
        if message.from_user.id != 5326184240:
            if len(text) <= 12 : 
                mes = ub.send_message(message.chat.id," R_E_A_D_Y ")
                text2 = " "
                for x in text:
                    if x == " " :
                        text2 = text2 + "_"
                    else :
                        text2 = text2 + x
                    ub.edit_message_text(chat_id = message.chat.id, message_id=mes.id, text = text2)
                    time.sleep(0.5)  
            else :
                        print("error")
        else:
            message.reply("👀")
    except Exception as e:
        print(e)




print("Userbot is running" )
ub.run()
print("go")