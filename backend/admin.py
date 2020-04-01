from django.contrib import admin
from . import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(models.Todo)