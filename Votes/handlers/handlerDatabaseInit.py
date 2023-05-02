import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

# Create the database if it does not exist
def databaseInit():
    if settingBot.databaseType == "MariaDB":
        # Table structure
        tableName = "addon_votes_channels"
        columns = [
            ["serverID", "BIGINT NOT NULL"], 
            ["channelID", "BIGINT NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        # Table structure
        tableName = "addon_votes_channels"
        columns = [
            ["serverID", "integer NOT NULL"], 
            ["channelID", "integer NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

