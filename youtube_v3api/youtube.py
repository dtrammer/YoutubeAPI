from . import data_api , model

def get_channel(channelid):
    #Retrieves a channel information based on the channelid, returns -> model.Channel
    return data_api.get_channel(channelid)

def get_videos_without_stats(channelid , maxResult = 5 ):
    #Retrieves videos information (exclusive video stats foreach Video) based on a channelid returns -> collection of Video elements
    return data_api.get_videos(channelid , maxResult)

def get_videos_with_stats(channelid , maxResult = 5 ):
    #Retrieves videos information (included video stats foreach Video) based on a channelid returns -> collection of Video elements
    return data_api.get_video_stats(data_api.get_videos(channelid , maxResult))

def search_channels_on_keywords(keywords , maxResults = 10 ):
    #retrieves channel info based on keywords (keywords format, inclusive 'key1|key2|key3|etc' exclusive ' -key', returns -> collection of Channel objects
    maxResults = 50 if maxResults > 50 else maxResults
    return data_api.search_channels(keywords , maxResults )

def search_videos_on_keywords(keywords , maxResults = 10):
    #retrieves channel info based on keywords (keywords format, inclusive 'key1|key2|key3|etc' exclusive ' -key', returns -> collection of Channel objects
    maxResults = 50 if maxResults > 50 else maxResults
    return data_api.search_videos(keywords , maxResults )

