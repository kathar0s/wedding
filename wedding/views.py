# -*- coding: utf-8 -*-
import urlparse
from datetime import datetime

import pytz
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from models import User, ChatRooms, ChatLogs, DefaultMessages, Gallery, Article


def index(request):

    template_data = {
        'message': 'hello',
    }

    return render(request, 'event.html', template_data)

