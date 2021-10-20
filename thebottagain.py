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

if "responding" not in db.keys():
  db["responding"] = True

words = ["hi", "yo", "hello", "wassup", "hi!" , "HI" , "HELLO"]

bot_responses = [
  "maybe the real bots were the friends we made along the way",
  "i hope u feel happy today!",
  "hii",
  "what up G",
  "You, you are.. my universe! and u make my heart light up inside!",
  "what delicious food have u had lately?",
  "im at the best I can be. I hope you are at your best too!",
  "i remember groovy..good times",
  "sometimes im living a life of suppressed rage, emotional imbalance, and denial.",
  "u a baddie",
  "The doctor said I would live.",
  "Thank you for being kind.",
  "Thanks for being a ray of sunshine on my cloudy days",
  "True friendship comes when the silence between two people is comfortable.",
  "you are a blessing",
]

best_valorant = [
  "Faruqi","Daryl","Aqil","Adam","Swattax","Danish","ItsKur0!","Pyantakokay","Ruhul","Benby","Andre","irfan","Sarah <3",
  "Junn","SantanTerselit","Luntur Fit","undrtone.my",
  "xxxmlgwolf","Fid","Aqil","Aqil","Aqil","Aqil","Aqil",
  "Oscar","Bryce","Pushioblinder","Zxile","yedee","Asteriancozmos",
  "Junndilliondiaper","SufianShah","DanishKUROOO","JONATHAN","andreson",
  "Ronin"
]

bot_friendly_responses = [
  "hows the weather?",
  "hope you have a great day!",
  "have a nice day!",
  "Brilliant! I’m glad we are on the same page!",
  "we the best music!",
  "DJ Khaled!!",
  "hope u are doing good in life!",
  "hope u rank up",
  "WE THE BEST MUSIC!!!",
  "You look beautiful today!",
  "you look like a baddie today!",
  "you look pretty today!",
  "you look fine today!",
  "i hope you feel what i felt when u shattered my soul",
  "what song do u wanna recommend to everyone today?",
  "any nice pics u wanna share today?",
  "please tell me some of your political views.",
  "Brilliant! I’m glad we are on the same page!",
  "I hope u wake up Chris Breezy",
  "you the best music!!",
  "im running out of time..",
  "please vote for me in the upcoming election",
  "You, you are.. my universe! and u make my heart light up inside!"
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

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

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

bothi = ['hi azim bot' , 'hibot' , 'hi azim' , 'hi bot']
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))   

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

  if any(word in msg for word in words):
    myid = message.author.display_name
    await message.channel.send('%s , ' % myid + random.choice(bot_friendly_responses))
  
  elif any(word in msg for word in bothi):
    await message.channel.send(random.choice(bot_responses))

  elif any(word in msg for word in dababy_responses):
    await message.channel.send(random.choice(letsgo_responses))   

  elif message.content.startswith('best valorant'):  
    await message.channel.send(random.choice(best_valorant))
  elif message.content.startswith('worst valorant'):  
    await message.channel.send(random.choice(best_valorant))

  elif message.content.startswith('best vandal'):  
    await message.channel.send(random.choice(vandal_skins)) 
  elif message.content.startswith('worst vandal'):  
    await message.channel.send(random.choice(vandal_skins))    

  elif message.content.startswith('best phantom'):  
    await message.channel.send(random.choice(phantom_skins)) 
  elif message.content.startswith('worst phantom'):  
    await message.channel.send(random.choice(phantom_skins)) 

  elif message.content.startswith('best operator'):  
    await message.channel.send(random.choice(operator_skins)) 
  elif message.content.startswith('worst operator'):  
    await message.channel.send(random.choice(operator_skins)) 

  elif message.content.startswith('best sheriff'):  
    await message.channel.send(random.choice(sheriff_skins)) 
  elif message.content.startswith('worst sheriff'):  
    await message.channel.send(random.choice(sheriff_skins)) 

  elif message.content.startswith('best classic'):  
    await message.channel.send(random.choice(classic_skins)) 
  elif message.content.startswith('worst classic'):  
    await message.channel.send(random.choice(classic_skins)) 

  elif message.content.startswith('-inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options.append(db["encouragements"])

    elif any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  elif msg.startswith("-new"):
    encouraging_message = msg.split("-new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")  

  elif msg.startswith("-del"):
    encouragements =[]
    if "encouragements" in db.keys():
      index = int(msg.split("-del",1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)   

  elif msg.startswith("-list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  elif msg.startswith("-responding"):
    value = msg.split("-responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  elif message.content.startswith('praise to lord daryl!'):
    for i in range(3):
      await message.channel.send('praise to lord daryl!')

  elif any(word in msg for word in amogus_words):
    for i in range(5):
      await message.channel.send('AMOGUS???')

  elif message.content.startswith('yes'):
    await message.channel.send('you know it.')

  elif message.content.startswith('no'):
    await message.channel.send('negative')     

  elif message.content.startswith('fuck u'):
    await message.channel.send('stfu u didnt have to be a lil bitch bout it')

  elif message.content.startswith('fuck you'):
    await message.channel.send('stfu u didnt have to be a lil bitch bout it')  

  elif message.content.startswith('fuck this bot'):
    await message.channel.send('f ur mum and ur dad lil bitch, what?gonna cry? well u should since u cant make a bot like me, huh? lil bitch stfu sit down, be humble')   

  elif message.content.startswith('shut up'):
    await message.channel.send('no u shut the fuck up lil pussy ass bitch, watch ur language cibai cock')  

  elif any(word in msg for word in shakes_words):
    await message.channel.send('SUPASTRIKAS')
       

  else:
    return      
                     
keep_alive()
client.run(os.getenv('TOKEN'))    
