import addons.Votes.handlers.handlerVotes as handlerVotes

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

import addons.Votes.settings.settingColors as settingColors
import addons.Votes.settings.settingThumbnail as settingThumbnail  

async def channelCreate(ctx, channel):

    # PERMISSIONS CHECK
    import addons.Votes.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdVotesChannelCreate") == False:
        return
    
    # COMMAND
    
    # Verify if the server has a votes channel
    if handlerVotes.listVotesChannel(ctx.guild.id) != []:

        channelID = handlerVotes.listVotesChannel(ctx.guild.id)[0][0]
        channelDB = discord.utils.get(ctx.guild.channels, id=channelID)

        if channelDB is None:
            handlerVotes.deleteVotesChannel(ctx.guild.id, channelID)
            embed = discord.Embed(title="Votes", description="Error channel not found.\n\nHe was removed from the database.", color=settingColors.red)
            embed.set_thumbnail(url=settingThumbnail.voteIcons)
            await ctx.respond(embed=embed)
            return

        embed = discord.Embed(title="Votes", description="The server already has a votes channel.\n\n**Channel:** " + channelDB.mention, color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.voteIcons)
        await ctx.respond(embed=embed)
        return
    
    # Embed
    embed = discord.Embed(title="Votes", description="The channel has been set as a votes channel.\n\n**Channel:** " + channel.mention, color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.voteIcons)
    await ctx.respond(embed=embed)

    # Add "This is a votes channel" to the channel topic
    if channel.topic is None:
        await channel.edit(topic="📨 This is a votes channel. Use the command `/vote suggest` to suggest something.")

    # Remove all messages from the channel
    await channel.purge()

    # Remove all threads from the channel
    for thread in channel.threads:
        await thread.delete()

    # Add the channel to the database
    handlerVotes.addVotesChannel(ctx.guild.id, channel.id)