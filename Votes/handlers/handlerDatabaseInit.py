import services.serviceDatabase as serviceDatabase

# Create the database if it does not exist
def databaseInit():
    # Table structure
    tableName = "addon_votes_channels"
    columns = [
        ["serverID", "BIGINT NOT NULL"], 
        ["channelID", "BIGINT NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

