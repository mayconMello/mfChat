from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': (
            'is_staff',
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions',
            'avatar'
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'groups',
                'user_permissions',
                'avatar'
            )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
