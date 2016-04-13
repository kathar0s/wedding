# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils import timezone

from card.core.models import InitDatabaseLog
from card.models import User, DefaultMessages


class Command(BaseCommand):
    args = '<no_arguments ...>'
    help = 'Init Database for new environment'

    def handle(self, *args, **options):
        init_db(self, "default_user_init")
        init_db(self, "default_message_init")

        self.stdout.write('Succesfully Init Database')


def default_message_init():
    default_user = User.objects.get(name=u'한의주♥형정석', last_number=u'0104')

    messages = [
        u'안녕하세요. 한의주&형정석의 모바일 청첩장입니다.',
        u'오른쪽 상단 메뉴를 이용하시면 결혼식 정보 및 사진을 볼수 있어요!',
        u'저희에게 축복의 메세지를 여기에 남겨주시면 저희가 보고 답장드려요!'
    ]

    for message in messages:
        default_message = DefaultMessages()
        default_message.message = message
        default_message.user = default_user
        default_message.created_at = timezone.now()
        default_message.save()


def default_user_init():

    User(name=u'형정석', last_number=u'2857', is_staff=True, profile=u'hjs.png').save()
    User(name=u'한의주', last_number=u'9911', is_staff=True, profile=u'hej.png').save()
    User(name=u'한의주♥형정석', last_number=u'0104', is_staff=True, profile=u'hej_hjs.png').save()


def init_db(self, method_name):
    if not is_execute(method_name):
        eval(method_name + "()")
        execute_done(method_name)
        self.stdout.write('Execute %s db init OK' % method_name)


def execute_done(query_id):

    try:
        log = InitDatabaseLog.objects.get(query_id=query_id)
        log.is_execute = True
    except InitDatabaseLog.DoesNotExist:
        log = InitDatabaseLog()
        log.query_id = query_id
        log.is_execute = True

    log.save()


def is_execute(query_id):
    try:
        init_log = InitDatabaseLog.objects.get(query_id=query_id)
        return init_log.is_execute
    except InitDatabaseLog.DoesNotExist:
        return False
