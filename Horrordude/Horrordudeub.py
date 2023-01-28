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
@ub.on_message(filters.text & filters.chat(config.Entertainment_chat))
async def forwardmsg(ub,message):
    target = "@Horrordude"
    target_word = "hi"
    
    if target in message.text:
        mes  = await  message.reply(f"ehhh. . .  {config.hello} 👀 ") 
        
    elif target_word in message.text:
        await ub.send_message(tri,message.text)
print("Userbot is running" )
ub.run()