
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here

#----------------#
#读书     #
#----------------#
class reading(models.Model):

    Bookname = models.CharField(u'书名', max_length = 60)
    Author = models.CharField(u'作者', max_length = 60) 
    ISBN = models.CharField(u'ISBN', max_length = 60)
    Category = models.CharField(u'类别', max_length = 60) 
    Picture = models.ImageField(upload_to = 'pictures') 
    Grade = models.IntegerField(u'评分', default = 0) 
    Ranking = models.DateTimeField(u'上榜时间', auto_now_add = True) 
    Price = models.CharField(u'价格', default = 0,  max_length = 130)
    Postage = models.CharField(u'邮费', default = 0,  max_length = 130)
    Abstract = models.CharField(u'简介', max_length = 130) 
    Comment = models.CharField(u'书评', max_length = 130) 
    Quantity =  models.IntegerField(u'数量', default = 0)
    createTime = models.DateTimeField(u'创建时间', auto_now_add = True)
