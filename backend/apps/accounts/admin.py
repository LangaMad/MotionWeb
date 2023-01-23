from django.contrib import admin

# Register your models here.
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'avatar',
        'phone',


    ]