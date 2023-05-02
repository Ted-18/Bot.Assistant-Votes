# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-Votes"
version = "1.0.0"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "votes"

# Name of the file containing the cog
cogFile = "cogVotes"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "send_messages",
    "add_reactions",
    "manage_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to create the votes channel
    "cmdVotesChannelCreate" : "discord.permission.manage_guild",

    # Permission to remove the votes channel
    "cmdVotesChannelDelete" : "discord.permission.manage_guild",

    # Permission to make a suggestion
    "cmdVotesSuggestion" : "votes.suggestion"
}