import random
import time
import config
from pyrogram import Client, filters

ub = Client("my_account",
              api_id = config.api_id,
              api_hash = config.api_hash
            )

gameun = "chtwrsbot"
squad = -1001795432674
async def Doquest(ub,message):
    try: 
        time.sleep(2)
        await message.click()
        #x`random([0,1,2]),0)
        time.sleep(1)
        #await ub.request_callback_answer(chat_id=message.chat.id, message_id=message.id,
         #                                callback_data=message.reply_markup[random.choice([0,1,2])][0].callback_data)

        print("message cicked")
    except Exception as e:
        print(e)

def stoper(ub,message):
    try:
        time.sleep(20)
        message.click(0)
        print("foray stoped")
    except:
        print("Unable to click !")

@ub.on_message(filters.chat("chtwrsbot"))
async def check(ub,message):
    try: 
        Quest = "🌲Forest"
        Quest2 = "🍄Swamp"
        Quest3 = "🏔Mountain"
        Stamina = "🔋Stamina"
        NoStamina="🔋Stamina: 0/"
        foray = "You were strolling around on your horse"
        sendMe = "You received"

        if foray in message.text:
            print ("Foray Found going to stop")
            stoper(ub,message)
        elif Quest in message.text or Quest2 in message.text or Quest3 in message.text:
            print("going to quest")
            await Doquest(ub,message)
        elif NoStamina in message.text:
             print("You run out of stamina")
        elif Stamina in message.text:
            time.sleep(1)
            await ub.send_message(message.chat.id,"🗺Quests")
        elif sendMe in message.text:
            time.sleep(2)
            await ub.send_message(message.chat.id,"🏅Me")
            
        
        print("over")
    except Exception as e:
        print(e)


@ub.on_message(filters.chat(squad))
def order(ub,message):
    try:
            if message.from_user.username == "Fine_guy_21":#moonorderbot":
                mes = message.text 
                ub.send_message(408101137,"/effects")

    except Exception as e:
        print(e)    


print("Userbot is running" )
ub.run()
print("go")