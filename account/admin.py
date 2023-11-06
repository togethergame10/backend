from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import User


class MyUserAdmin(UserAdmin):
    model = User
    # 유저 목록
    list_display = ['username', 'nickname', 'username', 'email']

    # 유저 정보 관리 페이지 정보 입력창 추가
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname',)}),
    )


admin.site.register(User, MyUserAdmin)
