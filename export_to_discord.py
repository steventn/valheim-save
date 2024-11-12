import discord
from discord.ext import commands
import os
import json

# Rename secrets_template.json to secrets.json
with open("secrets.json") as config_file:
    config = json.load(config_file)

# Replace with your bot token and channel ID
DISCORD_TOKEN = config["DISCORD_TOKEN"]
CHANNEL_ID = int(config["CHANNEL_ID"])

# Define the file path
directory_path = r"C:\Users\Steven\AppData\LocalLow\IronGate\Valheim\worlds_local"

# Initialize bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    try:
        channel = await bot.fetch_channel(CHANNEL_ID)
        if channel:
            # Loop through each file in the directory
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)

                # Check if it's a file
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        await channel.send(f"Uploading file: {filename}", file=discord.File(file, filename=filename))
                    print(f"Uploaded {filename}")
            await channel.send(f"Place files in "
                               fr"C:\Users\NAME_OF_USER\AppData\LocalLow\IronGate\Valheim\worlds_local")
        else:
            print("Channel not found.")
    except discord.NotFound:
        print("Channel not found or the bot lacks permission to access it.")
    except discord.Forbidden:
        print("The bot does not have permission to access this channel.")
    finally:
        await bot.close()

# Run the bot
bot.run(DISCORD_TOKEN)