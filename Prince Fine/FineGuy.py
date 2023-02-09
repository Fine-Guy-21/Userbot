import random
import time
import config
from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.raw import functions ,types
from googletrans import Translator 

ub = Client("my_account",
              api_id = config.api_id,
              api_hash = config.api_hash
            )

gameun = "chtwrsbot"
gamedos = "idle_city_bot"
squad = -1001795432674
commander = "moonorderbot"
MoonCastle = -1001140588463
MoonMob = -1001408823679
me = 758704198

"""         Functions           """

                   
def calculator(word):
    result = ""
    if len(word) > 2 :
        if len(word) % 2 == 0:
            max = int(len(word)/2) 
            for i in range(0,max):
                res = int(word[i]) + int(word[len(word)-1-i])
                result = result + str(res)
            return calculator(result)      
            
        else:
            max = int(len(word)/2)
            for i in range(0,max):
                res = int(word[i]) + int(word[len(word)-1-i])
                result = result + str(res) 
                if i == max-1:
                    result = result + str(word[max])
            return calculator(result)
            
    else:
        return (word)

def appearance(sentence):  
    Numbers = ""
    checked_letters = []
    for x in sentence:
        counter = 0
        if x == " ":          
            continue
        elif x not in checked_letters:
            for y in sentence:                      
                if y == " ":
                    continue
                elif y == x :
                    counter += 1
                else:
                    continue
            Numbers = Numbers + str(counter)
            checked_letters.append(x)
        else:
            continue
    return Numbers  

def SentenceGenerator(male , female):
    male= male.lower()
    female= female.lower()
    Sentence = f"{male} loves {female}" 
    sentence2 = f"<b>{male}</b> <i>loves</i> <b>{female}</b>"
    result = calculator(appearance(Sentence))
    mes = ( f"{sentence2} : <b>{result}% </b>.")
    
    return mes

def stoper(ub,message):
    try:
        message.pin()
        time.sleep(20)
        message.click(0)
        print("foray stoped")
    except:
        print("Unable to click !")



"""         Chat Wars           """


@ub.on_message(filters.chat(gameun))
def Chatwars(ub,message):
    try: 
        if "You were strolling around on your horse" in message.text:
            print ("Foray Found going to stop")
            stoper(ub,message)

       # elif "You are ready to strike" in message.text:
        #    print("order is set")

        elif "Communication with other castles" in message.text:
            ub.send_message(gameun,"🛡Defend")

    except Exception as e:
        print(e)

@ub.on_message(filters.chat(MoonCastle)& filters.chat(MoonMob))
def MobFight(ub,message):
    if "lvl.65" in message.text:
        ub.send_message(gameun,message.text) 
    elif "lvl.66" in message.text:
        ub.send_message(gameun,message.text)

@ub.on_message(filters.chat(squad))
def order(ub,message):
    if(message.from_user.username == commander ):
        mes = message.text        
        order = mes[1:3]
        time.sleep(1)
        ub.send_message(gameun,order)
        print("order set successfully")
    else:
        print("Other Members message")


"""   IDLE CITY   """


"""
@ub.on_message(filters.chat(gamedos))
def Idlecity(ub,message):


"""



"""     FINE GUY     """
"""@ub.on_message(filters.regex('.afk'))
def status(ub,message):
    text = message.text
    if text.split(" ")[1] == "off" or text.split(" ")[1] == "Off":
        ub.invoke(functions.account.UpdateStatus(offline=True)) 
        print ("Offline = True")
    elif text.split(" ")[1] == "on" or text.split(" ")[1] == "On":
        ub.invoke(functions.account.UpdateStatus(offline=False))
        print("Offline = False")
"""

@ub.on_message(filters.regex('.match'))
def LoveCal(ub,message):
            name = message.text
            ub.delete_messages(message.chat.id,message.id)
            time.sleep(10)
            user1 = name.split(" ")[1]
            user2 = name.split(" ")[2]
            mes = SentenceGenerator(user1,user2)
            mes2 = SentenceGenerator(user2,user1)
            res = f"\t Love Calculator:  \n {mes} \n while \n {mes2}" 
            message.reply(res)

@ub.on_message(filters.regex('.speak'))
def TTS(ub,message):
    if message.from_user.id == me :
        if (message.reply_to_message) :
            if(message.reply_to_message.text):
                text=message.reply_to_message.text
                ub.delete_messages(message.chat.id,message.id)
                voice=gTTS(text=text,lang='en',tld='com.au')
                voice.save("voice.mp3")
                ub.send_voice(message.chat.id,"voice.mp3",caption="australian")
              

@ub.on_message(filters.regex('.hablar'))
def TTS(ub,message):
       if message.from_user.id == me :
        if (message.reply_to_message) :
            if(message.reply_to_message.text):
                text=message.reply_to_message.text
                ub.delete_messages(message.chat.id,message.id)
                voice=gTTS(text=text,lang='es',tld='es')
                voice.save("voiceEs.mp3")
                ub.send_voice(message.chat.id,"voiceEs.mp3", caption=text)           

@ub.on_message(filters.regex('.getme'))
def Get_me(ub,message):

    ub.delete_messages(message.chat.id,message.id)
    if(message.reply_to_message):
        uid = str(message.reply_to_message.from_user.id)
        try:
            ufn = message.reply_to_message.from_user.first_name
        except:
            ufn = "Unknown"
        try:
            uln = message.reply_to_message.from_user.last_name
        except:
            uln = "Unknown"
        try:
            uun = "@" + message.reply_to_message.from_user.username
        except:
            uun = "Unknown"
        
        message.reply(
                        text = "<u><i>User Information</i></u> \n\n"+
                        f"<b>User ID  </b> : <i>{uid} </i>;"+
                        f"\n<b>User FirstName</b>: <i>{ufn} </i>;"+
                        f"\n<b>User LastName</b>: <i>{uln}</i> ;"+
                        f"\n<b>User Username</b>: <i> {uun} </i>;")
    else:
        uid = str(message.from_user.id)
        try:
            ufn = message.from_user.first_name
        except:
            ufn = "Unknown"
        try:
            uln = message.from_user.last_name
        except:
            uln = "Unknown"
        try:
            uun = "@" + message.from_user.username
        except:
            uun = "Unknown"
        
        message.reply(
                        text = "<u><i>User Information</i></u> \n\n"+
                        f"<b>User ID  </b> : <i>{uid} </i>;"+
                        f"\n<b>User FirstName</b>: <i>{ufn} </i>;"+
                        f"\n<b>User LastName</b>: <i>{uln}</i> ;"+
                        f"\n<b>User Username</b>: <i> {uun} </i>;")

@ub.on_message(filters.command('tr'))
def Langtranslator(ub,message):
    print("hi")
    text = message.reply_to_message.text 
    #message.TranslateText(to_lang="es",text=text)
    ub.invoke(function.message.TranslateText(to_lang="es",text=text))

print("Fineub is running" )
ub.run()
print("go")








