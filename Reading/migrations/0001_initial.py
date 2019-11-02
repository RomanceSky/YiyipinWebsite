# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Bookname', models.CharField(max_length=60, verbose_name='\u4e66\u540d')),
                ('Author', models.CharField(max_length=60, verbose_name='\u4f5c\u8005')),
                ('ISBN', models.CharField(max_length=60, verbose_name='ISBN')),
                ('Category', models.CharField(max_length=60, verbose_name='\u7c7b\u522b')),
                ('Picture', models.ImageField(upload_to=b'pictures')),
                ('Grade', models.IntegerField(default=0, verbose_name='\u8bc4\u5206')),
                ('Ranking', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u699c\u65f6\u95f4')),
                ('Price', models.CharField(default=0, max_length=130, verbose_name='\u4ef7\u683c')),
                ('Postage', models.CharField(default=0, max_length=130, verbose_name='\u90ae\u8d39')),
                ('Abstract', models.CharField(max_length=130, verbose_name='\u7b80\u4ecb')),
                ('Comment', models.CharField(max_length=130, verbose_name='\u4e66\u8bc4')),
                ('Quantity', models.IntegerField(default=0, verbose_name='\u6570\u91cf')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
    ]
