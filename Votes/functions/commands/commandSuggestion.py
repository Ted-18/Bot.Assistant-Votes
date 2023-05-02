import addons.Votes.handlers.handlerVotes as handlerVotes

import addons.Votes.functions.modals.modalSend as modalSend

import addons.Votes.settings.settingColors as settingColors
import addons.Votes.settings.settingThumbnail as settingThumbnail  

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()



async def suggestion(ctx):

    # PERMISSIONS CHECK
    import addons.Votes.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdVotesSuggestion") == False:
        return
    
    # COMMAND
    
    # Verify if the server has a votes channel
    if handlerVotes.listVotesChannel(ctx.guild.id) == []:
        embed = discord.Embed(title="Votes", description="The server doesn't have a votes channel.\n\n**Command:** `/vote create`", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.voteIcons)
        await ctx.respond(embed=embed)
        return
    else:
        channelID = handlerVotes.listVotesChannel(ctx.guild.id)[0][0]
        channel = discord.utils.get(ctx.guild.channels, id=channelID)

        if channel is None:
            handlerVotes.deleteVotesChannel(ctx.guild.id, channelID)
            embed = discord.Embed(title="Votes", description="Error channel not found.\n\nHe was removed from the database.", color=settingColors.red)
            embed.set_thumbnail(url=settingThumbnail.voteIcons)
            await ctx.respond(embed=embed)
            return
    
    # Send the modal
    modal = modalSend.Send(title = "Make a suggestion")
    await ctx.send_modal(modal)
    await modal.wait()

    # Get the values
    title = modal.children[0].value
    description = modal.children[1].value
    image = modal.children[2].value

    # Send the announcement
    embed = discord.Embed(
        title=title,
        description=description,
        color=settingColors.yellow
    )

    embed.set_author(name="Suggestion", icon_url=settingThumbnail.voteIcons)

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)

    # Verify if the URL is a valid image URL
    if modal.isImageURL == True:
        embed.set_image(url=image)
    elif modal.isImageURL == False:
        embed.set_image(url="https://i.imgur.com/GwEhbUt.png")    

    # Send the embed and add the reactions to the embed
    message = await channel.send(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

    # Create a thread for the suggestion with the title of the suggestion after the suggestion
    await message.create_thread(name=title)
    
