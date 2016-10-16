# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from cmdb.models import Server
from django.contrib.auth.models import User
# Create your models here.


class Release_template(models.Model):
    # 代码发布模板
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'模板名')
    path = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'程序路径')
    servers = models.ManyToManyField(Server)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.path)


class Work_order(models.Model):
    # 更新工单
    name = models.ForeignKey(Release_template, related_name='release_template', verbose_name=u'工单名称')
    apply_user = models.ForeignKey(User, verbose_name=u'申请人')
    apply_time = models.DateTimeField(auto_now_add=True, verbose_name=u'申请时间')
    verify_time = models.DateTimeField(verbose_name=u'审核时间')
    release_time = models.DateTimeField(verbose_name=u'发布时间')
    version_number = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'版本号')
    status = models.IntegerField(default=1, verbose_name=u'工单状态')

    def __unicode__(self):
        return '%s - %s' % (self.name, self.status)
