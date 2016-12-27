"""This script contains the definitions of Youtube objects"""
class Channel:
    #Youtube Channel model
    def __init__(self , id , title , desc , pubdate ,th_d , th_m , th_h ):
        self.id = id
        self.title = title
        self.desc = desc
        self.pubdate = pubdate
        self.thumb_default = th_d
        self.thumb_medium = th_m
        self.thumb_high = th_h
        self.stats = {'views':0,'comments':0,'subs':0,'videos':0}
        self.videos = []

    def __str__(self):
        return self.id + " - " + self.title

    def str_all(self):
        return self.id + " - " + self.title + " - " + self.desc + " - " + self.pubdate + " - " + self.thumb_default + " - " + self.thumb_medium + " - " + self.thumb_high

class Video:
    def __init__(self , id , title , desc , pubdate  ,th_d , th_m , th_h , channelid , channeltitle):
    #Youtube Video model
        self.channelid = channelid
        self.id = id
        self.pubdate = pubdate
        self.title = title
        self.desc = desc
        self.thumb_default = th_d
        self.thumb_medium = th_m
        self.thumb_high = th_h
        self.channeltitle = channeltitle
        self.stats = { 'views':0 , 'likes':0 , 'dislikes':0 , 'comments':0 }

    def str_nice(self):
        return self.id + " - " + self.pubdate + " - " + self.channeltitle + " - " + self.title + " - views : " + self.stats["views"].__str__() + " - likes : " + self.stats["likes"].__str__() + " - dislikes : " + self.stats["dislikes"].__str__()