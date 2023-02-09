from django.contrib import admin

from .models import Chat, Group, GroupMember


# Register your models here.

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    pass
