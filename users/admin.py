from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Additional Info',
#             {
#                 'fields':(
#                     'is_artist',
#                     'is_curator',
#                     'is_viewer'
#                 )
#             }
#         )
#     )

# admin.site.register(User, CustomUserAdmin)