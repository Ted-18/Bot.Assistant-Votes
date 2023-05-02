import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

def addVotesChannel(serverID, channelID):
    requestFormat = """
                    INSERT INTO addon_votes_channels
                    (serverID, channelID)
                    VALUES (%s, %s)
                    """
    requestSettings = (serverID, channelID,)

    try:
        if debug == True:
            Logger.debug("[HANDLER][VOTES][ADD] Adding a channel to the DB " + str(serverID) + " " + str(channelID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][VOTES][ADD] DB error addVotesChannel -> " + str(error))


def deleteVotesChannel(serverID, channelID):
    requestFormat = """
                    DELETE FROM addon_votes_channels
                    WHERE serverID = %s AND channelID = %s;
                    """
    requestSettings = (serverID, channelID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][VOTES][DELETE] Deleting a channel from the DB " + str(channelID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][VOTES][DELETE] DB error deleteVotesChannel -> " + str(error))


def listVotesChannel(serverID):
    requestFormat = """
                    SELECT channelID
                    FROM addon_votes_channels
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if debug == True:
            Logger.debug("[HANDLER][VOTES][LIST] Retrieving the list of channels -> " + str(result))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][VOTES][LIST] DB error listVotesChannel -> " + str(error))
        

def isVotesChannel(channelID):
    requestFormat = """
                    SELECT channelID
                    FROM addon_votes_channels
                    WHERE channelID = %s;
                    """
    requestSettings = (channelID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if debug == True:
            Logger.debug("[HANDLER][VOTES][ISVOTECHANNEL] Checking if the channel is a votes channel -> " + str(result))
            
        if result != []:
            return True
        else:
            return False
    
    except Exception as error:
        Logger.error("[HANDLER][VOTES][ISVOTECHANNEL] DB error isVotesChannel -> " + str(error))
