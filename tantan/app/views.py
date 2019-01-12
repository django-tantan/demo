from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse
import random

from redis_cache import cache

from app.models import User,Profile
from django.conf import settings

import oss2
from PIL import Image
import uuid

# Create your views here.
def register(request):
    phonenum=request.POST.get("phonenum")
    token = str(uuid.uuid4())
    nickname = None
    user = None
    if cache.get("phonenum"):
        user = User.objects.get(pk= phonenum)
        nickname=User.objects.get(nickname)
        user.token = token
        str = '1234567890'

        rand_str = ''
        for i in range(0, 6):
            rand_str += str[random.randrange(0, len(str))]
        phone = request.GET.get("phonenum")

        text = "您的验证码是：%s。请不要把验证码泄露给其他人。" % rand_str
        send_sms(text, phone)
    

        # rand_str = "1"
        request.session["verifycode"] = rand_str
        # print("----------------", rand_str)
        return JsonResponse({"error": 0, "data": {"verifycode": rand_str}})
    else:    
        phonenum = request.POST.get("phonenum")
        nickname = request.POST.get("nickname")
        sex = request.POST.get("sex")
        birth_year = request.POST.get("birth_year")
        birth_month = request.POST.get("birth_month")
        birth_day = request.POST.get("birth_day")
        avatar = request.POST.get("avatar")

        location = request.POST.get("location")
        token = str(uuid.uuid4())
        user = User.create(phonenum,nickname,sex,birth_year,birth_month,birth_day,avatar,location,token)
    user.save()
    request.session["phonenum"]= phonenum
    cache.set(phonenum,token)



    return JsonResponse({"error":0,"data":{"phone":User.phonenum,"sex":User.sex,"name":User.nickname,"year":User.birth_year,"month":User.birth_month,"day":User.birth_day,"info":User.avatar,"location":User.location}})









    

