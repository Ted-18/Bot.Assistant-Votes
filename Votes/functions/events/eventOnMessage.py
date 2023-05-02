import addons.Votes.handlers.handlerVotes as handlerVotes
import addons.Votes.settings.settingColors as settingColors
import addons.Votes.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
bot = serviceBot.classBot.getBot()
discord = serviceBot.classBot.getDiscord()

import discord

async def onMessage(message):

    # If its a system message, return
    if message.type != discord.MessageType.default:
        return
    
    
    
    # Remove the message if the message is in a votes channel
    if handlerVotes.isVotesChannel(message.channel.id):

        # If the sender is not me, remove the message
        if message.author.id == bot.user.id:
            
            if message.embeds[0].author.name == "Suggestion":
                if message.embeds[0].author.icon_url == settingThumbnail.voteIcons:
                    return
            
            await message.delete()
            return

        # Send a embed message to the sender
        embed = discord.Embed(
            title="Message removed",
            description="Please use `/votes suggest` to suggest something.",
            color=settingColors.red)
        
        embed.set_author(name="Suggestion", icon_url=settingThumbnail.voteIcons)
        
        # Reply to the message 
        await message.channel.send(embed=embed, mention_author=True, delete_after=10)

        try:
            await message.delete()
        except:
            pass