# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
#用户信息
class userinfo(models.Model):
    username = models.CharField(max_length=10)  #用户名
    password = models.CharField(max_length=20)  #密码
    hobbytype = models.CharField(max_length=7)  #兴趣爱好
    age = models.IntegerField()                 #年龄
    job = models.CharField(max_length=10)       #工作
    family = models.CharField(max_length=10)    #家庭状况

#用户收货地址
class useraddress(models.Model):
    username = models.CharField(max_length=10)  #收货人姓名
    address = models.CharField(max_length=40)   #地址信息

#共享物品的信息
class data(models.Model):
    Img = models.FileField(upload_to='./static/Imginfo')    #物体信息的图片
    hobby = models.CharField(max_length=7)  #物体对应的爱好
    thing = models.CharField(max_length=10)  #具体的物品类别,电子产品，书籍文献，日常用品，其它工具
    brand = models.CharField(max_length=10)    #物品的品牌
    thingname = models.CharField(max_length=20) #具体的物品名称
    paymoney = models.IntegerField()    #物品的押金
    needmoney = models.IntegerField()   #物品的租金
