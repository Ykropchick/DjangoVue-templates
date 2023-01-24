from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['phone', 'username', 'avatar', "approved", "banned", 'admin']
    list_filter = ['admin', "approved", "banned"]
    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        ('Personal info', {'fields': ("username", "avatar",)}),
        ('Permissions', {'fields': ("approved", "banned", 'admin',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('password', 'password2', 'username', 'phone', 'avatar', 'approved', 'banned', 'staff', 'admin',)}
        ),
    )
    search_fields = ['phone']
    ordering = ['approved']
    filter_horizontal = ()


admin.site.register(User)