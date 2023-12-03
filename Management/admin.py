from django.contrib import admin


from .models import Task,Command


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'title',
        'priority',
        'status',
        'deadline', 
        ]
    
@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'task',
        'timestamp', 
        ]
    
