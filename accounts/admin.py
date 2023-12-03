from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.models import Group

from accounts.models import User
from accounts.forms import UserCreationForm, UserChangeForm


class UserAdmin(UserBaseAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'full_name')}),
        ("permission", {'fields': ('is_admin', 'is_active', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password1', 'password2')}),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

