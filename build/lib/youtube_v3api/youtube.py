from . import data_api , model

def get_channel(channelid , APIKey):
    #Retrieves a channel information based on the channelid, returns -> model.Channel object
    return data_api.get_channel(channelid, APIKey)

def get_videos_without_stats(channelid , APIKey , maxResult = 5 , orderBy = 'viewCount'):
    '''Retrieves videos information (exclusive video stats for each Video, is faster than with stats) based on a channelid returns -> collection of model.Video elements
        by default the youtube query response is ordered by viewCount. 
        OrderBy valid values : viewCount, title, rating, date '''
    return data_api.get_videos(channelid , maxResult , APIKey , orderBy)

def get_videos_with_stats(channelid , APIKey ,  maxResult = 5  , orderBy = 'viewCount'):
    '''Retrieves videos information (inclusive video stats for each Video, this generates extra queries) based on a channelid returns -> collection of model.Video elements
        by default the youtube query response is ordered by viewCount. 
        OrderBy valid values : viewCount, title, rating, date '''
    return data_api.get_video_stats(data_api.get_videos(channelid , maxResult , APIKey, orderBy), APIKey)

def search_channels_on_keywords(keywords , APIKey, maxResults = 10 , orderBy = 'viewCount'):
    '''retrieves channel info based on keywords (keywords format=string, inclusive ex: 'key1|key2|key_n' exclusive ex: ' -key1 -key2', returns -> collection of model.Channel objects
        by default the youtube query response is ordered by viewCount.
        OrderBy valid values : viewCount, title, rating, date, videoCount
        Maxresult is maximum 50'''
    return data_api.search_channels(keywords , maxResults , APIKey ,orderBy)

def search_videos_on_keywords(keywords , APIKey , maxResults = 10 , orderBy = 'viewCount'):
    '''retrieves channel info based on keywords (keywords format=string, ex: 'key1|key2|key_n' exclusive ex: ' -key1 -key2', returns -> collection of model.Channel objects
        by default the youtube query response is ordered by viewCount. 
        OrderBy valid values : viewCount, title, rating, date
        Maxresult is maximum 50'''
    return data_api.search_videos(keywords , maxResults , APIKey , orderBy )
