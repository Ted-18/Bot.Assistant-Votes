# ADDON IMPOTS
import addons.Votes.init as init

import addons.Votes.functions.commands.commandRequirements as commandRequirements
import addons.Votes.functions.commands.commandChannelCreate as commandChannelCreate
import addons.Votes.functions.commands.commandChannelDelete as commandChannelDelete
import addons.Votes.functions.commands.commandSuggestion as commandSuggestion

import addons.Votes.functions.events.eventOnMessage as eventOnMessage

import addons.Votes.handlers.handlerDatabaseInit as handlerDatabaseInit
import addons.Votes.handlers.handlerVotes as handlerVotes

# BOTASSISTANT IMPORTS
from services.serviceLogger import consoleLogger as Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()

import discord

class Votes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # EVENTS LISTENERS
    @commands.Cog.listener()
    async def on_message(self, message):
        await eventOnMessage.onMessage(message)
        

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if handlerVotes.isVotesChannel(channel.id):
            handlerVotes.deleteVotesChannel(channel.guild.id, channel.id)


    # INIT GROUP COMMAND
    groupVotes = discordCommands.SlashCommandGroup(init.cogName, "Various commands to manage Votes")


    # Verify if the bot has the prerequisites permissions
    @groupVotes.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)

    # CREATE
    @groupVotes.command(name="create", description="Create a votes channel.")
    async def cmdCreate(
        self,
        ctx,
        channel: discord.Option(discord.TextChannel, channel_types = [discord.ChannelType.text], required=True),
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the create command.", str(ctx.command))
        await commandChannelCreate.channelCreate(ctx, channel)

    
    # DELETE
    @groupVotes.command(name="delete", description="Delete a votes channel.")
    async def cmdDelete(
        self,
        ctx
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the delete command.", str(ctx.command))
        await commandChannelDelete.channelDelete(ctx)

    
    # Suggestion
    @groupVotes.command(name="suggest", description="Suggest something.")
    async def cmdSuggest(
        self,
        ctx
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the suggest command.", str(ctx.command))
        await commandSuggestion.suggestion(ctx)

        
# INIT COG
def setup(bot):
    if debug: Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(Votes(bot))
