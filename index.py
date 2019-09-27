import discord
from discord.ext import commands
import json

#Prefix
client = commands.Bot(command_prefix = '!')
#this is where the bot removes the default help
client.remove_command('help')

# on_ready function
@client.event
async def on_ready():
	print('Bot is ready')

#Help
@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.orange()
	)
	
	embed.set_author(name='Help')
	embed.add_field(name='Info', value='Returns info command', inline=False)
	embed.add_field(name='Moderation Commands', value='Shows moderation commands. || Use !help_moderation for more info', inline=True)
	embed.add_field(name='Prefix', value='Shows prefix',inline=False)
	embed.set_footer(text='Fire || 1.0.0 Beta || All Rights Reserved')
	await ctx.send(embed=embed)
     
#Moderation Help cmd
@client.command(pass_context=True)
async def help_moderation(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	
	embed.set_author(name='Moderation Help')
	embed.add_field(name='Moderation', value= 'warn, ban, mute, unmute, kick', inline=False)
	embed.set_footer(text='Fire || 1.0.0 || All Rights Reserved')
	await ctx.send(embed=embed)
	
#Info command
@client.command(pass_Context=True)
async def info(ctx):
	embed = discord.Embed(
		title = 'Bot Info',
		description = 'Bot Info',
		colour = discord.Colour.blue()
)

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@client.command(hasPermissions, pass_Context = True)
@has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await client.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@client.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await client.say(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await client.say(f"{user.name} has never been reported")  

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await client.send_message(ctx.message.channel, text)   
      embed.set_author(text='Fire')
      embed.add_field(name='Hosted on', value='Python OS', inline=False)
      embed.add_field(name='Devs', value='KINGO', inline=False)
      await ctx.send(embed=embed)

#Prefix cmd
@client.command()
async def prefix(ctx):
	await ctx.send('My prefix is !')
	
#Token run command
client.run('token')


#Made by KING0 ~ All rights reserved
