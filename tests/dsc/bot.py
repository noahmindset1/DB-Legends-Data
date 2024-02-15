import discord
from discord.ext import commands
import json

# Load your JSON data
with open('characters.json', 'r') as f:
    json_data = json.load(f)
    
intents = discord.Intents.all()

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Command to search JSON data and send an embed
@bot.command()
async def search(ctx, query: str):
    # Search for the query in the JSON data
    results = [entry for entry in json_data if query.lower() in entry['name'].lower()]

    # If no results found, send a message
    if not results:
        await ctx.send("No results found.")
        return

    # Send an embed for each result
    for result in results:
        embed = discord.Embed(title=result['name'], color=discord.Color.blue())
        embed.add_field(name="Rarity", value=result['rarity'])
        embed.add_field(name="Tags", value=', '.join(result['tags']))
        embed.set_image(url=result['image_url'])
        await ctx.send(embed=embed)

# Run the bot
bot.run('your_bot_token')
