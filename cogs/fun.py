import discord
from discord.ext import commands, tasks
from discord.commands import ( 
    slash_command,
)
import json
import requests
import aiohttp
import psutil
from psutil import Process, virtual_memory
from typing import Union, Optional
import random
import asyncio
import time
import datetime
from .utils.config import *
import math
from afks import afks
from discord.utils import get
import numpy as np
import re

class ButtonView(discord.ui.View):
  def __init__(self):
    super().__init__()
  
    button = discord.ui.Button(label='Claim', style=discord.enums.ButtonStyle.green)
  
    self.add_item(button)

kisses = ['https://cdn.nekos.life/kiss/kiss_138.gif', 'https://cdn.nekos.life/kiss/kiss_106.gif', 'https://cdn.nekos.life/kiss/kiss_128.gif', 'https://cdn.nekos.life/kiss/kiss_139.gif', 'https://cdn.nekos.life/kiss/kiss_061.gif']
loves = ['']
cuteim = ['https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218764136337469/868354099043794944.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218760332083200/856799753815326760.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://i.redd.it/o1g3su199hp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/g09y1v5iugp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/hai3526j6hp71.jpg', 'https://i.redd.it/91p1yme33ip71.jpg', 'https://i.redd.it/6lvfdsdp6hp71.jpg', 'https://i.redd.it/5arz0zh57hp71.jpg', 'https://i.redd.it/nxukbymljjp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/w544woii9gp71.jpg', 'https://i.redd.it/6bqrmkzpjgp71.jpg']
slaps = ['https://cdn.weeb.sh/images/B1fnQyKDW.gif', 'https://cdn.weeb.sh/images/ByTR7kFwW.gif', 'https://cdn.weeb.sh/images/HyV5mJtDb.gif', 'https://cdn.weeb.sh/images/SkNimyKvZ.gif', 'https://cdn.weeb.sh/images/HkK2mkYPZ.gif', 'https://cdn.weeb.sh/images/SkSCyl5yz.gif', 'https://cdn.weeb.sh/images/SJx7M0Ft-.gif']
pats = ['https://cdn.nekos.life/pat/pat_035.gif', 'https://cdn.nekos.life/pat/pat_074.gif', 'https://cdn.nekos.life/pat/pat_028.gif', 'https://cdn.nekos.life/pat/pat_022.gif']
jokes = ['']
cats = ['']
password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
advices = ['Respect your elders', 'Speak always truth', 'be honest', 'Think About your future.', 'Think positive.', 'Work hard not going for smart work.', 'Always remember your culture.', 'Trust on god.', 'Never give up.', 'be cool be calm', 'Listen carefully.', 'Remember Your responseblity.', 'Never forget your past.']
margya = ['']
boreds = ['']
gayr = ['1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '68%', '69%', '70%', '71%', '72%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%','100%']
quacks = ['']
carry = ['I\'d slap you, but that will be animal abuse.', 'You must have born on a highway cos\' that\'s where most accidents happen.', 'I would roast you but momma says i\'m ain\'t allowed to burn trash.', 'English maybe I don\'t speak idiot.', 'If I wanted a bitch i would buy a dog.', 'Boys only bully girls If they fancy them.', 'Oh sorry was i supposed to be offnded?', 'Maybe if you ate some of your makeup , You would on pretty the inside.', 'I could argue back but i would be in the wrong too.', 'Go make a hate page if you don\'t like me.', 'If your name is not google stop , acting like you know everything.', 'If you ran like your mouth , you would be in good shape.']
battles = ['']
typeracer = ['Happiness is the reward we get for living to the highest right we know.', 'Babur was the first Mughal emperor in india.', 'Nobody followed up on that email.', 'Gopal pays no attention on his health.', 'Mikesh is unable to follow instructions.', 'Shall we go on a Goa trip?']
dances = ['']
cuddles = ['']
koalas = ['']
pandas = ['']
tickles = ['']
ages = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
truths = ["Are you a hard-working student?",
"Are you into any sports?",
"Are you scared of any animals?",
"Are you scared of dying? Why?",
"Are you scared of ghosts?",
"Are you still a virgin?",
"Can you lick your elbow?",
"Can you see yourself being married to the creepiest kid a your school someday?",
"Can you speak a different language?",
"Can you touch your tongue to your nose?",
"Can you use a pogo stick?",
"Could you go a week without junk food?",
"Could you go two months without talking to your friends?",
"Describe the weirdest dream you've ever had?",
"Describe the weirdest dream you’ve ever had?",
"Describe your most recent dream that you recall.",
"Describe your most recent romantic encounter.",
"Describe your worst kiss ever.",
"Do you believe in love at all?",
"Do you believe in love at first sight?",
"Do you ever talk to yourself in the mirror?",
"Do you have a hidden talent? What is it?",
"Do you have a job? If so, what is your favourite thing about it?",
"Do you have an imaginary friend?",
"Do you have any phobias?",
"Do you have any unusual talents?",
"Do you know how to cook?",
"Do you know how to dance?",
"Do you like doing chores?",
"Do you like to exercise?",
"Do you message people during your classes?",
"Do you prefer apple or android?",
"Do you sing in the shower? What song did you sing the last time?",
"Do you think you will marry your bf/gf? If not, why not?",
"Explain to the person you like least in this group why you like them the least.",
"Have you been in any fights while in school?",
"Have you ever been kissed yet? If so, who was your best kiss?",
"Have you ever bitten a toenail?",
"Have you ever blamed a fart on an animal?",
"Have you ever blamed something that you have done on one of your siblings?",
"Have you ever cheated on a test?",
"Have you ever cheated or been cheated on?",
"Have you ever climbed a tree?",
"Have you ever crapped your pants since you were a child?",
"Have you ever eaten food that you've dropped on the ground? If so, how long was it on the ground?",
"Have you ever fallen asleep during a class?",
"Have you ever had a crush on a teacher?",
"Have you ever had a crush on someone that your best friend has dated?",
"Have you ever had someone write an assignment or a work for you?",
"Have you ever kissed an animal?",
"Have you ever let someone take the blame for something you did?",
"Have you ever lied to your best friend?",
"Have you ever lied to your parents about if you were in classes or not?",
"Have you ever lied to your parents about what you were doing after school?",
"Have you ever peed in a pool?",
"Have you ever picked your nose in public?",
"Have you ever posted something on the internet/social media that you regret?",
"Have you ever pulled a prank on one of your teachers?",
"Have you ever received a love letter?",
"Have you ever ridden the bus without paying the fare?",
"Have you ever stolen something of value worth more than $10?",
"Have you ever stolen something?",
"Have you ever taken money from your roommate?",
"Have you ever taken money that didn't belong to you?",
"Have you ever thrown a party at your house?",
"Have you ever told a lie during a game of Truth or Dare? What was it and why?",
"Have you ever told one of your best friend's secrets, even if you said you wouldn't?",
"Have you ever used someone else's password?",
"Have you ever watched an adult film without your parents knowing?",
"Have you ever worn the same clothes for more than three days?",
"How do you feel about end pieces of a loaf of bread?",
"How do you feel about social media?",
"How far would you go to land the guy or girl of your dreams?",
"How many boyfriends (or girlfriends) have you had?",
"How many days could you go without your partner?",
"How many kids would you like to have?",
"How many siblings do you have?",
"How many times have you skipped class for no reason?",
"How old were you when your parents sat you down for 'the talk' and what did they say (or not say) about 'the birds and the bees'?",
"How soon did you realize that you were in love with your partner?",
"How soon did/do you want start a family?",
"How was your first kiss?",
"If there was no such thing as money, what would you do with your life?",
"If you could be a superhero; what would your power be?",
"If you could be any animal, which one would you be?",
"If you could be any dinosaur; which would it be?",
"If you could be any super villain; who would you be?",
"If you could change one thing on your body, what would it be?",
"If you could dye your hair any colour, what colour would you pick?",
"If you could erase one past experience, what would it be?",
"If you could go anywhere in the world, where would you go?",
"If you could make one wish right this second, what would it be?",
"If you could only hear one song for the rest of your life, what would it be?",
"If you could own your own business one day, what would it be?",
"If you could own your own business one day; what would it be?",
"If you could switch lives with any celebrity for a day, who would it be?",
"If you could take away one bad thing in the world, what would it be?",
"If you could, what would you change about your life?",
"If you had never met your partner, where do you think you would be?",
"If you had the choice to live on your own right now, would you do it?",
"If you have ever cheated, why did you do it?",
"If you suddenly had a million dollars; what would you do with all of your money?",
"If you were a billionaire, what would you spend your time doing?",
"If you were rescuing everyone here from a burning building, but you had to leave one behind, who would it be?",
"If you were to be stuck on a deserted island, which friend would you want with you?",
"If you were to be trapped on an island for 3 days, what would you take with you?"]
dares = ["Act like a monkey and record a video of it.",
"Act like you do not understand human language until your next turn (come up with your own language).",
"Act like your favourite Disney character for the rest of the game.",
"Close your eyes and send a blind text to a random person.",
"Compose a poem on the spot based on something the group comes up with.",
"Everything you say for the next 5 minutes has to rhyme.",
"Everything you say for the next 5 minutes must not contain the words: 'but', 'a', 'the', 'or'",
"Make a freestyle rap song about each person in the group",
"Make a poem using the words 'orange' and 'moose'.",
"Make a poem using the words 'pineapple' and 'apple'.",
"Make a poem using the words 'goose' and 'peanuts'.",
"Make up a poem about the colour blue.",
"Make up a story about a random person in the group.",
"Post 'I love English!' on a social media.",
"Record a video of you dancing, but without music.",
"Record a video of you playing the air drums to a song of your choice.",
"Record a video of you playing the air guitar to a song of your choice.",
"Record an impression of your favourite celebrity.",
"Record an impression of your favourite animal.",
"Record your best evil laugh; as loud as you can.",
"Record your best president impression.",
"Record yourself saying the alphabet backwards.",
"Record yourself singing 'Twinkle Twinkle, Little Star' while beat boxing.",
"Record yourself singing the alphabet without moving your mouth.",
"Record yourself talking about your favourite food in a russian accent.",
"Say 'ya heard meh' after everything you say for the next 5 minutes.",
"Say 'you know what am sayin' after everything you say for the next 5 minutes.",
"Text someone asking them if they believe in aliens, send a screenshot of the conversation.",
"Send an email to one of your teachers, telling them about how your day is going and take a screenshot.",
"Send an unsolicited text message to one of your friends, telling them about how your day is going and take a screenshot.",
"Send the last photo you took with your phone camera.",
"Send the last screenshot you took on your phone.",
"Send the most embarrassing photo on your phone.",
"Send the oldest selfie on your phone.",
"Send a screenshot of your most recent google search history.",
"Send a selfie of you making a funny face.",
"Set your phone language to Chinese for the next 10 minutes.",
"Show the last three people you texted and what the messages said.",
"Text your crush and tell them how much you like them.",
"Use the letters of the name of another player to describe them (ex. SAM : S = Silly ; A = Attractive ; M = Merry)",
"Yell out the first word that comes to your mind, and record it."]
shaadi = ['']
cries = ['']
feeds = ['']
khush = ['']
sharam = ['']
chases = ['']
confuse = ['']
laughes = ['']
cheers = ['']
hugs = ['']
EIGHT_BALL_ANSWERS = [
            "Yeah", "Yes", "Ofcourse", "Ofc", "Ah Yes", "I see in the Prophecy: TRUE!"
            "Nah", "No", 'Nope', 'Never', "I don't think so",
            "idk", "Maybe", "ig", "I'm bored", "You're annoying"
        ]
birthdayfile = './data/databases/bdays.txt'

def sub(self, x: float, y: float):
  return x - y

def add(self, x: float, y: float):
  return x + y

def div(self, x: float, y: float):
  return x / y


def sqrt(self, x: float):
  return math.sqrt(x)

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

def advantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    highRoll = max(a)
    ind = np.argmax(a)
    highRollMath = b[ind]
    return str(highRoll), highRollMath

def disadvantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    lowRoll = min(a)
    ind = np.argmin(a)
    lowRollMath = b[ind]
    return str(lowRoll), lowRollMath


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<a:Fun:958992538222596177>'
		      label = "Fun"
		      description = "Shows all Fun commands"
		      return emoji, label, description
  

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title="Here is a meme for you!", color = DEFAULT_COLOR, timestamp=ctx.message.created_at)
        embed.set_footer(text="Requested by {}".format(ctx.author.name))

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=h ot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

  
    @commands.command()
    async def hug(self, ctx, member: discord.Member):
      random_link = random.choice(hugs)
      embed = discord.Embed(title=f"{ctx.author.name} hugs {member.display_name}!", color = DEFAULT_COLOR);
      embed.set_image(url=f"{random_link}");
      await ctx.send(embed=embed);

    @commands.command(aliases=['echo'])
    async def say(self, ctx, channel: discord.TextChannel =  None, * , s):
      if channel == None:
        channel = ctx.channel
      if s == "@everyone":
        return await ctx.send("You can't ping everyone!")
      if s == "@here":
        return await ctx.send("You can't ping everyone!")
      else:
        await channel.send(f"{s}")

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        embedkiss = discord.Embed(title=f"{ctx.author.name} kisses {member.display_name}", color = DEFAULT_COLOR)

        random_link = random.choice(kisses)
        embedkiss.set_image(url=random_link)

        await ctx.send(embed=embedkiss)

    @commands.command()
    async def love(self, ctx, member: discord.Member):
        embedlove = discord.Embed(title=f"{ctx.author.name} loves {member.display_name}", color =  DEFAULT_COLOR)

        random_link = random.choice(loves)
        embedlove.set_image(url = random_link)
        
        await ctx.send(embed=embedlove)

    @commands.command()
    async def aw(self, ctx):
        embedaw = discord.Embed(title=f"awww", color =  DEFAULT_COLOR)

        random_link = random.choice(cuteim)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command(aliases=['em'])
    async def embed(self, ctx, channel: discord.TextChannel = None, * , em=None):
      if channel == None:
        channel = ctx.channel
        embedem = discord.Embed(title=f"{em}", color =  DEFAULT_COLOR)
        await channel.send(embed=embedem)

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None):
      button = discord.ui.Button(label=f'Badges', style=discord.ButtonStyle.grey)
      if member == None:
        member = ctx.author
      async def button_callback(interaction: discord.Interaction):
        badges = ""
        if ctx.author.public_flags.hypesquad:
          badges = "Hypesquad"
        elif ctx.author.public_flags.hypesquad_balance:
          badges = "Hypesquad Balance"
        elif ctx.author.public_flags.hypesquad_bravery:
          badges = "Hypesquad Bravery"
        elif ctx.author.public_flags.hypesquad_brilliance:
          badges = "Hypesquad Brilliance"
        elif ctx.author.public_flags.early_supporter:
          badges = "Early Supporter"
        elif ctx.author.public_flags.verified_bot_developer:
          badges = "Verified Bot Developer"
        elif ctx.author.public_flags.partner:
          badges = "Partner"
        elif ctx.author.public_flags.bug_hunter:
          badges = "Bug Hunter"
        for i in badges:
          embed1 = discord.Embed(title='Badges', color = DEFAULT_COLOR)
          embed1.set_author(name=f'{member}', icon_url=f'{member.avatar}')
          await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(color = member.color)
      bannerUser = await self.bot.fetch_user(member.id)
      embed.add_field(name=f"__**General Information**__", value=f"**Name:** {member.name}#{member.discriminator}\n **ID**: {member.id}\n **Account Created:** <t:{int(member.created_at.timestamp())}:D>\n **Joined Server On:** <t:{int(member.joined_at.timestamp())}:D>\n **Highest Role:** {member.top_role.mention}")
      embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embed.set_thumbnail(url=member.avatar)
      if not bannerUser.banner:
        pass
      else:
        embed.set_image(url=bannerUser.banner) 
      await ctx.send(embed=embed)

    @commands.command(
        name='avatar',
        aliases=['av', 'ab', 'ac', 'ah', 'pfp', 'avi', 'ico', 'icon'],
        help='get any discord user profile picture'
    )
    async def avatar(self, ctx, user: discord.Member = None):
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        avemb = discord.Embed(
            color=DEFAULT_COLOR,
            title=f"{user}'s Avatar",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not user.avatar.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({user.avatar.replace(format='gif')})"
        )
        avemb.set_image(url=user.avatar.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)

    @commands.command()
    async def servericon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=DEFAULT_COLOR,
            title=f"{server}'s Icon",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not server.icon.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)

    @commands.command(aliases=['mc', 'members'])
    async def membercount(self, ctx):
        embedmem = discord.Embed(title=f"**Members**", description=f"{ctx.guild.member_count}", color = DEFAULT_COLOR, timestamp=ctx.message.created_at)
        embedmem.set_footer(text=f"{ctx.guild.name}")
        await ctx.send(embed=embedmem)

    @commands.command(aliases=['inv'])
    async def invite(self, ctx: commands.Context):
        embed = discord.Embed(title=f"**Invite Link:**", description = f" • [Click here to get {self.bot.user.name}](https://discord.com/oauth2/authorize?client_id=911149764438016101&permissions=8&scope=bot%20applications.commands)\n • [Click here to join my support server](https://discord.gg/hKVrhq6ZaF)\n • [voting soon]", color =  DEFAULT_COLOR, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Made by  Hacker")
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        embedaw = discord.Embed(title=f"{ctx.author.name} slaps {member.display_name}!", color =  DEFAULT_COLOR)

        random_link = random.choice(slaps)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
      embedpat = discord.Embed(title=f"{ctx.author.name} pats {member.display_name}!", color = DEFAULT_COLOR)

      random_link = random.choice(pats)
      embedpat.set_image(url=random_link)
      
      await ctx.send(embed=embedpat)

    @commands.command()
    async def cat(self, ctx):
      embedcat = discord.Embed(timestamp=ctx.message.created_at, color =  DEFAULT_COLOR)
      
      random_link = random.choice(cats)
      embedcat.set_image(url=random_link)

      await ctx.send(embed=embedcat)

    @commands.command()
    async def joke(self, ctx):
      embedjoke = discord.Embed(color = DEFAULT_COLOR)

      random_msg = random.choice(jokes)
      embedjoke.add_field(name=f"**Joke:**", value=f"{random_msg}")

      await ctx.send(embed=embedjoke)

    @commands.command()
    async def advice(self, ctx):
      random_msg = random.choice(advices)
      embed = discord.Embed(title=f"**Get adviced!**", description=f"{random_msg}", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def bored(self, ctx):
      random_msg = random.choice(boreds)
      embed = discord.Embed(title=f"**Get in some work:**", description=f"{random_msg}", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def inspire(self, ctx):
        quote = get_quote()
        embedin = discord.Embed(title=f"Get Inspired!", description=f"{quote}", color =  DEFAULT_COLOR)
        await ctx.send(embed=embedin)

    @commands.command()
    async def dance(self, ctx):
      random_link = random.choice(dances)

      embed = discord.Embed(title=f"**I like to see you dance OwO**", description=f"{ctx.author.mention} has danced for 59 minutes", color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx,*,message):
      emp = discord.Embed(title=f"**Poll!**", description=f"{message}", color =  DEFAULT_COLOR)
      msg = await ctx.send(embed=emp)
      await msg.add_reaction("👍")
      await msg.add_reaction("👎")

    @commands.command()
    async def hack(self, ctx, member: discord.Member):
      random_pass = random.choice(password)
      embed = discord.Embed(title=f"**Hacked!**", description=f"Username - {member.display_name}\n E-Mail - {member.display_name}@gmail.com\n Password - {member.display_name}@{random_pass}", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
      embed = discord.Embed(title=f"{ctx.author.name} kills {member.display_name}", color =  DEFAULT_COLOR)
      
      random_link = random.choice(margya)
      embed.set_image(url = random_link)

      await ctx.send(embed=embed)

    @commands.command()
    async def gay(self, ctx, user: discord.Member):
      random_msg = random.choice(gayr)
      embed = discord.Embed(title=f"{user.display_name}'s gay rate:", description=F"{random_msg}", color =  DEFAULT_COLOR)

      await ctx.send(embed=embed)

    @commands.command()
    async def quack(self, ctx):
      embed = discord.Embed(
        description=f"**Quack Quack🦆**",
        color =  discord.Colour.green()
      )
      random_link = random.choice(quacks)
      embed.set_image(url=random_link)

      await ctx.send(embed=embed)

    @commands.command()
    async def token(self, ctx, user: discord.Member = None):
        list = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
            '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        token = random.choices(list, k=59)
        if user is None:
            user = ctx.author
            await ctx.send(user.mention + "'s token is " + ''.join(token))
        else:
            await ctx.send(user.mention + "'s token is " + "".join(token))

    @commands.command()
    async def roast(self, ctx, member: discord.Member):
      random_msg = random.choice(carry)
      embed = discord.Embed(title=f"{ctx.author.name} roasted {member.display_name}!", description=f"{random_msg}", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def battle(self, ctx, member: discord.Member, user: discord.Member):
      random_msg = random.choice(battles)
      embed = discord.Embed(title=f"{member.display_name} battles {user.display_name}!", description=f"{random_msg}", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def codestats(self, ctx):
      embed = discord.Embed(title=f"**Code Stats:**", description=f"```Files: 16\nLines: 4k+```", color =  DEFAULT_COLOR)
      await ctx.send(embed=embed)

    @commands.command()
    async def typerace(self, ctx):
        starttime = time.time()
        answer = random.choice(typeracer)
        timer = 17.0
        await ctx.send(f"You have {timer} seconds to type: {answer}")

        def is_correct(msg):
            return msg.author==ctx.author

        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=timer)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long :(")

        if guess.content == answer:
            await ctx.send("You got it!")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")

        else:
            await ctx.send("Nope, that wasn't really right")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")



    @commands.command()
    async def age(self, ctx, member: discord.Member):
      random_msg = random.choice(ages)
      embed = discord.Embed(
        title=f"**Age of {member.display_name}**",
        description=f"{random_msg}",
        color =  DEFAULT_COLOR
      )
      await ctx.send(embed=embed)



    @commands.command()
    async def enlarge(self, ctx, emoji: discord.Emoji):
      embed = discord.Embed(
        title=f"**Enlarge!**",
        color =  DEFAULT_COLOR
      )
      embed.set_image(url=emoji.url)
      await ctx.send(embed=embed)

    @commands.command()
    async def users(self, ctx):
      embed = discord.Embed(
        title=f"**Users:**", 
        description=f"{len(set(self.bot.get_all_members()))}",
        color = DEFAULT_COLOR
      )
      await ctx.send(embed=embed)

    @commands.command(aliases=['serverinfo'])
    async def info(self, ctx: commands.Context):
      nsfw_level = ''
      button = discord.ui.Button(label=f'Server icon', style=discord.ButtonStyle.url, url=f'{ctx.guild.icon}')
      button2 = discord.ui.Button(label=f'Roles', style=discord.ButtonStyle.grey)
      view = discord.ui.View()
      view.add_item(button)
      view.add_item(button2)
      if ctx.guild.nsfw_level.name == 'default':
        nsfw_level = '**Default**'
      if ctx.guild.nsfw_level.name == 'explicit':
        nsfw_level = '**Explicit**'
      if ctx.guild.nsfw_level.name == 'safe':
        nsfw_level = '**Safe**'
      if ctx.guild.nsfw_level.name == 'age_restricted':
        nsfw_level = '**Age Restricted**'
      async def button2_callback(interaction: discord.Interaction):
        roles = ""
        for i in ctx.guild.roles:
          roles += "• " + str(i.mention) + "\n"
        embed1 = discord.Embed(title=f'{ctx.guild.name}', description=f'{roles}', color=DEFAULT_COLOR)
        await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(title=f'{ctx.guild.name} | {ctx.guild.id}', color = DEFAULT_COLOR)
      embed.add_field(name=f'**__General Information__**', value=f'**Owner:** {ctx.guild.owner.mention} | {ctx.guild.owner.id}\n**Region:** {ctx.guild.region}\n**Members:**: {ctx.guild.member_count}\n**Created**: <t:{int(ctx.guild.created_at.timestamp())}:D>\n**Server Channels**: {len(ctx.guild.channels)}\n**Server Roles**: {len(ctx.guild.roles)}')
      embed.add_field(name=f'**__Additional__**', value=f'NSFW level: **{nsfw_level}**\nVerification level: **{ctx.guild.verification_level.name}**\nExplicit Content Filter: **{ctx.guild.explicit_content_filter.name}**\n**Boost Teir**: {ctx.guild.premium_tier}\nMax Talk Bitrate: **{int(ctx.guild.bitrate_limit)}** kbps\nEmojis: {len(ctx.guild.emojis)}\nStickers: {len(ctx.guild.stickers)}\nBoost count: {ctx.guild.premium_subscription_count}')
      button2.callback = button2_callback
      await ctx.send(embed=embed, view=view)


    @commands.command()
    async def italicize(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('*' + message + '*')


    @commands.command()
    async def strike(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('~~' + message + '~~')


    @commands.command()
    async def quote(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('> ' + message)


    @commands.command()
    async def code(self, ctx, *, message):
        await ctx.send('`' + message + "`")

    @commands.command()
    async def gender(self, ctx, member: discord.Member):
      embed = discord.Embed(
        description=f"{member.mention}'s gender is None",
        color = discord.Colour.default()
      )
      await ctx.send(embed=embed)

    @commands.command()
    async def bold(self, ctx, *, message):
        await ctx.send('**' + message + '**')


    @commands.command()
    async def censor(self, ctx, *, message):
        await ctx.send('||' + message + '||')


    @commands.command()
    async def underline(self, ctx, *, message):
        await ctx.send('__' + message + '__')

    @commands.command()
    async def cuddle(self, ctx):
      random_link = random.choice(cuddles)
      embed = discord.Embed(color = discord.Colour.default())
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)


    @commands.command()
    async def wizz(self, ctx):
      message6 = await ctx.send(f"`Wizzing {ctx.guild.name}, will take 22 seconds to complete`")
      message5 = await ctx.send(f"`Deleting {len(ctx.guild.roles)} Roles...`")
      message4 = await ctx.send(f"`Deleting {len(ctx.guild.channels)} Channels...`")
      message3 = await ctx.send(f"`Deleting Webhooks...`")
      message2 = await ctx.send(f"`Deleting emojis`")
      message1 = await ctx.send(f"`Installing Ban Wave..`")
      await message6.delete()
      await message5.delete()
      await message4.delete()
      await message3.delete()
      await message2.delete()
      await message1.delete()

    @commands.command()
    async def f(self, ctx, * , message):
      await ctx.send(f"{ctx.author.name} has paid their respect for **{message}**")

    @commands.command()
    async def koala(self, ctx):
      random_link = random.choice(koalas)
      embed = discord.Embed(color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
      random_link = random.choice(pandas)
      embed = discord.Embed(color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def tickle(self, ctx):
      random_link = random.choice(tickles)
      embed = discord.Embed(color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def truth(self, ctx):
      random_msg = random.choice(truths)
      await ctx.send(f"{random_msg}")

    @commands.command()
    async def dare(self, ctx):
      random_msg = random.choice(dares)
      await ctx.send(f"{random_msg}")

    @commands.command()
    async def marry(self, ctx, *, member: discord.Member):
      random_link = random.choice(shaadi)
      embed = discord.Embed(title=f"{ctx.author.name} marries {member.display_name}!", color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
      random_link = random.choice(cries)
      embed = discord.Embed(title=f":sob: {ctx.author.name} crries.", color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def feed(self, ctx, *, member: discord.Member):
      random_link = random.choice(feeds)
      embed = discord.Embed(title=f"{ctx.author.name} Feeds {member.display_name}!", color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def happy(self, ctx):
      random_link = random.choice(khush)
      embed = discord.Embed(color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx):
      random_link = random.choice(sharam)
      embed = discord.Embed(title=f"**{ctx.author.name} blushes.**", color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def chase(self, ctx):
      random_link = random.choice(chases)
      embed = discord.Embed(color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def cheer(self, ctx):
      random_link = random.choice(cheers)
      embed = discord.Embed(color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")

      await ctx.send(embed=embed)

    @commands.command()
    async def laugh(self, ctx):
      random_link = random.choice(laughes)
      embed = discord.Embed(color = DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def confused(self, ctx):
      random_link = random.choice(confuse)
      embed = discord.Embed(color =  DEFAULT_COLOR)
      embed.set_image(url=f"{random_link}")
      await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! {}'.format(round(self.bot.latency * 1000)))
    
    @commands.command()
    async def botinfo(self, ctx):
      proc = Process()
      with proc.oneshot():
        mem_total =virtual_memory().total / (1024**2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
        embed = discord.Embed(color = DEFAULT_COLOR)
        embed.add_field(name=f"**__{self.bot.user.name} Info__**", value=f"**Servers : ** {len(self.bot.guilds)}\n**Users : **{len(set(self.bot.get_all_members()))}\n**Commands : **{len(self.bot.commands)}\n**Memory Usage : **{mem_usage}\n**Total Storage : **`{mem_usage:,.3f} MB`")
        await ctx.send(embed=embed)

    @commands.command()
    async def timer(ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 600:
                await ctx.send("I don't think I can go over 10 mins.")
                raise BaseException
            if secondint <= 0:
                await ctx.send("I don't think I can go to negatives.")
                raise BaseException

            message = await ctx.send(f"Timer: {seconds}")

            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="Ended!")
                    break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)

            await ctx.send(f"{ctx.author.mention}, Your cooldown has been ended!")
        except ValueError:
            await ctx.send("You Must Enter A number!")

    @commands.command()
    async def bday(self, ctx):
        flag = 0
        user = ctx.message.author
        await ctx.send("What is your birthday? Please use DD/MM format.")

        msg = await self.bot.wait_for('message', check=lambda msg: msg.author == ctx.author)
        msg = msg.content

        # Check to see if the date provided is valid
        try:
            list = msg.split("/")
            if int(list[1]) > 13 or int(list[1]) < 1:
                await ctx.send("Invalid date.")
                return
            else:
                pass

            if int(list[1]) in (1, 3, 5, 7, 8, 10, 12):
                if int(list[0]) > 31 or int(list[0]) < 1:
                    await ctx.send("Invalid date.")
                    return
                else:
                    pass
            elif int(list[1]) in (4, 6, 9, 11):
                if int(list[0]) > 30 or int(list[0]) < 1:
                    await ctx.send("Invalid date.")
                    return
                else:
                    pass
            elif int(list[1]) == 2:
                if int(list[0]) > 29 or int(list[0]) < 1:
                    await ctx.send("Invalid date.")
                    return
                else:
                    pass
            else:
                await ctx.send("Invalid date.")
                return
        except:
            await ctx.send("Invalid date.")
            return

        txt = list[0] + list[1] + ' ' + user.display_name + ' ' + str(user.id)
        print(txt)

        # Check if user has a birthday logged already
        fileName = open(birthdayfile, 'r')
        for line in fileName:
            if str(user.id) in line:
                print('User already has a birthday logged')
                flag = 1
        # Add user's birthday to file if not already added
        if flag == 0:
            with open('bdays.txt', 'a') as f:
                f.write(txt + '\n')
                f.close()
                await ctx.channel.send('Your Birthday has been logged!')
        else:
            await ctx.channel.send('You already has a birthday logged')

    @commands.command()
    async def mathadd(self, ctx, x: float, y: float):
        res = add(x, y)
        await ctx.send(res)

    @commands.command()
    async def mathsub(self, ctx, x: float, y: float):
        res = sub(x, y)
        await ctx.send(res)

    @commands.command()
    async def mathdiv(self, ctx, x: float, y: float):
        res = div(x, y)
        await ctx.send(res)

    @commands.command()
    async def mathsqrt(self, ctx, x: int, y: int):
        res = sqrt(x, y)
        await ctx.send(res)

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question) -> None:
        embed = discord.Embed(title=f"8Ball", description=f"Question - {question}\nAnswer - {random.choice(EIGHT_BALL_ANSWERS)}", color = DEFAULT_COLOR);
        await ctx.send(embed=embed)

    @commands.command()
    async def afk(self, ctx, *, reason="I am afk."):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick = f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        await ctx.send(f"{member.name} Your AFK is now set to {reason}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            await message.channel.send(f"{message.author.name}, I removed your AFK.")

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                await message.reply(f"{member.name} is AFK {reason}")

    @commands.command()#for times loop, random(1, sides). multiplier
    async def roll(self, ctx, times=0, sides=0, *, args=None):
        member = ctx.author
        times = int(times)
        sides = int(sides)
        try:
            num = re.sub('[^\d.,]' , '', str(args))
            add = int(num)
            if "-" in args:
                add = "-"+ str(add)
                add = int(add)
        except:
            add = 0
        if not args:
            args = "normal"
        if times == 0 or  sides == 0:
            await ctx.send("Yo bro/sis you need to specify the parts I use\n `roll (how many times) (how many sided dice) (modifier)`")
        else:
            try:
                if 'disadv' in str(args.lower()) or 'disadvantage' in str(args.lower()):
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Disadvantage', colour=discord.Colour.default())
                    result = disadvantageRoll(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
                elif 'adv' in str(args.lower()) or 'advantage' in str(args.lower()):
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Advantage', colour=discord.Colour.default())
                    result = advantageRoll(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
                else:
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Normal', colour=discord.Colour.default())
                    result = fun(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
            except:
                embed = discord.Embed(title='Roll:', description='Roll Type: **ERROR**', colour=discord.Colour.default())
                embed.add_field(name='**ERROR**', value='\uFEFF')
            embed.set_author(icon_url=member.avatar, name=str(member))
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def pokemon(self,ctx,*,pokemon):
      async with aiohttp.ClientSession() as session:
        message0 = await ctx.send("I am looking for that Pokemon. Please be patient.")
        await ctx.channel.trigger_typing()
        response = await session.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon}') # Again, I use the same API. They are really good and I consider using them
        await ctx.channel.trigger_typing()
        if str(response.status) == "404":
            await ctx.send("I couldn't find that pokemon. Please try again.")
        else:
                        rj = await response.json()
                        name = (rj['name']).capitalize()
                        pid = (rj['id'])
                        ptype = (rj['type'])
                        desc = (rj['description'])
                        species = (rj['species'])
                        stats = (rj['stats'])
                        evolfam = (rj['family'])
                        evs = (evolfam['evolutionLine'])
                        evs=str(evs)
                        evs=evs.replace("'","")
                        evs=evs.replace("]","")
                        evs=evs.replace("[","")
                        hp = (stats['hp'])
                        attack = (stats['attack'])
                        defense = (stats['defense'])
                        speed = (stats['speed'])
                        spattack = (stats['sp_atk'])
                        spdef = (stats['sp_def'])
                        abilities = (rj['abilities'])
                        abilities = str(abilities)
                        abilities=abilities.replace("'","")
                        abilities=abilities.replace("[","")
                        abilities=abilities.replace("]","")
                        weight = (rj['weight'])
                        height = (rj['height'])
                        weight = weight.replace(u'\xa0', u' ')
                        height = height.replace(u'\xa0', u' ')
                        species = str(species)
                        species=species.replace("'","")
                        species=species.replace("[","")
                        species=species.replace("]","")
                        species=species.replace(",","")
                        ptype = str(ptype)
                        ptype=ptype.replace("'","")
                        ptype=ptype.replace("[","")
                        ptype=ptype.replace("]","")
                        imgs=(rj['sprites'])
                        if int(rj['generation']) < 6:
                            img=(imgs['animated'])
                        else:
                            img=(imgs['normal'])
                        url = (imgs['normal'])
                        try:
                            idx = await session.get(url)
                            idx = await idx.read()
                            #await url.save(f'{pokemon}av.png',seek_begin = True)
                            embed=discord.Embed(title=name,description=desc,color=random.randint(0, 0xFFFFFF))
                        except:
                            embed=discord.Embed(title=name,description=desc)
                        embed.set_thumbnail(url=img)
                        embed.add_field(name="Information",value=f"Pokedex Entry: {pid}\nFirst introduced in generation {(rj['generation'])}\nType(s): {ptype}\nAbilities: {abilities}",inline=True)
                        embed.add_field(name="Base Stats",value=f"HP: {hp}\nDefense: {defense}\nSpeed: {speed}\nAttack: {attack}\nSpecial Attack: {spattack}\nSpecial Defense: {spdef}",inline=True)
                        if len(evs) != 0:
                            embed.add_field(name="Evolution Line",value=evs,inline=True)
                        await ctx.channel.trigger_typing()
                        await message0.delete()
                        await ctx.send(embed=embed)

    @commands.command()
    async def pikachu(self, ctx):
      response = requests.get('https://some-random-api.ml/img/pikachu')
      data = response.json()
      embed = discord.Embed(
        title = 'Pikachu',
        description = 'Here is a gif of Pikachu.',
        color = 0xfff900
      )
      embed.set_image(url=data['link'])
      embed.set_footer(text="")
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

    @commands.group()
    async def banner(self, ctx: commands.Context):
      ...

    @banner.command()
    async def user(self, ctx: commands.Context, *, member: discord.Member = None):
      if member == None:
        member = ctx.author
      embed = discord.Embed(title=f'{member.name} + {member.discriminator}\'s Banner', color = DEFAULT_COLOR)
      embed.set_image(url=member.banner.url)
      await ctx.send(embed=embed)
    
    @banner.command()
    async def server(self, ctx: commands.Context):
      if not ctx.guild.banner:
        await ctx.send('This server does not have any banner!')
      embed = discord.Embed(title=f'{ctx.guild.name}\'s Banner', color = DEFAULT_COLOR)
      embed.set_image(url=ctx.guild.banner)
      await ctx.send(embed=embed)

    @commands.command(aliases=['match'])
    async def ship(self, ctx: commands.Context, *, user: discord.Member):
      love_count = range(0, 100)
      love_emoji = ""
      if love_count <= 50:
        love_emoji.replace('', '💔')
        embed = discord.Embed(title=f'{ctx.author.name}#{ctx.author.discriminator} {love_emoji} {user.name}#{user.discriminator}', color = DEFAULT_COLOR)
        await ctx.send(content=f'{ctx.author.name}#{ctx.author.discriminator} ships {user.name}#{user.discriminator}',embed=embed)
      else:
        love_emoji.replace('', '💖')
        embed = discord.Embed(title=f'{ctx.author.name}#{ctx.author.discriminator} {love_emoji} {user.name}#{user.discriminator}', color = DEFAULT_COLOR)
        await ctx.send(content=f'{ctx.author.name}#{ctx.author.discriminator} ships {user.name}#{user.discriminator}',embed=embed)



def setup(bot):
    bot.add_cog(fun(bot))
