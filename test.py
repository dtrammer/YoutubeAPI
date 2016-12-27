'''Youtube API Test module'''
from youtube_v3api import youtube

if __name__ == '__main__' :
    channel = youtube.get_channel('UChf19X-xjHOQAsZx5GbEk3g')
    print(channel.__str__())
    
    