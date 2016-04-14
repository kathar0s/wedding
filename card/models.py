# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name=u'이름')
    last_number = models.CharField(max_length=4, blank=True, default='', verbose_name=u'전화번호 뒷 4자리')
    is_staff = models.BooleanField(default=False, verbose_name=u'관리자 여부')
    profile = models.CharField(max_length=255, default='', verbose_name=u'프로필 사진 경로')

    date_joined_at = models.DateTimeField(default=timezone.now, verbose_name=u'최초 접속일')
    last_login_at = models.DateTimeField(default=timezone.now, verbose_name=u'최근 접속일')

    def __unicode__(self):
        return u"%s%s" % (self.name, self.last_number)

    class Meta:
        verbose_name_plural = u'사용자 목록'
        verbose_name = u'사용자'


class ChatRooms(models.Model):

    title = models.CharField(max_length=255, verbose_name=u'채팅방 이름')
    owner = models.ForeignKey(User, verbose_name=u'채팅방 소유자')

    members = models.TextField(default='', verbose_name=u'구성원')
    # last_log = models.ForeignKey(ChatLogs, verbose_name=u'최근 메세지 아이디')
    # last_message = models.TextField(default='', verbose_name=u'최근 메세지')
    # last_updated_at = models.DateTimeField(verbose_name=u'최근 업데이트 시간')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'생성시간')

    @property
    def members_names(self):
        member_ids = self.members.split(',')

        members = []
        for member_id in member_ids:
            members.append(User.objects.get(id=member_id))

        return [unicode(m.name) for m in members]

    def __unicode__(self):
        return u"[%s] %s" % (self.id, self.title)

    class Meta:
        verbose_name_plural = u'채팅방 목록'
        verbose_name = u'채팅방'


class ChatLogs(models.Model):
    MESSAGE_TYPES = (
        ('me', u'자신'),
        ('other', u'상대방'),
        ('notice', u'공지')
    )

    chatroom = models.ForeignKey(ChatRooms, db_index=True, verbose_name=u'채팅방',
                                 on_delete=models.CASCADE)
    type = models.CharField(max_length=15, default='me', choices=MESSAGE_TYPES, verbose_name=u'메세지 종류')
    # 누가 쓴 메세지인지
    user = models.ForeignKey(User, verbose_name=u'사용자')
    message = models.TextField(default='', verbose_name=u'메세지')

    unread_count = models.PositiveSmallIntegerField(default=0, verbose_name=u'읽음 표시')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'작성시간')

    def save(self, *args, **kwargs):
        super(ChatLogs, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"[%s] - %s" % (self.id, self.chatroom)

    class Meta:
        verbose_name_plural = u'채팅 목록'
        verbose_name = u'채팅'


class DefaultMessages(models.Model):
    target = models.CharField(max_length=50, default='', verbose_name=u'대상')
    message = models.TextField(default='', verbose_name=u'메세지')

    user = models.ForeignKey(User, null=True, verbose_name=u'보낸 사람')

    created_at = models.DateTimeField(verbose_name=u'생성일(순서)')

    def __unicode__(self):
        return u"[%s] - %s" % (self.user_id, self.message)

    class Meta:
        verbose_name_plural = u'기본 메세지 목록'
        verbose_name = u'기본 메세지'


class Article(models.Model):
    CATEGORIES = (
        ('location', u'위치'),
        ('notice', u'공지'),
        ('calendar', u'일정'),
        ('', u'일반'),
    )

    author = models.CharField(max_length=50, default='', verbose_name=u'작성자')

    category = models.CharField(max_length=20, blank=True, default='', choices=CATEGORIES, verbose_name=u'제목')
    title = models.CharField(max_length=50, default='', verbose_name=u'제목')
    content = models.TextField(default='', verbose_name=u'내용')

    is_notice = models.BooleanField(default=False, verbose_name=u'공지여부')
    is_secret = models.BooleanField(default=False, verbose_name=u'비밀글 여부')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'생성일')

    def __unicode__(self):
        return u"[%s] %s" % (self.category, self.title)

    class Meta:
        verbose_name_plural = u'글 목록'
        verbose_name = u'글'


class Gallery(models.Model):
    title = models.CharField(max_length=50, blank=True, default='', verbose_name=u'제목')
    subscript = models.TextField(default='', blank=True, verbose_name=u'설명')
    path = models.ImageField(upload_to='gallery/', verbose_name=u'이미지')

    def __unicode__(self):
        return u"[%s] %s" % (self.id, self.title)

    class Meta:
        verbose_name_plural = u'갤러리 목록'
        verbose_name = u'갤러리'
