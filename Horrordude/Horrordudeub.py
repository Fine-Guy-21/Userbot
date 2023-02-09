import random
import time
import config
from pyrogram import Client, filters

ub = Client("my_account",
              api_id = config.api_id,
              api_hash = config.api_hash
            )
            
"""@ub.on_message(filters.private)
async def hello(client, message):
    try:
        username = message.from_user.username 
        botval = username[-3]+username[-2]+username[-1]
    except:
        username = None
        botval = None
        
    user = message.from_user.first_name
    if username == "FineContactBot":
        print("@FineContactBot")
    elif username == "Horrordude":
        print("you")
    elif botval == "bot" or botval == "Bot":
        print(username)
    else:
       await message.reply(f" Hello {user} ! \n Please Contact Me through : @FineContactBot")
      # await message.forward(Group_id)
       mes = message
      # await ub.delete_messages(message.chat.id, message.id)
"""
tri = -1001682844722
gameun = "chtwrsbot"
idlecity = "idle_city_bot"
"""@ub.on_message(filters.chat(idlecity))
def check(ub,message):
    try: 
        
        text = message.text
        target = "🎣 Fishing 🎣"
        if target in text :
            print("before")
            message.click(0)
            print("after")
    except :
        print(TypeError)

"""        
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
    except Exception as e:
        print(e)


@ub.on_message(filters.chat(config.Entertainment_chat))
async def forwardmsg(ub,message):
    target = "@Horrordude"
    
    if target in message.text:
        user = message.from_user.mention()
        await  message.reply(f"ehhh. . .  Hi  {user} 👀 ") 
        
        


print("Userbot is running" )
ub.run()


"""
🌲Forest 3min
Many things can happen in the forest.

🍄Swamp 4min
Who knows what is lurking in mud.

🏔Mountain Valley 4min
Watch out for landslides.

🗡Foray 🔋🔋
Foray is a dangerous activity. Someone can notice you and may beat you up. But if you go unnoticed, you will acquire a lot of loot.

📯Arena 
Arena isn't a place for the weak. Here you fight against other players and if you stand victorious, you acquire precious experience.
"""