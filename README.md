<h1>Youtube v3 API module for Python 3.5</h1>

<h2>Requires :</h2>
    - Python 3.5.2
    - requests 2.12
    - Youtube APIKey that can be obtained with your google account in the developer console

<h2>Install :</h2>
Download the wheel file from the 'dist' folder and launch virtual env in command prompt and enter :

    >>pip install c:\path\to\wheel\file\YoutubeV3API-0.1.1-py3-none-any.whl


<h2>Quick usage :</h2>
    
    from youtube_v3api import youtube

    #Retrieves a channel information based on the channelid, returns -> model.Channel object
    
    mychannel = Channel()
    mychannel = youtube.get_channel(channelid , APIKey)
    
    '''Retrieves videos information (exclusive video stats for each Video, is faster than with stats) 
    based on a channelid returns -> collection of model.Video elements
    by default the youtube query response is ordered by viewCount.
    OrderBy valid values : viewCount, title, rating, date '''
    
    videoElements = []
    videoElements = youtube.get_videos_without_stats(channelid , APIKey , maxResult = 5 , orderBy = 'viewCount')

    '''Retrieves videos information (inclusive video stats for each Video, this generates extra queries) 
    based on a channelid returns -> collection of model.Video elements
    by default the youtube query response is ordered by viewCount. 
    OrderBy valid values : viewCount, title, rating, date '''
    
    videoElements = []
    videoElements = youtube.get_videos_with_stats(channelid , APIKey ,  maxResult = 5  , orderBy = 'viewCount')

    '''retrieves channel info based on keywords 
    (keywords format=string, inclusive ex: 'key1|key2|key_n' exclusive ex: ' -key1 -key2'
    by default the youtube query response is ordered by viewCount.
    OrderBy valid values : viewCount, title, rating, date, videoCount
    Maxresult is maximum 50
    returns -> collection of model.Channel objects'''
    
    channelElements = []
    channelElements = youtube.search_channels_on_keywords(keywords , APIKey, maxResults = 10 , orderBy = 'viewCount')

    '''retrieves channel info based on keywords 
    (keywords format=string, ex: 'key1|key2|key_n' exclusive ex: ' -key1 -key2'
    by default the youtube query response is ordered by viewCount. 
    OrderBy valid values : viewCount, title, rating, date
    Maxresult is maximum 50
    returns -> collection of model.Channel objects'''
    
    videoElements = []
    videoElements = youtube.search_videos_on_keywords(keywords , APIKey , maxResults = 10 , orderBy = 'viewCount')
    
    
<h2>Objects reference</h2>

<table>
    <tr>
    <th colspan=2>Video</th>
    </tr>
    <tr>
        <td>channelid</td><td>The youtube ID of the channel</td>
    </tr><tr>
        <td>id</td><td>The youtube ID of the video</td>
    </tr><tr>
        <td>pubdate</td><td>Video publishing date</td>
    </tr><tr>
        <td>title</td><td>Title of the video</td>
    </tr><tr>        
        <td>desc</td><td>Description of the video</td>
    </tr><tr>
        <td>thumb_default</td><td>The video default thumbnail image link</td>
    </tr><tr>
        <td>thumb_medium</td><td>Medium size thumbnail link</td>
   </tr><tr>
        <td>thumb_high</td><td>High size thumbnail link</td>
    </tr><tr>
        <td>channeltitle</td><td>The channel title</td>
    </tr><tr>
        <td>stats</td><td>A dictionary containing the video statistics, keys<br>
                           Keys { 'views':0 , 'likes':0 , 'dislikes':0 , 'comments':0 }</td>
                           
    </tr>
    
</table>

