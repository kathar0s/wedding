# -*- coding: utf-8 -*-
from django.contrib.gis.db import models


class InitDatabaseLog(models.Model):

    query_id = models.CharField(max_length=100, db_index=True, unique=True, verbose_name=u'업데이트명')
    is_execute = models.BooleanField(default=False, verbose_name=u'실행 여부')
    execute_date = models.DateTimeField(auto_now_add=True, verbose_name=u'실행일')

    def __unicode__(self):
        return "[%s] %s" % (self.query_id, self.is_execute)

    class Meta:
        verbose_name = u'데이터베이스 업데이트 로그'
        verbose_name_plural = u'데이터베이스 업데이트 로그 목록'
