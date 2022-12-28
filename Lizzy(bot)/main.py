#final code has not been tested
# It listens to sad messages and sends encouragements
# It responds to "$inspire" text with encouraging quotes

import discord 
import random
from decouple import config
import json
import requests


client = discord.Client(intents=discord.Intents.all())


# uses api to get random encouraging quotes.
def get_quote():
	response = requests.get("httpsA://zenquotes.io/api/random")
	json_data = json.loads(response.text)

	quote = json_data[0]['q'] +"\
		-" + json_data[0]['a']
	return quote

sad_words = ["depressed", "sad", "depressing", "miserable", "unhappy"]

encouragement = [ "cheer up buddy!", "Hang in there", "I still love you", "You are a great man." ]

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)

	print(f'Message {user_message} by {username} on {channel}')

	if message.author == client.user:
		return

	if channel == "general":
		if user_message.lower() == "$hello" or user_message.lower() == "$hi":
			await message.channel.send(f'Hello {username}')
			return
		elif user_message.lower() == "$bye":
			await message.channel.send(f'Bye {username}')
		elif user_message.lower() == "$tell me a joke":
			jokes = [" Can someone please shed more\
			light on how my lamp got stolen?",
					"Why does no one love me?\
						.",
					"What do you call a gazelle in a \
					lions territory? Denzel."]
			await message.channel.send(random.choice(jokes))

		elif "happy birthday" in user_message.lower():
			await message.channel.send("happy birthday")

		elif any(word in user_message.lower() for word in sad_words) :
			await message.channel.send(random.choice(encouragement))
		

client.run(config('TOKEN'))