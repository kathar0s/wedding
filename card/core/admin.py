from django.contrib import admin

# Register your models here.
from card.core.models import InitDatabaseLog

admin.site.register(InitDatabaseLog)
