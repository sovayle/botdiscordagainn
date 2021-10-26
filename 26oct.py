import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

amogus_words = ["among us", "AMONG US" , "AMOGUS" , "AMONG" , "among" , "amogus???" , "AMONGUS???" , "AMONGUS??" , "AMONGUS?" , "AMOGUS???" , "AMOGUS??" , "AMOGUS?" , "AMONG US???" , " AMONG US??" , "AMONG US?", "amongus" , "Amongus" , "Amogus" , "Among us"]

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]


starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]
newer_encouragements = ["hello u have uninspire too much, please inspire yourself"]

if "responding" not in db.keys():
  db["responding"] = True

words = ["hi", "yo", "hello", "wassup", "hi!" , "HI" , "HELLO"]

bot_responses = [
  "maybe the real bots were the friends we made along the way",
  "i hope u feel happy today!",
  "hii",
  "what up G",
  "you, you are.. my universe! and u make my heart light up inside!",
  "what delicious food have u had lately?",
  "im at the best I can be. I hope you are at your best too!",
  "i remember groovy..good times",
  "sometimes im living a life of suppressed rage, emotional imbalance, and denial.",
  "u a baddie",
  "the doctor said I would live.",
  "thank you for being kind.",
  "thanks for being a ray of sunshine on my cloudy days",
  "true friendship comes when the silence between two people is comfortable.",
  "you are a blessing",
  "hows the weather?",
  "hope you have a great day!",
  "Brilliant! I’m glad we are on the same page!",
  "we the best music!",
  "DJ Khaled!!",
  "hope u are doing good in life!",
  "hope u rank up",
  "WE THE BEST MUSIC!!!",
  "you look beautiful today!",
  "you look like a baddie today!",
  "you look pretty today!",
  "you look fine today!",
  "i hope you feel what i felt when u shattered my soul",
  "what song do u wanna recommend to everyone today?",
  "any nice pics u wanna share today?",
  "please tell me some of your political views.",
  "you're brilliant! I’m glad we are on the same page!",
  "I hope u wake up Chris Breezy",
  "you the best music!!",
  "im running out of time..",
  "please vote for me in the upcoming election",
  "you, you are.. my universe! and u make my heart light up inside!"
  
]

best_valorant = [
  "Faruqi","Daryl","Aqil","Adam","Swattax","Danish","ItsKur0!","Pyantakokay","Ruhul","Benby","Andre","irfan","Sarah",
  "Junn","SantanTerselit","Luntur Fit","undrtone.my",
  "xxxmlgwolf","Fid","Aqil","Aqil","Aqil","Aqil","Aqil",
  "Oscar","Bryce","Pushioblinder","Zxile","yedee","Asteriancozmos",
  "Junndilliondiaper","SufianShah","DanishKUROOO","JONATHAN","andreson",
  "Ronin"
]

dababy_responses = ["dababy", "Dababy", "dabenby", "DaBaby", "Dabenby", "DaBenby", "DABENBY", "dababi", "DABABY", "DABABY", "Lets go"]

letsgo_responses = ["lets go", "let's go!", "LETS GO", "Let's proceed...i mean lets go", "les go",
  "Let's go!", "Let's Go!", "lesgo", "Lets Go", "Lets go"]

shakes_words = ["shakesman", "SHAKESMAN", "Shakesman", "shakesMAN", "snakesman", "SHAKES", "on 3", "ON 3", "1 2 3", "On 3", "123"]  

vandal_skins = ["Aristocrat Vandal","Avalanche Vandal","Cavalier Vandal",
"Depths Vandal,""Dot Exe Vandal","Ego Vandal","Elderflame Vandal","Forsaken Vandal","Glitchpop II Vandal","Hivemind Vandal","Horizon Vandal","K/TAC Vandal","Luxe Vandal","Origin Vandal","Prime Vandal","Prism II Vandal","Reaver Vandal","Ruin Vandal","Sakura Vandal","Sensation Vandal","Sentinels Of Light Vandal","Silvanus Vandal","Tethered Realms Vandal","Wasteland Vandal","Winter Wonderland Vandal"]

