from django.contrib import admin
from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass