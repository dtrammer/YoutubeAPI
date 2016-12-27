import requests
import json

from requests.auth import HTTPDigestAuth
from .model import Channel, Video

def get_channel(channelid , APIKey):
    #Retrieves channel information
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id=" + channelid + "&key=" + APIKey
    r = requests.get(url)
    if r.status_code == 200 :
        result = json.loads(r.text)
        channel = Channel(
            channelid,
            result['items'][0]['snippet']['title'],
            result['items'][0]['snippet']['description'],
            result['items'][0]['snippet']['publishedAt'],
            result['items'][0]['snippet']['thumbnails']['default']['url'],
            result['items'][0]['snippet']['thumbnails']['medium']['url'],
            result['items'][0]['snippet']['thumbnails']['high']['url']
        )
        channel.stats["views"] = result['items'][0]['statistics']['viewCount']
        channel.stats["comments"] = result['items'][0]['statistics']['commentCount']
        channel.stats["subs"] = result['items'][0]['statistics']['subscriberCount']
        channel.stats["videos"] = result['items'][0]['statistics']['videoCount']
    return channel

def get_videos(channelid , maxresult , APIKey , orderBy = 'viewCount'):
    #Retrieves videos information
    videosContainer = []
    resultsLimit =  50 if maxresult > 50 else maxresult
    elementCount = 0
    nextPageToken = "go"
    
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo&order=" + orderBy + "&type=video&key=" + APIKey + "&channelId=" + channelid + "&maxResults=" + resultsLimit.__str__()
    r = requests.get(url)
    
    while not (nextPageToken is None):
        
        if r.status_code == 200 :
            result = json.loads(r.text)
            
            if 'nextPageToken' in result :
                nextPageToken = result['nextPageToken']
            else:
                nextPageToken = None

            for video in result['items']:
                videosContainer.append( Video (
                    video['id']['videoId'],
                    video['snippet']['title'],
                    video['snippet']['description'],
                    video['snippet']['publishedAt'],
                    video['snippet']['thumbnails']['default']['url'],
                    video['snippet']['thumbnails']['medium']['url'],
                    video['snippet']['thumbnails']['high']['url'],
                    video['snippet']['channelId'],
                    video['snippet']['channelTitle']
                ))
                
                elementCount += 1
                
                if elementCount == maxresult:
                    return videosContainer

        if not (nextPageToken is None):#sniff sniff
            url = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&pageToken=" + nextPageToken + "&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo&order=viewCount&type=video&key=" + GoogleAPIKey + "&channelId=" + channelid + "&maxResults=" + resultsLimit.__str__()
            r = requests.get(url)

    return videosContainer

def get_video_stats(VideoObjList , APIKey):
    #Retrieves video stats information
    querystring = ""
    queries = []
    counter = 0

    for video in VideoObjList:
        querystring += video.id + ","
        counter += 1
        if counter == 50 :
            querystring = querystring [:-1]
            queries.append(querystring)
            querystring = ""
            counter = 0
    
    querystring = querystring [:-1]
    queries.append(querystring)

    elementCount = 0
    for query in queries:
        url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id=" + query + "&key=" + APIKey
        r = requests.get(url)
        if r.status_code == 200 :
            result = json.loads(r.text)
            for stats in result['items']:
                VideoObjList[elementCount].stats["views"] = stats['statistics']['viewCount']
                VideoObjList[elementCount].stats["likes"] = stats['statistics']['likeCount']
                VideoObjList[elementCount].stats["dislikes"] = stats['statistics']['dislikeCount']
                VideoObjList[elementCount].stats["comments"] = stats['statistics']['commentCount']
                elementCount += 1
    return VideoObjList

def search_channels(keywords , maxResult , APIKey , orderBy = "viewCount" ):
    '''Retrieves channel information based on search criteria, returns -> collection of model.Channel instances
        Orderby valid values : viewCount, rating, date, videoCount
        maxResult is maximum 50'''
    maxResult = 50 if maxResult > 50 else maxResult
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=" + maxResult.__str__() + "&order=" + orderBy + "&q=" + keywords + "&type=channel&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo%2CregionCode&key=" + APIKey
    r = requests.get(url)
    channelContainer = []
    if r.status_code == 200 :
        result = json.loads(r.text)
        for info in result['items']:
            channelContainer.append( Channel(
                info['snippet']['channelId'],
                info['snippet']['title'],
                info['snippet']['description'],
                info['snippet']['publishedAt'],
                info['snippet']['thumbnails']['default']['url'],
                info['snippet']['thumbnails']['medium']['url'],
                info['snippet']['thumbnails']['high']['url']
            ))
    return channelContainer

def search_videos(keywords , maxResult , APIKey , orderBy = "viewCount" ):
    '''Retrieves videos information based on search criteria, returns -> collection of model.Video instances
            Orderby valid values : viewCount, rating, date, videoCount
            maxResult is maximum 50 '''
    maxResult = 50 if maxResult > 50 else maxResult
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=" + maxResult.__str__() + "&order=" + orderBy + "&q=" + keywords + "&type=video&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo%2CregionCode&key=" + APIKey
    r = requests.get(url)
    videoContainer = []
    if r.status_code == 200 :
        result = json.loads(r.text)
        for info in result['items']:
            videoContainer.append( Video(
                info['id']['videoId'],
                info['snippet']['title'],
                info['snippet']['description'],
                info['snippet']['publishedAt'],
                info['snippet']['thumbnails']['default']['url'],
                info['snippet']['thumbnails']['medium']['url'],
                info['snippet']['thumbnails']['high']['url'],
                info['snippet']['channelId'],
                info['snippet']['channelTitle']
            ))
    return videoContainer