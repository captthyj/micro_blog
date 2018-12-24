from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from demo.models import *

# Create your views here.

# 注册
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    u = request.POST['u']
    p = request.POST['p']
    e = request.POST['e']
    try:    #查重
        db= (User.objects.get(username= u)|User.objects.get(email=e)).username
        return HttpResponse('该用户名或邮箱已被占用，请重新输入！')
    except: #没有重复
        use=User.objects.create_user(username=u,password=p)
        use.save()
        return HttpResponseRedirect("/")

# 登陆
def signin(request):
    u = request.POST['u']
    p = request.POST['p']
    user=authenticate(username=u,password=p)
    if user is not None:    #验证通过没
        if user.is_active:  #是否被禁用
            login(request,user)
            return HttpResponse("ok")
        else:
            str="Your account is forbidden!"
    else:
        str="Please check your input!"
    return HttpResponseRedirect("/")

# 注销
@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect("/")

# 发表推文
#@login_required
def post(request):
    content = request.POST['c']
    poster = request.user
    p=Post.objects.create(content=content,poster=poster)
    p.save()
    return HttpResponse('发表成功！')

# 发表评论
#@login_required
def comment(request):
    content = request.POST['c']
    poster = request.user
    belongs = request.POST['b']
    c = Comment.objects.create(content=content,poster=poster,belongs_id=belongs)
    c.save()
    return HttpResponse('发表成功！')

# 发表回复
#@login_required
def reply(request):
    content = request.POST['c']
    poster = request.user
    belongs = request.POST['b']
    r = Reply.objects.create(content=content,poster=poster,belongs_id=belongs)
    r.save()
    return HttpResponse('发表成功！')

# 点赞
#@login_required
def like(request):
    liker = request.user
    vic_like = request.POST['v']
    l = Like.objects.create(liker=liker,vic_like_id=vic_like)
    l.save()
    return HttpResponse('对方已收到你的赞！')

# @
#@login_required
def at(request):
    type = request.POST['t']
    belongs_id = request.POST['b']
    ater = request.user
    vic_at = request.POST['v']
    a = At.objects.create(type=type,belongs_id=belongs_id,ater=ater,vic_at_id=vic_at)
    a.save()


    #这里可能还需要加入通知


    return HttpResponse('ok')   # 这里后期可能直接改成创建成功的对象

# 私信
#@login_required
def letter(request):
    sender = request.user
    receiver = request.POST['r']
    content = request.POST['c']
    l = Letter.objects.create(sender=sender,receiver_id=receiver,content=content)
    l.save()
    return HttpResponse('ok')   # 这里后期可能直接改成创建成功的对象


# 请求指定数目的推文
def get_post(request):
    num = request.POST['num']   #请求数量
    time = request.POST['time'] #请求早于该时间点的数据
    userid = request.POST['userid'] #请求指定用户的推文，为空不做限制
    return HttpResponseRedirect("/")

