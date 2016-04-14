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
        init_db(self, "register_invited_persons")

        self.stdout.write('Succesfully Init Database')


def register_invited_persons():

    invited_list = [
        {'name': u'방준성'},
        {'name': u'차효준'},
        {'name': u'정나래'},
        {'name': u'김효현'},
        {'name': u'신영섭'},
        {'name': u'이광영'},
        {'name': u'이찬규'},
        {'name': u'김지훈'},
        {'name': u'허두석'},
        {'name': u'권오현'},
        {'name': u'김다슬'},
        {'name': u'조일희'},
        {'name': u'정성진'},
        {'name': u'정희원'},
        {'name': u'이건희'},
        {'name': u'강인구'},
        {'name': u'박윤경'},
        {'name': u'전상호'},
        {'name': u'서준석'},
        {'name': u'박경찬'},
        {'name': u'김준형'},
        {'name': u'이루리'},
        {'name': u'김자연'},
        {'name': u'김가영'},
        {'name': u'변지영'},
        {'name': u'길종훈'},
        {'name': u'박영훈'},
        {'name': u'김재익'},
        {'name': u'정은미'},
        {'name': u'서재오'},
        {'name': u'윤상웅'},
        {'name': u'안혜진'},

        {'name': u'손선화'},
        {'name': u'손선미'},
        {'name': u'이혜민'},
        {'name': u'박우정'},
        {'name': u'김생화'},
        {'name': u'김혜지'},
        {'name': u'박희연'},
        {'name': u'구자민'},
        {'name': u'장성은'},
        {'name': u'문슬기'},
        {'name': u'노서영'},
        {'name': u'송하나'},
        {'name': u'윤세진'},
        {'name': u'이은경', 'last_number': 9063},
        {'name': u'남수해'},
        {'name': u'황성혜'},
        {'name': u'김슬아'},
        {'name': u'윤보연'},
        {'name': u'김은진'},
        {'name': u'백성훈'},
        {'name': u'김재윤'},
        {'name': u'조호연'},
        {'name': u'이지섭'},
        {'name': u'김현정'},
        {'name': u'정승연'},
        {'name': u'김자경'},

        {'name': u'장원석'},
        {'name': u'김윤미'},
        {'name': u'임진경'},
        {'name': u'형성안'},
        {'name': u'김보선'},
        {'name': u'형우식'},
        {'name': u'형성길'},
        {'name': u'최갑남'},
        {'name': u'형승희'},
        {'name': u'형성래'},
        {'name': u'최점덕'},
        {'name': u'형지선'},
        {'name': u'신옥자'},
        {'name': u'김주영'},
        {'name': u'김춘희'},
        {'name': u'신현수'},
        {'name': u'김현식'},
        {'name': u'류승희'},
        {'name': u'신광수'},
        {'name': u'류정희'},
        {'name': u'김기호'},
        {'name': u'류남순'},
        {'name': u'양경욱'},
        {'name': u'류휘경'},
        {'name': u'권인숙'},
        {'name': u'류기성'},
        {'name': u'류희문'},
        {'name': u'윤미나'},
        {'name': u'양용규'},
        {'name': u'신옥순'},
        {'name': u'형성욱'},
        {'name': u'류희순'},
        {'name': u'형지현'},

        {'name': u'백인애'},
        {'name': u'한달원'},
        {'name': u'김기남'},
        {'name': u'한승곤'},
        {'name': u'노나래'},
        {'name': u'한지연'},
        {'name': u'신현태'},
        {'name': u'한규원'},
        {'name': u'서형애'},
        {'name': u'한지윤'},
        {'name': u'김재은'},
        {'name': u'한지원'},
        {'name': u'이규화'},
        {'name': u'한승화'},
        {'name': u'신미남'},
        {'name': u'송홍근'},
        {'name': u'송지희'},
        {'name': u'송연태'},
        {'name': u'송선화'},
        {'name': u'유재구'},
        {'name': u'신중경'},
        {'name': u'김남욱'},
        {'name': u'신중한'},
        {'name': u'오현숙'},
        {'name': u'신범규'},
        {'name': u'신희라'},
        {'name': u'신중구'},
        {'name': u'박명숙'},
        {'name': u'신헌규'},
        {'name': u'설은주'},
        {'name': u'최수혜'},
        {'name': u'한미령'},
        {'name': u'김진회'},
        {'name': u'이은경'},
        {'name': u'김명순'},
        {'name': u'도현석'},
        {'name': u'진명규'},
        {'name': u'유명희'},
        {'name': u'이두성'},
        {'name': u'박순례'},
        {'name': u'한철원'},
        {'name': u'신미현'},
  ]

    for person in invited_list:
        user = User()
        user.name = person['name']
        if 'last_number' in person:
            user.last_number = person['last_number']
        user.is_invited = True
        user.save()


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
