# coding=utf-8
class Movie():
    """
    定义电影类
    Attributes:
        title: 电影标题.
        post_image: 电影海报图片地址.
        youtube_url: 电影youtube播放链接
    """
    def __init__(self,title,post_image,youtube_url):
        '''实例化电影类，接受电影标题，海报图片地址，youtube播放链接参数'''
        self.title = title
        self.poster_image_url = post_image
        self.trailer_youtube_url = youtube_url
