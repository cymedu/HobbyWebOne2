# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from .models import userinfo
from .models import useraddress
from .models import data
from django.shortcuts import render_to_response
from django.http import HttpResponse
#链接数据库
import MySQLdb
conn = MySQLdb.connect(host='localhost', port=3306, user='root',passwd='mypassword',db='HobbyOneTest',charset='utf8')
cur = conn.cursor()   #创建并返回游标
# Create your views here.
def aboutusfuc(request):
    return render(request,'aboutus.html')

def contactfuc(request):
    return render(request,'contact.html')

def detailsfuc(request):
    return render(request,'details.html')

def indexfuc(request):
    """
    try:
        if request.method == "POST":
            req = request.POST
            name = req['slider-namename']
            hobby = req['slider-namehobby']
            brand = req['slider-namebrand']
            type = req['slider-nametype']
        else:
            print "noPOST"
    except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    """
    return render(request,'index.html')

def offersfuc(request):
    return render(request,'offers.html')

def registerfuc(request):
    try:
        if request.method == 'POST':
            req = request.POST
            register_name=req['register_name']
            register_hobby=req['register_hobby']
            register_job=req['register_job']
            register_family=req['register_family']
            register_age=req['register_age']
            register_password = req['register_password']
            register_rpassword = req['register_rpassword']
            if register_password == register_rpassword and register_name!="":
                test = userinfo(username=register_name, password=register_password, hobbytype=register_hobby,
                                age=register_age, job=register_job, family=register_family)
                test.save()
                return HttpResponse('注册成功!手动返回')
            else:
                return HttpResponse('两次密码不一致，请重新输入')
        else:
            print "noPOST"
    except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    return render_to_response('register.html')

def signinfuc(request):
    try:
        if request.method == 'POST':
            req = request.POST
            signin_name = req['username']
            signin_password = req['password']
            cur.execute("select * from MainTest_userinfo where username='"+signin_name+"'")
            datanum=cur.execute("select * from MainTest_userinfo where username='"+signin_name+"'")
            data = cur.fetchall()  # 查询结果给data。
            if datanum == 0:
                dictionary_list = []
                result = {}
                result['username'] = 'weizhuceyhm'  #如果未找到相应的用户名
                result['password'] = ''
                jsondata = json.dumps(result, ensure_ascii=False)  # Python的dict --转换成----> json的object
                Arr = json.loads(jsondata)
                dictionary_list.append(Arr)
                all_jsons = json.dumps(dictionary_list)
                return HttpResponse(all_jsons)
            else:
                cur.scroll(0, 'absolute')
                info = cur.fetchmany(datanum)
                # 获取查询结果中列的字段名，如果查询SQL中使用别名，此处显示别名。
                cur.scroll(0, 'absolute')
                fields = cur.description
                column_list = []  # 定义字段名的列表
                for i in fields:
                    column_list.append(i[0])  # 提取字段名#['id', 'username', 'password', 'hobbytype', 'age', 'job', 'family']

                dictionary_list = []  # 定义一个存字典的数组
                for row in data:  # 一次循环，row代表一行，row以元组的形式显示。
                    result = {}  # 定义Python 字典
                    result[column_list[1]] = row[1]
                    result[column_list[2]] = row[2]
                    if(signin_password!=row[2]):
                        dictionary_list1 = []
                        result1 = {}
                        result1['username'] = 'yhmmimabuzhengque'  # 如果未找到相应的用户名
                        result1['password'] = ''
                        jsondata = json.dumps(result1, ensure_ascii=False)  # Python的dict --转换成----> json的object
                        Arr1 = json.loads(jsondata)
                        dictionary_list1.append(Arr1)
                        all_jsons1 = json.dumps(dictionary_list1)
                        return HttpResponse(all_jsons1)
                    jsondata = json.dumps(result, ensure_ascii=False)  # Python的dict --转换成----> json的object
                    Arr = json.loads(jsondata)
                    dictionary_list.append(Arr)

                all_jsons = json.dumps(dictionary_list)
                return HttpResponse(all_jsons)
        else:
            print "noPOST"
    except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    return render(request,'signin.html')

# Create your views here.
from django import forms

class ImgForm(forms.Form):
    headImg = forms.FileField()

def insert(request):
    try:
        if request.method == "POST":
            imgf = ImgForm(request.POST, request.FILES)
            req = request.POST
            thingtype = req['thingtype']
            brand = req['brand']
            thinghobby = req['thinghobby']
            realname = req['realname']
            paymoney = req['paymoney']
            needmoney = req['needmoney']
            if imgf.is_valid():
                print "success"
                #获取表单图片
                Img=imgf.cleaned_data['headImg']
                test = data(Img=Img, hobby=thinghobby, thing=thingtype, brand=brand, thingname=realname, paymoney=paymoney, needmoney=needmoney)
                test.save()
                return HttpResponse('上传成功!')
            else:
                print "fail"
        else:
            imgf = ImgForm()
    except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    return render_to_response('insert.html', {'imgf': imgf})