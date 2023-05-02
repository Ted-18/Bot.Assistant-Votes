import addons.Votes.handlers.handlerVotes as handlerVotes

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

import addons.Votes.settings.settingColors as settingColors
import addons.Votes.settings.settingThumbnail as settingThumbnail  

async def channelDelete(ctx):

    # PERMISSIONS CHECK
    import addons.Votes.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdVotesChannelDelete") == False:
        return
        
    # COMMAND
    
    # Verify if the server has a votes channel
    if handlerVotes.listVotesChannel(ctx.guild.id) != []:

        channelID = handlerVotes.listVotesChannel(ctx.guild.id)[0][0]
        channel = discord.utils.get(ctx.guild.channels, id=channelID)

        if channel is None:
            handlerVotes.deleteVotesChannel(ctx.guild.id, channelID)
            embed = discord.Embed(title="Votes", description="Error channel not found.\n\nHe was removed from the database.", color=settingColors.red)
            embed.set_thumbnail(url=settingThumbnail.voteIcons)
            await ctx.respond(embed=embed)
            return
        
        # Verify if the channel is already a votes channel
        if not handlerVotes.isVotesChannel(channel.id):
            embed = discord.Embed(title="Votes", description="The channel is not a votes channel.\n\n**Channel:** " + channel.mention, color=settingColors.red)
            embed.set_thumbnail(url=settingThumbnail.voteIcons)
            await ctx.respond(embed=embed)
            return

        # Embed
        embed = discord.Embed(title="Votes", description="The channel has been removed.\n\n**Channel:** " + channel.mention, color=settingColors.green)
        embed.set_thumbnail(url=settingThumbnail.voteIcons)
        await ctx.respond(embed=embed)

        # Remove the channel from the database
        handlerVotes.deleteVotesChannel(ctx.guild.id, channel.id)

        # Remove all messages from the channel
        await channel.purge()

        # Remove all threads from the channel
        for thread in channel.threads:
            await thread.delete()

        # Remove "This is a votes channel" from the channel topic
        if channel.topic is not None and channel.topic.startswith("📨 This is a votes channel. Use the command `/vote suggest` to suggest something."):
            await channel.edit(topic=channel.topic.replace("📨 This is a votes channel. Use the command `/vote suggest` to suggest something.", ""))
        

    else:
        embed = discord.Embed(title="Votes", description="The server doesn't have a votes channel.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.voteIcons)
        await ctx.respond(embed=embed)