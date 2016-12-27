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

class Video:
    def __init__(self , id , title , desc , pubdate  ,th_d , th_m , th_h , channeltitle):
    #Yotube Video model
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
        return self.id + " - " + self.pubdate + " - " + self.channeltitle + " - " + self.title + self.stats["views"].__str__()