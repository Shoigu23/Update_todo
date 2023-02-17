from django.contrib import admin
from main.models import Todo, Usera
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Todo, TodoAdmin)

class UseraAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
