from django.contrib import admin
from .models import User, Media
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin', 'create_at')
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "password1", "password2"],
            },
        ),
    ]

    ordering = ["id", "email"]
    filter_horizontal = []
    search_fields = ["email"]


class MediaAdmin(admin.ModelAdmin):
    list_display = ('user', 'media')


admin.site.register(User, UserAdmin)
admin.site.register(Media, MediaAdmin)