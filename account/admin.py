from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
# admin.site.unregister(Group)




class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'is_staff','is_active']
    list_filter = ['is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','gender', 'phone', 'date_of_birth', 'category')}),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','email','category', 'password1', 'password2', 'is_staff','is_active')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)