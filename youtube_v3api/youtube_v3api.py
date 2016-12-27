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