phantom_skins=["Avalanche Phantom","BlastX Phantom","Celestial Phantom","Galleria Phantom","Glitchpop II Phantom","Go Volume 1 Phantom","Infinity Phantom","Ion Phantom","Kingdom Phantom","Lightwave Phantom","Minima Phantom","Nebula Phantom","Oni Phantom","Prime 2 Phantom","Prism Phantom","Recon Phantom","Ruination Phantom","Rush Phantom","Serenity Phantom","Silvanus Phantom","Singularity Phantom","Smite Phantom",
"Spline Phantom","Winter Wonderland Phantom"]

operator_skins=["Aerosol Operator","Cavalier Operator","Convex Operator","Elderflame Operator","Forsaken Operator","Glitchpop II Operator",
"Gravitational Uranium Neuroblaster Operator","Infantry Operator",
"Ion Operator","K/TAC Operator","Luxe Operator","Minima Operator",
"Origin Operator","Prism Operator","Reaver Operator","Red Alert Operator","Ronin Operator","Sentinels Of Light Operator","Silvanus Operator","Spline OperatorTethered Realms Operator"]

sheriff_skins=["Aristocrat Sheriff","Convex Sheriff","Death Wish Sheriff","Game Over Sheriff","Ion Sheriff","K/TAC Sheriff",
"Lightwave Sheriff","Minima Sheriff","Nebula Sheriff",
"Peacekeeper Sheriff","Polyfox Sheriff","Polyfrog Sheriff",
"Prism II Sheriff","Protektor Sheriff","Reaver Sheriff",
"Ronin Sheriff","Sakura Sheriff","Sentinels Of Light Sheriff",
"Silvanus Sheriff","Singularity Sheriff","Surge Sheriff",
"Wasteland Sheriff"]

classic_skins=["Avalanche Classic","FIRE/arm Classic","Final Chamber Classic","Forsaken Classic","Galleria Classic","Glitchpop II Classic",
"Gravitational Uranium Neuroblaster Classic","Imperium Classic",
"Infinity Classic","Kingdom Classic","Pistolinha Classic",
"Prime Classic","Prism III Classic","Red Alert Classic","Sakura Classic","Smite Classic","Songsteel Classic","Spline Classic","Surge Classic"]

yes_responses=["","","","","you know it.","","","","","","","","","","",""]

no_responses=["","","","","he said no didnt he? Give some respect","","","","","","","","","","",""]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_quote2():
  response2 = requests.get("https://www.goodreads.com/quotes/tag/demotivational")
  json_data = json.loads(response2.text)
  quote2 = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote2)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]  

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

bothi = ['hi azim bot' , 'hibot' , 'hi azim' , 'hi bot',"hey bot"]

diss1=["fuck you", "fuck u", "yo bot stfu", "shut up","stfu","shaddap","stfu bot","fucking bot","fuk u","fuc u"]

diss_responses=['stfu u didnt have to be a lil bitch bout it',
'no u shut the fuck up lil pussy ass bitch, watch ur language cibai cock',
'shut up mf',
'piss poor diss, lil bitch',
'leave the server u cumstain',
'fuck you pussy',
'fuck u and ur whole family',
'ur mum',
'suck a cock please, cuntstain',
'do the whole world a favour and kys cunt',
'watch ur tone u lil piece of shit',
'I’m not pefect but atleast I’m not you.'
]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  """channel = client.get_channel(490525976795545602) #  Gets channel from internal cache
  await channel.send(" ") #  Sends message to channel"""   

