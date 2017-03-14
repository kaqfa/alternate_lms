from django.contrib import admin
from .models import Member, UserLog


class MemberAdmin(admin.ModelAdmin):
    pass


class UserLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(UserLog, UserLogAdmin)
