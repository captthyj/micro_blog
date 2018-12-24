from django.db import models
from django.contrib.auth.models import User

# Create by Limmy at 2018.12.23

# 推文基类
class Base_Post(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    time = models.TimeField(auto_now_add=True)

# 推文类
class Post(Base_Post):
    hits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

# 评论类
class Comment(Base_Post):
    belongs = models.ForeignKey(Post, on_delete=models.CASCADE, default="")

# 回复类
class Reply(Base_Post):
    replyer = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='replyer')
    vic_reply = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='vic_reply')
    belongs = models.ForeignKey(Comment, on_delete=models.CASCADE, default="")

# 关注关系类
class Focus_Rela(models.Model):
    focuser = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='focuser')
    vic_focus = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='vic_focus')

# 点赞关系类
class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    vic_like = models.ForeignKey(Post, on_delete=models.CASCADE, default="")

# @类
class At(models.Model):
    type = models.CharField(max_length=8)
    belongs_id = models.IntegerField()
    ater = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='ater')
    vic_at = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='vic_at')

# 私信类
class Letter(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, default="",related_name='receiver')
    content = models.CharField(max_length=255)
    time = models.TimeField(auto_now_add=True)
