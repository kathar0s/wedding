# -*- coding: utf-8 -*-
import urlparse
from datetime import datetime

import pytz
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from models import User, ChatRooms, ChatLogs, DefaultMessages, Gallery, Article


def index(request):

    template_data = {
        'message': 'hello',
    }

    return render(request, 'index.html', template_data)


def chat(request):
    user, created = get_user(request)

    if user is not None:
        # 현재 들어온 사람에 대한 정보를 일단 불러온다. 없으면 새로 생성

        hjs = User.objects.get(name=u'형정석', last_number=u'2857')
        hej = User.objects.get(name=u'한의주', last_number=u'9911')
        hej_hjs = User.objects.get(name=u'한의주♥형정석', last_number=u'0104')

        members = [hjs, hej, hej_hjs]

        # 구성원에서 자기 자신은 제외한다.
        if user in members:
            members.remove(user)

        # 해당 User가 가지고 있는 방을 가져온다. 없으면 생성
        chatrooms = ChatRooms.objects.filter(owner=user, members=','.join([str(m.id) for m in members]))

        if len(chatrooms) > 0:
            # 사실 지금은 방이 하나만 있어야하는데 여러개 있으면 문제가 있는것.
            chatroom = chatrooms[0]
        else:
            chatroom = ChatRooms.objects.create(owner=user, members=','.join([str(m.id) for m in members]),
                                                title=u','.join([unicode(m.name) for m in members]))

        chatlogs = chatroom.chatlogs_set.all().order_by('created_at')

        gallery = Gallery.objects.all().order_by('id')[:8]
        articles = Article.objects.all().order_by('id')[:4]

        template_data = {
            'user': user,
            'chatroom': chatroom,
            'chatlogs': chatlogs,
            'gallery': gallery,
            'articles': articles,
        }

        return render(request, 'chat.html', template_data)

    # 쿠키값이 없으면 정상접속이 아니므로 첫화면으로 리다이렉트
    else:
        return HttpResponseRedirect(reverse("card:index"))


# 채팅봇 만들기
@transaction.atomic
def chat_bot(request):

    # POST이고 Ajax인 경우에만 처리
    if request.method == "POST" and request.is_ajax():
        data = {
            'error': True,
            'code': 500,
            'message': u'잘못된 접근입니다'
        }

        post = request.POST.copy()

        # 초기 요청인 경우에는 기본 메세지를 보낸다.
        if post['rcode'] == 'greeting':
            # 해당 유저에게 특화된 메세지가 있는지 확인하고 없으면 기본 메세지를 보여준다.
            user, created = get_user(request)
            default_messages = DefaultMessages.objects.filter(target=user.name+user.last_number).order_by('created_at')

            # 해당 유저에게 특화된 메세지가 없는 경우 Default 값을 불러온다.
            if len(default_messages) == 0:
                default_messages = DefaultMessages.objects.filter(target='').order_by('created_at')

            # 초기 초대 참여 공지 추가 (초기 메세지이므로 처음에 삽입한다.)
            chatlog = ChatLogs(user=user, message='')
            chatlog.chatroom_id = post['chatroom']
            chatlog.type = 'notice'
            chatlog.save()

            chatlog.message = u'<strong>%s</strong>님이 <strong>%s</strong>을 초대했습니다.' % (default_messages[0].user.name, user.name)
            chatlog.save()

            messages = []
            for default_message in default_messages:
                messages.append({
                    'message': default_message.message,
                    'name': default_message.user.name
                })

                chatlog = ChatLogs(user=default_message.user, message=default_message.message)
                chatlog.chatroom_id = post['chatroom']
                chatlog.type = 'other'
                chatlog.save()

            data['error'] = False
            data['code'] = 200
            data['message'] = u'초기 인사말 불러오기 완료'
            data['response'] = {
                'messages': messages
            }

        return JsonResponse(data)


def chat_send(request):

    # POST이고 Ajax인 경우에만 처리
    if request.method == "POST" and request.is_ajax():
        data = {
            'error': True,
            'code': 500,
            'message': u'잘못된 접근입니다'
        }

        post = request.POST.copy()

        # 메세지를 저장한다.

        user, created = get_user(request)

        # 메세지 양쪽 공백 제거한 후 길이가 0인 경우에는 저장하지 않는다.
        message = post['message']

        try:
            chatroom = ChatRooms.objects.get(id=post['chatroom'])

            # 요청한 채팅방 주인인지 확인
            # 메세지 길이가 공백제거한 후 1글자라도 있어야 된다.
            if user.id == chatroom.owner.id and len(message.strip()) != 0:
                chatlog = ChatLogs(user=user, message=message)
                chatlog.chatroom_id = post['chatroom']
                chatlog.type = 'me'
                chatlog.unread_count = 1
                chatlog.save()

                data['error'] = False
                data['code'] = 200
                data['message'] = u'메세지 저장 완료'
            else:
                data['message'] = u'메세지 저장 실패'

        except ChatRooms.DoesNotExist:
            data['message'] = u'존재하지 않는 채팅방입니다.'

        return JsonResponse(data)


def get_user(request):
    userinfo = urlparse.unquote(request.COOKIES.get('userinfo'))
    userinfo = dict(urlparse.parse_qsl(userinfo))

    try:
        # 현재 들어온 사람에 대한 정보를 일단 불러온다. 없으면 새로 생성
        user, created = User.objects.get_or_create(name=userinfo['name'])

        # 새로 생기는 경우라면 번호를 입력해준다.
        if created:
            user.last_number = userinfo['last_number']
            user.save()

        # 기존에 이름은 존재하나 번호가 입력되지 않은 경우는 번호를 입력해주고
        # 기존에 등록된 이름과, 전화번호라면 별도로 저장하지 않는다.
        else:
            if len(user.last_number) == 0:
                user.last_number = userinfo['last_number']
                user.save()

            # 번호가 존재하면 지금 입력한 번호와 동일한지 확인하고 동일하지 않는 경우 신규 사용자로 생성한다.
            else:
                if user.last_number != userinfo['last_number']:
                    user = User.objects.create(name=userinfo['name'], last_number=userinfo['last_number'])
                    created = True

        return user, created
    except ValueError:
        return None, False

    # 동명이인의 경우 뒷번호를 조회해서 반환한다.
    except User.MultipleObjectsReturned:
        user, created = User.objects.get_or_create(name=userinfo['name'], last_number=userinfo['last_number'])

        return user, created
