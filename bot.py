# Work in Progress Bot

# Import discord and necessary libraries for it
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from passlib.hash import pbkdf2_sha256

client = discord.Client()
bot = commands.Bot(command_prefix='p!') # bot prefix, for eg p!manga

# Remove default help command
bot.remove_command('help')


# <--- Console Ready --->
@bot.event
async def on_ready():
    print("Successfully Booted Up!")
    print('------')
    await bot.change_presence(activity=discord.Game(name="Progress-chan | p!help"))

# p!progress
@bot.command()
async def progress(ctx):
    await ctx.send("sfx: Crickets")


# p!manga
@bot.command()
async def manga(ctx, *args):
    list = []
    list = args # stores args of command

    print(list) # prints to console
    await ctx.send("Nothing to see here yet")


#p!chapter
@bot.command()
async def chapter(ctx):
    await ctx.send("ら～ららららららら")


# p!edit 
@bot.command()
async def edit(ctx):
    await ctx.send("¯\_(ツ)_/¯")


# p!estimate
@bot.command()
async def estimate(ctx):
    await ctx.send("42")

@bot.command()
async def help(ctx):
    help_message = open('resources/help.txt').read()
    await ctx.send(help_message)

@bot.command()
async def panic(ctx,arg):
    hash='$pbkdf2-sha256$29000$cC4FACDEmBMCAIBQypmTUg$voQOvKaNTQiump6MtmCFb7d4bTKSiGQ5pfLukN9NPyI'
    if pbkdf2_sha256.verify(arg, hash):
        await ctx.send("cake")
    else:
        await ctx.send("no cake")

# Example embed message
@bot.command()
async def userinfo1(ctx, user: discord.Member = None):
        """
        Gives you info on a user. If a user isn't passed then the shown info is yours.
        """
        if not user:
            user = ctx.author

        embed = discord.Embed(title="{}'s Info".format(user.name), description="Here's What the end product should probably look like.", color=0x0072ff)
        embed.add_field(name="Name", value=user.name)
        embed.add_field(name="Discrim", value=user.discriminator, inline=False)
        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="Status", value=user.status, inline=False)
        embed.add_field(name="Highest Role", value=user.top_role, inline=False)
        embed.add_field(name="Joined At", value=user.joined_at, inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Progress Bot for WiP")
        await ctx.send(embed=embed)

