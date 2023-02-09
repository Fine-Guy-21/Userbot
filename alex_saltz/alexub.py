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
commander = "moonorderbot"

async def Doquest(ub,message,choice = random.choice([0,1,2])):
    try: 
        
        time.sleep(2)
        await message.click(choice)
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

@ub.on_message(filters.command("start"))
async def start(ub, message):
    try:
        await ub.send_message(gameun,"🏅Me")
    except:
        print("unable to send")


@ub.on_message(filters.chat("chtwrsbot"))
async def check(ub,message):
    try: 
        Stamina = "🔋Stamina"
        NoStamina="🔋Stamina: 0/"
        sendMe = "You received"

        if "You were strolling around on your horse" in message.text:
            print ("Foray Found going to stop")
            stoper(ub,message)
            

        elif "🌲Forest 3min 🔥" in message.text or "🌲Forest 4min 🔥" in message.text or "🌲Forest 5min 🔥" in message.text:
            print("fire detected in forest sending order to click forest ")
            await Doquest(ub,message,0)  
        elif "🍄Swamp 4min 🔥" in message.text or "🍄Swamp 5min 🔥" in message.text or "🍄Swamp 6min 🔥" in message.text:
            print("fire detected in swamp sending order to click swamp ")
            await Doquest(ub,message,1) 
        elif "🏔Mountain Valley 4min 🔥" in message.text or "🏔Mountain Valley 5min 🔥" in message.text or "🏔Mountain Valley 6min 🔥" in message.text:
            print("fire detected in valley sending order to click valley ")
            await Doquest(ub,message,2)     

        elif "🌲Forest" in message.text:
            
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
        elif "You are ready to strike" in message.text:
            print("order is set")
        elif "Communication with other castles" in message.text:
            await ub.send_message(gameun,"🛡Defend")
        
        print("over")

    except Exception as e:
        print(e)


@ub.on_message(filters.chat(squad))
def order(ub,message):
    if(message.from_user.username == commander ):
        mes = message.text        
        order = mes[1:3]
        time.sleep(1)
        ub.send_message(gameun,order)
        print("order set successfully")
    else:
        print("Failed")

print("Userbot is running" )
ub.run()
print("go")