"""

Discord SelfBot with working embeds!
Author: @t3rminalpro (Telegram)

"""

# Imports
import yaml
import requests
import discord
import os
import sys
import time
from discord.ext import commands

# Configuration
config = yaml.safe_load(open("./config.yml", "r"))
token = config["token"]
prefix = config["prefix"]
resp_mode = config["response"]

# Check token
r = requests.get("https://discord.com/api/users/@me", headers = {"authorization": token}).status_code
if r == 200: pass
else:
  print("Check if the token is entered correctly and is valid.")
  sys.exit(1)

# Bot code
client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), intents = discord.Intents.all(), self_bot = True)
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.invisible)
  print("SelfBot ready to use.")

@client.command(name = "help")
async def help(ctx):
  if resp_mode == "embeds":
    embed = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": f"Discord SelfBot Example Help",
      "description": f"""
Command prefix is "{prefix}".

{prefix}help - shows this text
{prefix}play (text) - set Playing status
{prefix}stream (text) - set Streaming status
{prefix}listen (text) - set Listening to status
{prefix}watch (text) - set Watching status
{prefix}compet (text) - set Competing status
{prefix}type (seconds) - type in a channel N seconds
{prefix}status (status) - set provided status (online, idle, dnd, offline)
{prefix}kill - turn off the bot

Made by @t3rminalpro (Telegram)
""",
      "color": "FF0000",
      "image_url": None
    }).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"""
Discord SelfBot example help;
Command prefix is "{prefix}".
```
{prefix}help - shows this text
{prefix}play (text) - set Playing status
{prefix}stream (text) - set Streaming status
{prefix}listen (text) - set Listening to status
{prefix}watch (text) - set Watching status
{prefix}compet (text) - set Competing status
{prefix}type (seconds) - type in a channel N seconds
{prefix}status (status) - set provided status (online, idle, dnd, offline)
{prefix}kill - turn off the bot
```
Made by @t3rminalpro (Telegram)
""")

@client.command(name = "play")
async def play(ctx, *, text):
  await client.change_presence(activity = discord.Game(text))
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Now, your activity is:",
      "description": f"```\nPlaying {text}\n```"
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"Now, your activity is: `Playing {text}`")

@client.command(name = "stream")
async def play(ctx, *, text):
  await client.change_presence(activity = discord.Streaming(text, url = "https://twitch.tv/404"))
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Now, your activity is:",
      "description": f"```\nStreaming {text}\n```"
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"Now, your activity is: `Streaming {text}`")

@client.command(name = "listen")
async def play(ctx, *, text):
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = text))
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Now, your activity is:",
      "description": f"```\nListening to {text}\n```"
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"Now, your activity is: `Listening to {text}`")

@client.command(name = "watch")
async def play(ctx, *, text):
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = text))
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Now, your activity is:",
      "description": f"```\nWatching {text}\n```"
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"Now, your activity is: `Watching {text}`")

@client.command(name = "compet")
async def play(ctx, *, text):
  await client.change_presence(activity = discord.ActivityType.competing, name = text)
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Now, your activity is:",
      "description": f"```\nCompeting {text}\n```"
}).text
    await ctx.send("||" + str(json.loads(embed)['embed']) + "||")
  elif resp_mode == "normal":
    await ctx.send(f"Now, your activity is: `Competing {text}`")

@client.command(name = "type")
async def type(ctx, *, seconds)
  async with ctx.typing(float(seconds)):
    time.sleep(float(seconds))
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": f"I have finished typing.",
      "description": f"It took {seconds} seconds."
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"I have finished typing. It took {seconds} seconds.")

@client.command(name = "status")
async def status(ctx, *, status):
  type = None
  if status == "online": type = discord.Status.online
  elif status == "idle": type = discord.Status.idle
  elif status == "dnd": type = discord.Status.dnd
  elif status == "offline": type = discord.Status.invisible
  await client.change_presence(status = type)
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": f"Now, your status is: {status}"
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send(f"Now, your status is: {status}")

@client.command(name = "kill")
async def bot_kill(ctx):
  if resp_mode == "embeds":
    r = requests.post("https://embd.tk/api/createEmbed", json = {
      "title": "Killing the selfbot process..."
}).text
    await ctx.send(str(json.loads(embed)['embed']))
  elif resp_mode == "normal":
    await ctx.send("Killing the selfbot process...")
  sys.exit(1)
  
client.run(token, bot = False)