@client.event
async def on_message(message):
  userid = message.author.name
  if message.author ==client.user:
    return
  #elif userid == 'harrod12345' and message.content.startswith('-p'):
  #  return
  #elif userid == 'harrod12345' and message.content.startswith3('-clear'):
  #  return
  #elif userid == 'harrod12345' and message.content.startswith('-skip'):
  #  return
  #elif userid == 'harrod12345' and message.content.startswith('-next'):
  #  return          
  #elif userid == 'harrod12345' and message.content.startswith('-'):
  #  await message.channel.send('shadap ben')
  #  return  

  msg = message.content  

  if any(word in msg for word in bothi):
    myid = message.author.display_name
    await message.channel.send('%s , ' % myid + random.choice(bot_responses))

  if any(word in msg for word in dababy_responses):
    await message.channel.send(random.choice(letsgo_responses)) 

  if any(word in msg for word in diss1):
    await message.channel.send(random.choice(diss_responses))    

  if message.content.startswith('best valorant') or message.content.startswith('worst valorant') or message.content.startswith('2nd best valorant') or message.content.startswith('3rd best valorant'):  
    await message.channel.send(random.choice(best_valorant))

  if message.content.startswith('best vandal') or message.content.startswith('worst vandal') or message.content.startswith('2nd best vandal') or message.content.startswith('3rd best vandal'):  
    await message.channel.send(random.choice(vandal_skins)) 

  if message.content.startswith('best phantom') or message.content.startswith('worst phantom') or message.content.startswith('2nd best phantom') or message.content.startswith('3rd best phantom'):  
    await message.channel.send(random.choice(phantom_skins))

  if message.content.startswith('best operator') or      message.content.startswith('worst operator') or message.content.startswith('2nd best operator') or message.content.startswith('3rd best operator'):  
    await message.channel.send(random.choice(operator_skins)) 

  if message.content.startswith('best sheriff') or message.content.startswith('worst sheriff') or message.content.startswith('2nd best sheriff') or message.content.startswith('3rd best sheriff'): 
    await message.channel.send(random.choice(sheriff_skins))

  if message.content.startswith('best classic') or message.content.startswith('worst classic') or message.content.startswith('2nd best classic') or message.content.startswith('3rd best classic'):  
    await message.channel.send(random.choice(classic_skins))

  if message.content.startswith('-inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  options = newer_encouragements
  if "encouragements" in db.keys():
      options = options + db["encouragements"].value

  if message.content.startswith('-uninspire'):
      await message.channel.send(random.choice(options))

  if message.content.startswith('-uninspire2'):
    quote2 = get_quote2()
    await message.channel.send(quote2)

  """
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options.append(db["encouragements"])

    elif any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))"""

  if msg.startswith("-new"):
    encouraging_message = msg.split("-new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")  

  if msg.startswith("-del"):
    encouragements =[]
    if "encouragements" in db.keys():
      index = int(msg.split("-del",1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send("Deleted the encouraging message at index " + str(index)  ) 

  if msg.startswith("-list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
      print(encouragements)

  if msg.startswith("-responding"):
    value = msg.split("-responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  if message.content.startswith('praise to lord daryl!'):
    for i in range(3):
      await message.channel.send('praise to lord daryl!')

  if any(word in msg for word in amogus_words):
    for i in range(3):
      await message.channel.send('AMOGUS???')

  if message.content.startswith('yes'):
    await message.channel.send(random.choice(yes_responses))     
  if message.content.startswith('no'):
    await message.channel.send(random.choice(no_responses))

  if message.content.startswith('fuck this bot'):
    await message.channel.send('f ur mum and ur dad lil bitch, what?gonna cry? well u should since u cant make a bot like me, huh? lil bitch stfu sit down, be humble')   

  if any(word in msg for word in shakes_words):
    await message.channel.send('SUPASTRIKAS')



       
print("\n\n\n")
encouragements = []
if "encouragements" in db.keys():
  encouragements = db["encouragements"]
print(encouragements)
print("\n\n\n")
print(encouragements[0])


      
                     
keep_alive()
client.run(os.getenv('TOKEN'))    
  
