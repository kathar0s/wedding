from django.contrib import admin


# Register your models here.
from card.models import User, ChatRooms, ChatLogs, DefaultMessages


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_number', 'is_staff', 'profile', 'date_joined_at', 'last_login_at')
    ordering = ('-id', )
admin.site.register(User, UserAdmin)


class ChatLogsAdmin(admin.ModelAdmin):
    list_display = ('chatroom', 'user', 'message', 'created_at')
    ordering = ('-id', )
admin.site.register(ChatLogs, ChatLogsAdmin)


class ChatRoomsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'members', 'created_at')
    ordering = ('-id', )
admin.site.register(ChatRooms, ChatRoomsAdmin)


class DefaultMessagesAdmin(admin.ModelAdmin):
    list_display = ('target', 'message', 'created_at')
    ordering = ('-id', )
admin.site.register(DefaultMessages, DefaultMessagesAdmin)
