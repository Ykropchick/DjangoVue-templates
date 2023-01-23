from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['phone', 'username', 'avatar', "time_registrate", "approved", "banned", 'admin']
    list_filter = ['admin', "time_registrate", "approved", "banned"]
    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        ('Personal info', {'fields': ("username", "avatar", )}),
        ('Permissions', {'fields': ("approved", "banned", 'admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password', 'username', 'avatar', "time_registrate", "approved", "banned", 'admin')}
        ),
    )
    search_fields = ['phone']
    ordering = ['approved']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)