import requests
import json

from requests.auth import HTTPDigestAuth
from .model import Channel, Video

GoogleAPIKey = "AIzaSyC3_KwHOzCFaU9om8-O1nTyQQDYqRlSg4Q"

def get_channel(channelid):
    #Retrieves channel information
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id=" + channelid + "&key=" + GoogleAPIKey
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

def get_videos(channelid , maxresult ):
    #Retrieves videos information
    videosContainer = []
    resultsLimit =  50 if maxresult > 50 else maxresult
    elementCount = 0
    nextPageToken = "go"
    
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo&order=viewCount&type=video&key=" + GoogleAPIKey + "&channelId=" + channelid + "&maxResults=" + resultsLimit.__str__()
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
                    video['snippet']['channelTitle']
                ))
                
                elementCount += 1
                
                if elementCount == maxresult:
                    return videosContainer

        if not (nextPageToken is None):#sniff sniff
            url = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&pageToken=" + nextPageToken + "&fields=etag%2Citems%2Ckind%2CnextPageToken%2CpageInfo&order=viewCount&type=video&key=" + GoogleAPIKey + "&channelId=" + channelid + "&maxResults=" + resultsLimit.__str__()
            r = requests.get(url)

    return videosContainer

def get_video_stats(videosContainer):
    #Retrieves video stats information
    querystring = ""
    queries = []
    counter = 0

    for video in videosContainer:
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
        url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id=" + query + "&key=" + GoogleAPIKey
        r = requests.get(url)
        if r.status_code == 200 :
            result = json.loads(r.text)
            for stats in result['items']:
                videosContainer[elementCount].stats["views"] = stats['statistics']['viewCount']
                videosContainer[elementCount].stats["likes"] = stats['statistics']['likeCount']
                videosContainer[elementCount].stats["dislikes"] = stats['statistics']['dislikeCount']
                videosContainer[elementCount].stats["comments"] = stats['statistics']['commentCount']
                elementCount += 1
    return videosContainer