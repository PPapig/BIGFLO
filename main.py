#coding utf-8
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "²")

@bot.event
async def on_ready():
    print("JTE BAN")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User):
    await ctx.guild.ban(user)
    await ctx.send(f"{user} s'est fait ban, ce faux homme.\n https://tenor.com/view/tban-ban-bigflo-oli-bigflo-et-oli-gif-17515232")

bot.run("NzYxNjAwNzgzMzgwNTEyODM4.X3c-AA.NVrzpzyEdPfSbxHrmocNYEjlHh4")
