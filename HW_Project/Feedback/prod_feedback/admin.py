# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Feed_back , User

@admin.register(Feed_back)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'rating', 'message', 'created_at', 'is_visible')
    list_filter = ('is_visible', 'created_at')
    search_fields = ('email', 'mobile')
    list_editable = ('is_visible',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

